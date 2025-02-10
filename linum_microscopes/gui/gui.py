# This Python file uses the following encoding: utf-8
import logging
import sys
import time

import numpy as np
import pyqtgraph as pg
import qdarktheme
from PySide6 import QtCore
from PySide6.QtGui import QPixmap, QActionGroup, QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QDialogButtonBox, QVBoxLayout, QLabel

from linum_microscopes.acquisition_management import AcquisitionStrategy
from linum_microscopes.config import ConfigManager, initialise_logging
from linum_microscopes.controllers import AbstractDevice
# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow


# from linum_microscopes.controllers import pcoCamera
# TODO: put the camera capture in a different thread to avoid freezing the GUI
# TODO: problem with the z range for the PLI
# TODO: add tools to set the min-max range in software for the config (ex: max height for PLI).
# TODO: disable the software during homing sequence.
# TODO: prepare the hardware when starting the GUI instead of when choosing the device (available device should be a config thing on every system)
# TODO: use numpad/joystick to control the stage
# TODO: hide the jog options if the move would be outside the stage limits
# TODO: replace tabs by movable boxes
# TODO: add a busy signal to disable control while actions are in progress (ex. slicing)
# TODO: refactor to have multiple files, one per widget) instead of a big one.
# TODO: keep a list of cutting heights in the params file
# TODO: add options to load and export the slicing and imaging history, logs, etc.


# Tasks
# TODO: deactivate the stage controller if not homed or configured
# TODO: create a separate thread for every hardware component
# FIXME: homing will break the stage polling
# FIXME: the stage seems to go off limits
# TODO: add a message box during homing sequence.
# FIXME: problem with frequent jogs, the GUI freezes


class PauseBetweenCutDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Cutting Pause")

        QBtn = (
                QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        )

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        layout = QVBoxLayout()
        message = QLabel("Start the next slice?")
        layout.addWidget(message)
        layout.addWidget(self.buttonBox)
        self.setLayout(layout)


class MainWindow(QMainWindow):
    config_manager: ConfigManager
    # AbstractDevice governs the thread and connection state
    stage: AbstractDevice
    camera: AbstractDevice
    vibratome: AbstractDevice
    # AcquisitionStrategy houses the functionality of the different devices.
    # For proper type hinting, use the device for interacting with the class and use strategy.device
    # for calling device functionality
    strategy: AcquisitionStrategy

    def __init__(self, parent=None):
        super().__init__(parent)
        self.config_manager = ConfigManager(config_file="config.toml")
        initialise_logging()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_ui()
        self.update_image(np.random.rand(100, 100))
        self.init_viewer()
        self.update_view()

        # Prepare the camera timer
        self.acquisitionStatus = False
        fps = 30
        self.timeInterval = int(1000 / fps)
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.acquire_image)
        self.timer.setInterval(self.timeInterval)
        self.timer.setSingleShot(True)
        if self.acquisitionStatus:
            self.timer.start()

    def init_ui(self):
        # Set the icons
        # self.ui.actionOpen.setIcon(QPixmap("resources/open.svg"))

        # Set menu actions
        microscopeSetupGroupTools = QActionGroup(self)
        microscopeSetupGroupTools.addAction(self.ui.actionMUSE_Microscopy_by_UV_surface_excitation)
        microscopeSetupGroupTools.addAction(self.ui.actionOCT_Optical_Coherence_Tomography)
        microscopeSetupGroupTools.addAction(self.ui.actionOCRT_Optical_Coherence_Refraction_Tomography)
        microscopeSetupGroupTools.addAction(self.ui.actionPLI_Polarized_Light_Imaging)
        microscopeSetupGroupTools.addAction(self.ui.actionS_OCT_Serial_OCT)
        microscopeSetupGroupTools.setExclusive(True)

        # Signal and Slots
        self.ui.actionS_OCT_Serial_OCT.triggered.connect(self.set_microscope_as_soct)
        self.ui.actionPLI_Polarized_Light_Imaging.triggered.connect(self.set_microscope_as_pli)
        self.ui.actionVibratome.triggered.connect(self.set_microscope_as_vibratome)

        # Stage XYZ job control
        self.ui.pushButton_stage_jogX.clicked.connect(self.jog_x)
        self.ui.pushButton_stage_jogXReverse.clicked.connect(self.reverse_jog_x)
        self.ui.pushButton_stage_jogY.clicked.connect(self.jog_y)
        self.ui.pushButton_stage_jogYReverse.clicked.connect(self.reverse_jog_y)
        self.ui.pushButton_stage_jogZ.clicked.connect(self.jog_z)
        self.ui.pushButton_vibratome_jogZ_up.clicked.connect(self.jog_z)
        self.ui.pushButton_stage_jogZReverse.clicked.connect(self.reverse_jog_z)
        self.ui.pushButton_vibratome_jogZ_down.clicked.connect(self.reverse_jog_z)
        self.ui.pushButton_stage_moveToHomeXYZ.clicked.connect(self.homing_xyz)
        self.ui.pushButton_stage_stop.clicked.connect(self.stop_moves)
        self.ui.doubleSpinBox_z_jogstep_mm.valueChanged.connect(self.update_z_jogstep)
        self.ui.doubleSpinBox_vibratome_zStep_mm.valueChanged.connect(self.update_z_jogstep_vibratome)
        self.ui.pushButton_stageXYZ_moveTo.clicked.connect(self.stage_moveto)

        # Rotation stage action
        self.ui.pushButton_pliRot_topJog.clicked.connect(self.jog_top_rot)
        self.ui.pushButton_pliRot_topJogReverse.clicked.connect(self.jog_top_rot_reverse)
        self.ui.pushButton_pliRot_bottomJog.clicked.connect(self.jog_bottom_rot)
        self.ui.pushButton_pliRot_bottomJogReverse.clicked.connect(self.jog_bottom_rot_reverse)
        self.ui.pushButton_pliRot_home.clicked.connect(self.homing_rot)

        # Camera Actions
        self.ui.pushButton_camera_acquire.clicked.connect(self.acquire_image)

        # Hide some panels if not used
        self.ui.groupBox_stageXYZ.hide()
        self.ui.groupBox_stageRot.hide()

        # Vibratome UI initialization
        self.ui.doubleSpinBox_vibratomeSliceThicknessMm.valueChanged.connect(self.update_vibratome_parameters)
        self.ui.spinBox_vibratome_nSlices.valueChanged.connect(self.update_vibratome_parameters)
        self.ui.actionShow_advanded_vibratome_parameters.changed.connect(self.update_vibratome_parameters)
        self.ui.checkBox_vibratome_firstCutAtCurrentHeight.clicked.connect(self.update_vibratome_parameters)
        self.ui.progressBar_vibratome_cutting.setValue(0)

        # Setup vibratome settings
        self.ui.doubleSpinBox_vibratomeCuttingLengthMm.setValue(
            self.config_manager.config['vibratome']['cutting_distance'])
        self.ui.doubleSpinBox_vibratomeFeedingRate_mms.setValue(self.config_manager.config['vibratome']['feeding_rate'])
        self.ui.doubleSpinBox_vibratomeSliceThicknessMm.setValue(
            self.config_manager.config['vibratome']['slice_thickness'])
        self.ui.doubleSpinBox_vibratomeBladeFrequencyHz.setValue(
            self.config_manager.config['vibratome']['cutting_frequency'])
        self.ui.doubleSpinBox_vibratomeBladeAmplitudeV.setValue(
            self.config_manager.config['vibratome']['cutting_amplitude'])
        self.ui.actionSet_current_position_as_vibratome_position.triggered.connect(self.update_vibratome_position)
        self.update_vibratome_parameters()

    def init_viewer(self):
        # Initialize the image viewer
        self.glayout = pg.GraphicsLayoutWidget()
        self.ui.groupBox_viewer.layout().addWidget(self.glayout)

        # Create the widget
        self.viewer = self.glayout.addPlot()
        self.viewer.setLabel("left", "Y", "m")
        self.viewer.setLabel("bottom", "X", "m")
        self.viewer.setAspectLocked(lock=True, ratio=1)
        self.imageItem = pg.ImageItem(image=self.image, border="y")
        self.viewer.addItem(self.imageItem)

        # Add a color bar
        self.colorbarItem = pg.ColorBarItem(colorMap="magma", limits=(0, 1), rounding=0.001)
        self.colorbarItem.setImageItem(self.imageItem, insert_in=self.viewer)

    def update_status_and_log(self, msg, timeout: int = 5000):
        logging.info(msg)
        self.ui.statusbar.showMessage(msg, timeout=timeout)

    def update_image(self, image):
        self.image = image

    def update_view(self, img: np.ndarray = None):
        # Simulate an image
        if img is None:
            img = np.random.rand(100, 100)
        self.imageItem.setImage(img)

    def update_position(self, x, y, z):
        self.ui.lcdNumber_x_mm.display(x)
        self.ui.lcdNumber_y_mm.display(y)
        self.ui.lcdNumber_z_mm.display(z)
        self.ui.lineEdit_vibratome_currentZ_mm.setText(f"{z:.3f}")
        if self.ui.checkBox_vibratome_firstCutAtCurrentHeight.isChecked():
            self.update_vibratome_parameters()

    def update_position_rot(self, rot_top, rot_bottom, z):
        self.ui.lcdNumber_rotTop.display(rot_top)
        self.ui.lcdNumber_rotBottom.display(rot_bottom)

    def update_z_jogstep(self):
        jog_step = self.ui.doubleSpinBox_z_jogstep_mm.value()
        self.ui.doubleSpinBox_vibratome_zStep_mm.setValue(jog_step)

    def update_z_jogstep_vibratome(self):
        jog_step = self.ui.doubleSpinBox_vibratome_zStep_mm.value()
        self.ui.doubleSpinBox_z_jogstep_mm.setValue(jog_step)

    def update_vibratome_parameters(self):
        """Update the vibratome parameters"""
        # Get the number of slices and the slice thickness
        current_z = float(self.ui.lineEdit_vibratome_currentZ_mm.text())
        previous_z = float(self.ui.lineEdit_vibratome_previousCut_mm.text())
        n_slices = self.ui.spinBox_vibratome_nSlices.value()
        slice_thickness = self.ui.doubleSpinBox_vibratomeSliceThicknessMm.value()
        maximum_cutting_height = self.config_manager.config['vibratome']['maximum_cutting_height']
        first_cut_atCurrentZ = self.ui.checkBox_vibratome_firstCutAtCurrentHeight.isChecked()

        # Compute the remaining thickness, nb. of slice remaining, etc.
        if first_cut_atCurrentZ:
            next_z = current_z
        else:
            next_z = previous_z + slice_thickness
        next_thickness = next_z - previous_z
        total_cut_thickness = next_thickness + (n_slices - 1) * slice_thickness
        remaining_thickness = maximum_cutting_height - previous_z
        n_slices_remaining = int(np.floor((remaining_thickness - next_thickness) / slice_thickness)) + 1

        # Update the UI
        self.ui.lineEdit_vibratome_nextCut_mm.setText(f"{next_z:.3f}")
        self.ui.lineEdit_vibratome_nextCuttingDistance_mm.setText(f"{next_thickness:.3f}")
        self.ui.lineEdit_vibratome_nextTotalThickness_mm.setText((f"{total_cut_thickness:.3f}"))
        self.ui.lineEdit_vibratome_remainingThickness_mm.setText((f"{remaining_thickness:.3f}"))
        self.ui.lineEdit_vibratome_nSlicesRemaining.setText(str(n_slices_remaining))
        self.ui.spinBox_vibratome_nSlices.setMaximum(n_slices_remaining)
        if self.ui.actionShow_advanded_vibratome_parameters.isChecked():
            self.ui.groupBox_vibratome_advancedParameters.show()
        else:
            self.ui.groupBox_vibratome_advancedParameters.hide()

    def stage_moveto(self):
        # Get the destination
        destination = self.ui.comboBox_stage_XYZ_moveTo.currentText()
        if destination.lower() == "objective":
            x, y = self.config_manager.config["soct-stage-xyz"]["position_objective"]
        elif destination.lower() == "vibratome":
            x, y = self.config_manager.config["soct-stage-xyz"]["position_vibratome"]
        # TODO: make sure the move is done at a safe height
        self.strategy.stage.move_to(x=x, y=y)

    def stage_move_to_vibratome(self):
        x, y = self.config_manager.config["soct-stage-xyz"]["position_vibratome"]
        current_x, current_y = self.strategy.stage.position[0:2]
        self.strategy.stage.move_to(current_x, current_y, z=0.0,
                                    blocking=True)  # TODO: replace to move at a safe height
        self.strategy.stage.move_to(x=x, y=y)

    def update_vibratome_position(self):
        x, y = self.strategy.stage.position[0:2]
        self.config_manager.config["soct-stage-xyz"]["position_vibratome"] = (x, y)
        msg = f"Setting the vibratome position to (x,y) = ({x},{y})"
        logging.info(msg)

    def set_microscope_as_soct(self):
        try:
            from linum_microscopes.microscopes.soct import AgilentVibratome, XYZStage, OCTCamera, SOCTStrategy
        except:
            self.update_status_and_log("The SOCT module is not available.")
            return

        self.update_status_and_log("Setting the microscope as soct.")

        # Initialize the controllers, separate out assignment and object creation to avoid issues with type hinting
        camera = OCTCamera()
        stage = XYZStage(self.config_manager.config)
        vibratome = AgilentVibratome(self.config_manager.config)

        self.camera = camera
        self.stage = stage
        self.vibratome = vibratome

        # Create the strategy
        self.strategy = SOCTStrategy(camera, vibratome, stage)

        # Display the XYZ Stage Control
        self.ui.groupBox_stageXYZ.show()
        self.ui.groupBox_stageRot.hide()

        if hasattr(self, "thread_stagexyz"):
            print("Exiting the thread")
            self.thread_stagexyz.stop()
            del self.thread_stagexyz

        # Connect the stage to the thread
        self.strategy.stage.sig_stage_position.connect(self.update_position)
        self.stage.thread.run()

        # Hide the rotation control
        # self.ui.

    def set_microscope_as_pli(self):
        # self.update_status_and_log("Setting the microscope as PLI.")
        #
        # # Update the controllers display
        # self.ui.groupBox_stageXYZ.show()
        # self.ui.groupBox_stageRot.show()
        #
        # if hasattr(self, "thread_stagexyz"):
        #     print("Exiting thread")
        #     self.thread_stagexyz.stop()
        #     del self.thread_stagexyz
        #
        # self.stage_rot = pdvStage.PLIRotStage()
        # self.thread_stagerot = StageXYZThread(self.stage_rot)
        # self.thread_stagerot.sig_stage_position.connect(self.update_position_rot)
        # self.stage_xyz = pdvStage.PLIXYZStage()
        # self.thread_stagexyz = StageXYZThread(self.stage_xyz)
        # self.thread_stagexyz.sig_stage_position.connect(self.update_position)
        # self.thread_stagerot.start()
        # self.thread_stagexyz.start()

        raise NotImplementedError("The PLI module is not available.")

    def set_microscope_as_vibratome(self):
        try:
            from linum_microscopes.microscopes.soct import AgilentVibratome, XYZStage, VibratomeStrategy
        except:
            self.update_status_and_log("The SOCT module is not available.")
            return
        self.update_status_and_log("Setting the microscope as vibratome.")

        # Update the controllers display
        self.ui.groupBox_stageXYZ.show()
        self.ui.groupBox_stageRot.hide()
        self.ui.pliTab.setEnabled(False)
        self.ui.CameraTab.setEnabled(False)
        self.ui.vibratomeTab.show()
        self.ui.groupBox_viewer.hide()

        # Initialize the controllers
        stage = XYZStage(self.config_manager.config)
        vibratome = AgilentVibratome(self.config_manager.config)

        self.stage = stage
        self.vibratome = vibratome

        # Create the strategy
        self.strategy = VibratomeStrategy(None, vibratome, stage)

        # Create a vibratome controller
        # self.flag_vibratome = False
        # self.vibratome = function_generator_jds6600.Vibratome(self.config['vibratome']['com_port'])
        # self.vibratome = AgilentVibratome(self.config_manager.config)
        self.ui.pushButton_vibratome.clicked.connect(self.start_stop_vibratome)

        # Initialize the values
        self.vibratome_update_frequency()
        self.vibratome_update_amplitude()

        # Connect signals and slots
        self.ui.doubleSpinBox_vibratomeBladeFrequencyHz.valueChanged.connect(self.vibratome_update_frequency)
        self.ui.doubleSpinBox_vibratomeBladeAmplitudeV.valueChanged.connect(self.vibratome_update_amplitude)
        self.ui.pushButton_vibratome_stageGotoVibratome.clicked.connect(self.stage_move_to_vibratome)
        self.ui.pushButton_vibratomeCut.clicked.connect(self.vibratome_cut)

        # Setup the stage
        if hasattr(self, "thread_stagexyz"):
            print("Exiting the thread")
            self.thread_stagexyz.stop()
            del self.thread_stagexyz

        self.strategy.stage.sig_stage_position.connect(self.update_position)
        self.stage.thread.start()

    def start_stop_vibratome(self):
        if self.ui.pushButton_vibratome.isChecked():
            self.update_status_and_log("Starting the vibratome.")
            self.strategy.vibratome.start()
            self.ui.pushButton_vibratome.setText("Stop blade")
            self.ui.pushButton_vibratome.setIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaPlaybackStop))
        else:
            self.update_status_and_log("Stopping the vibratome.")
            self.strategy.vibratome.stop()
            self.ui.pushButton_vibratome.setText("Start blade")
            self.ui.pushButton_vibratome.setIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaPlaybackStart))

    def vibratome_update_frequency(self):
        frequency = self.ui.doubleSpinBox_vibratomeBladeFrequencyHz.value()
        msg = f"Setting blade frequency to {frequency} Hz"
        self.update_status_and_log(msg)
        self.strategy.vibratome.frequency = frequency

    def vibratome_update_amplitude(self):
        amplitude = self.ui.doubleSpinBox_vibratomeBladeAmplitudeV.value()
        msg = f"Setting amplitude to {amplitude} V"
        self.update_status_and_log(msg)
        self.strategy.vibratome.amplitude = amplitude

    def vibratome_cut(self):  # Send this to a separate thread
        self.update_status_and_log("Performing a cut", timeout=0)
        self.update_vibratome_parameters()
        self.vibratome_update_frequency()
        self.vibratome_update_amplitude()
        self.ui.progressBar_vibratome_cutting.setValue(0)

        # Move the sample in front of the vibratome
        position = np.array(self.strategy.stage.position)
        pos_vibratome = np.array(self.config_manager.config['soct-stage-xyz']['position_vibratome'])
        cutting_length_mm = self.ui.doubleSpinBox_vibratomeCuttingLengthMm.value()
        pos_end_cut = [pos_vibratome[0], pos_vibratome[1] - cutting_length_mm]
        print(pos_end_cut)
        margin = 2.0  # mm
        if not np.allclose(position[0:2], self.config_manager.config['soct-stage-xyz']['position_vibratome']):
            current_x, current_y = position[0:2]
            x, y = pos_vibratome[0:2]
            self.strategy.stage.move_to(current_x, current_y, z=0.0, blocking=True)  # TODO: move to safe height
            self.strategy.stage.move_to(x=x, y=y, blocking=True)

        # Get the slicing information
        next_cut_z = float(self.ui.lineEdit_vibratome_nextCut_mm.text())
        n_slices = self.ui.spinBox_vibratome_nSlices.value()
        thickness = self.ui.doubleSpinBox_vibratomeSliceThicknessMm.value()
        pause_between_slice = self.ui.checkBox_vibratome_pauseBetweenSlice.isChecked()
        feeding_rate_mms = self.ui.doubleSpinBox_vibratomeFeedingRate_mms.value()
        cutting_heights = np.linspace(next_cut_z, next_cut_z + (n_slices - 1) * thickness, n_slices).tolist()

        for i in range(len(cutting_heights)):
            self.ui.progressBar_vibratome_cutting.setValue(i / len(cutting_heights) * 100)
            # Go to the front of the blade
            k = cutting_heights[i]
            position = np.array(self.strategy.stage.position)
            if not np.allclose(position[0:2], pos_vibratome[0:2]):
                current_x, current_y = position[0:2]
                x, y = pos_vibratome[0:2]
                self.strategy.stage.move_to(current_x, current_y, z=0.0, blocking=True)  # TODO: move to safe height
                self.strategy.stage.move_to(x=x, y=y, blocking=True)

            # Move to the next cutting height
            current_x, current_y = self.strategy.stage.position[0:2]
            self.strategy.stage.move_to(current_x, current_y, z=k, blocking=True)
            while not np.allclose(self.strategy.stage.position, [*pos_vibratome, k]):
                time.sleep(0.1)

            # Start the blade
            self.strategy.vibratome.start()
            time.sleep(1.0)

            # Start a move
            self.strategy.stage.speed = feeding_rate_mms * 60
            self.strategy.stage.move_to(x=pos_end_cut[0], y=pos_end_cut[1], blocking=True)
            while not np.allclose(self.strategy.stage.position, [*pos_end_cut, k]):
                time.sleep(0.1)

            # Stop the blade
            self.strategy.vibratome.stop()
            time.sleep(1.0)

            # Update the number of slices
            n_slices_done = int(self.ui.lineEdit_vibratome_nSlicesDone.text())
            self.ui.lineEdit_vibratome_nSlicesDone.setText(str(n_slices_done + 1))

            # Move down
            safe_z = max(self.strategy.stage.position[2] - margin, 0.0)
            # self.thread_stagexyz.move_by(dz=-margin, blocking=True)
            current_x, current_y = self.strategy.stage.position[0:2]
            self.strategy.stage.move_to(current_x, current_y, z=safe_z, blocking=True)

            # Check if we need to pause between slices
            if pause_between_slice and k != cutting_heights[-1]:
                dlg = PauseBetweenCutDialog()
                if dlg.exec():
                    continue
                else:
                    break

        # Post-cut settings
        # TODO: instead of clicking, do it with the APi
        self.ui.progressBar_vibratome_cutting.setValue(100)
        self.ui.lineEdit_vibratome_previousCut_mm.setText(f"{cutting_heights[i]:.3f}")
        self.update_vibratome_parameters()

    def jog_x(self):
        distance = self.ui.doubleSpinBox_xy_jogstep_mm.value()
        self.strategy.stage.move_by(dx=distance, dy=0, dz=0, blocking=False)

    def reverse_jog_x(self):
        distance = self.ui.doubleSpinBox_xy_jogstep_mm.value()
        self.strategy.stage.move_by(dx=-distance, dy=0, dz=0, blocking=False)

    def jog_y(self):
        distance = self.ui.doubleSpinBox_xy_jogstep_mm.value()
        self.strategy.stage.move_by(dx=0, dy=distance, dz=0, blocking=False)

    def reverse_jog_y(self):
        distance = self.ui.doubleSpinBox_xy_jogstep_mm.value()
        self.strategy.stage.move_by(dx=0, dy=-distance, dz=0, blocking=False)

    def jog_z(self):
        distance = self.ui.doubleSpinBox_z_jogstep_mm.value()
        self.strategy.stage.move_by(dx=0, dy=0, dz=distance, blocking=False)

    def reverse_jog_z(self):
        distance = self.ui.doubleSpinBox_z_jogstep_mm.value()
        self.strategy.stage.move_by(dx=0, dy=0, dz=-distance, blocking=False)

    # TODO: Create stage implementation for the rotational stage
    def jog_top_rot(self):
        # angle_top = self.ui.doubleSpinBox_rot_jogstep_deg.value()
        # angle_bottom = 0.0
        # if self.ui.checkBox_linkTopBottomRot.isChecked():
        #     angle_bottom = angle_top
        # self.stage_rot.move_relative(dx=angle_top, dy=angle_bottom, blocking=False)
        raise NotImplementedError("The rotational stage is not implemented.")

    def jog_top_rot_reverse(self):
        # angle_top = -self.ui.doubleSpinBox_rot_jogstep_deg.value()
        # angle_bottom = 0.0
        # if self.ui.checkBox_linkTopBottomRot.isChecked():
        #     angle_bottom = angle_top
        # self.stage_rot.move_relative(dx=angle_top, dy=angle_bottom, blocking=False)
        raise NotImplementedError("The rotational stage is not implemented.")

    def jog_bottom_rot(self):
        # angle_bottom = self.ui.doubleSpinBox_rot_jogstep_deg.value()
        # angle_top = 0
        # if self.ui.checkBox_linkTopBottomRot.isChecked():
        #     angle_top = angle_bottom
        # self.stage_rot.move_relative(dx=angle_top, dy=angle_bottom, blocking=False)
        raise NotImplementedError("The rotational stage is not implemented.")

    def jog_bottom_rot_reverse(self):
        # angle_bottom = -self.ui.doubleSpinBox_rot_jogstep_deg.value()
        # angle_top = 0
        # if self.ui.checkBox_linkTopBottomRot.isChecked():
        #     angle_top = angle_bottom
        # self.stage_rot.move_relative(dx=angle_top, dy=angle_bottom, blocking=False)
        raise NotImplementedError("The rotational stage is not implemented.")

    def homing_xyz(self):
        current_x, current_y = self.strategy.stage.position[0:2]
        self.strategy.stage.move_to(current_x, current_y, z=0, blocking=True)
        self.strategy.stage.move_to(x=0, y=0)
        # self.stage_xyz.homing()

    def homing_rot(self):
        # self.stage_rot.homing()
        raise NotImplementedError("The rotational stage is not implemented.")

    def stop_moves(self):
        if hasattr(self, "stage_xyz") and self.strategy.stage is not None:
            self.stage.add_to_queue("abort", "abort")

    def acquire_image(self):
        self.update_status_and_log("Acquiring an image")
        # img = pcoCamera.acquire_single_image()
        img = np.random.random((100, 100))
        self.update_view(img)
        self.acquisitionStatus = True
        self.timer.start()

    # @property
    # def safe_z(self) -> float: # TODO: implement the safe move height logic.
    #     """Safe height for a move"""
    #     next_cut_z = self.ui.lineEdit_vibratome_nextCut_mm
    #
    #     max(min([self.next_cutting_height - self.slice_thickness, self.focus_height]) - self._safe_move_margin,
    #         0.0)
    #     #z = max()
    #     return 0


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QPixmap("resources/linum-logo.svg"))
    qdarktheme.setup_theme("auto")  # Apply the system's color theme
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
