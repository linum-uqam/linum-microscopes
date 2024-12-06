# This Python file uses the following encoding: utf-8
import sys

import numpy as np
import pyqtgraph as pg
import qdarktheme
from PySide6 import QtCore
from PySide6.QtCore import QThread, Signal
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QPixmap, QActionGroup, QIcon
import logging
from pathlib import Path
import time


#from linum_microscopes.controllers import pcoCamera
from linum_microscopes.controllers import pdvStage
from linum_microscopes.controllers import function_generator_jds6600
from linum_microscopes.config import config

# TODO: put the camera capture in a different thread to avoid freezing the GUI
# TODO: problem with the z range for the PLI
# TODO: add tools to set the min-max range in software for the ocnfig (ex: max height for PLI).
# TODO: disable the software during homing sequence.
# TODO: prepare the hardware when starting the GUI instead of when choosing the device (available device should be a config thing on every system)
# TODO: use numpad/joystick to control the stage

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow

logging.basicConfig(
    format=f"%(levelname)s - %(asctime)s [{Path(__file__).name}:%(lineno)s | %(funcName)s()] %(message)s",
    level=logging.INFO,
    datefmt="%Y-%m-%d %H:%M:%S")

# Tasks
# TODO: deactivate the stage controller if not homed or configured
# TODO: create a separate thread for every hardware component
# FIXME: homing will break the stage polling
# FIXME: the stage seems to go off limits
# TODO: add a message box during homing sequence.
# FIXME: problem with frequent jogs, the GUI freezes


class StageXYZThread(QThread):
    actions = []
    sig_stage_action_done = Signal(str)
    sig_current_action = Signal(str)
    sig_stage_position = Signal(float, float, float)

    def __init__(self, stage, parent=None):
        super().__init__(parent=parent)
        self.stage = stage
        self.stage.homing()
        self._position = None

    def addAction(self, action: str):
        if action == "stage_abort":
            self.actions.clear()
        self.actions.append(action)

    def process_next_action(self):
        if len(self.actions) == 0:
            action = "None"
        else:
            action = self.actions.pop(0)
            self.sig_current_action.emit("Processing: " + action)

        if action == "stage_abort":
            self.stage.stop()

        if action.startswith("moveto_"):
            pattern = re.compile(r"moveto_x(.*)_y(.*)_z(.*)_speed(.*)_blocking_(.*)")
            match = pattern.match(action)
            x_str = match.group(1)
            x = float(x_str) if len(x_str) > 0 else None
            y_str = match.group(2)
            y = float(y_str) if len(y_str) > 0 else None
            z_str = match.group(3)
            z = float(z_str) if len(z_str) > 0 else None
            speed = float(match.group(4))
            blocking = bool(int(match.group(5)))
            self.stage.move(x=x, y=y, z=z, speed=speed, blocking=blocking)

        if action.startswith("moveby_"):
            pattern = re.compile("moveby_x(.*)_y(.*)_z(.*)_speed(.*)_blocking_(.*)")
            match = pattern.match(action)
            dx_str = match.group(1)
            dx = float(dx_str) if len(dx_str) > 0 else None
            dy_str = match.group(2)
            dy = float(dy_str) if len(dy_str) > 0 else None
            dz_str = match.group(3)
            dz = float(dz_str) if len(dz_str) > 0 else None
            speed = float(match.group(4))
            blocking = bool(int(match.group(5)))
            self.stage.move_relative(dx=dx, dy=dy, dz=dz, speed=speed, blocking=blocking)

        # Post action processing
        self._position = self.stage.position
        self.sig_stage_position.emit(*self._position)

    def move_to(self, x: float = None, y: float = None, z: float = None, speed: float = 500, blocking: bool = False):
        assert x is not None or y is not None or z is not None, "At least one of x, y, z or speed must be set"

        if x is None:
            x = ""
        else:
            x = f"{x:.3f}"
        if y is None:
            y = ""
        else:
            y = f"{y:.3f}"
        if z is None:
            z = ""
        else:
            z = f"{z:.3f}"

        # Prepare the action
        action = f"moveto_x{x}_y{y}_z{z}_speed{speed:.3f}_blocking_{str(int(blocking))}"
        self.addAction(action)

    def move_by(self, dx: float = None, dy: float = None, dz: float = None, speed: float = 500, blocking: bool = False):
        assert dx is not None or dy is not None or dz is not None, "At least one of dx, dy, dz or speed must be set"

        # Prepare the action
        if dx is None:
            dx = ""
        else:
            dx = f"{dx:.3f}"
        if dy is None:
            dy = ""
        else:
            dy = f"{dy:.3f}"
        if dz is None:
            dz = ""
        else:
            dz = f"{dz:.3f}"

        action = f"moveby_x{dx}_y{dy}_z{dz}_speed{speed:.3f}_blocking_{str(int(blocking))}"
        self.addAction(action)

    def run(self):
        while not self.isInterruptionRequested():
            self.process_next_action()
            time.sleep(1 / 30)

    def stop(self):
        self.stage.disconnect()
        self.requestInterruption()
        self.wait()

    @property
    def position(self):
        return self._position


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
    def __init__(self, parent=None):
        super().__init__(parent)
        self.config = config
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_ui()
        self.update_image(np.random.rand(100, 100))
        self.init_viewer()
        self.update_view()
        self.stage_xyz = None


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
        #self.ui.actionOpen.setIcon(QPixmap("resources/open.svg"))

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
        self.ui.pushButton_stage_jogXReverse.clicked.connect(self.reverse_jogx)
        self.ui.pushButton_stage_jogY.clicked.connect(self.jog_y)
        self.ui.pushButton_stage_jogYReverse.clicked.connect(self.reverse_jogy)
        self.ui.pushButton_stage_jogZ.clicked.connect(self.jog_z)
        self.ui.pushButton_vibratome_jogZ_up.clicked.connect(self.jog_z)
        self.ui.pushButton_stage_jogZReverse.clicked.connect(self.reverse_jogz)
        self.ui.pushButton_vibratome_jogZ_down.clicked.connect(self.reverse_jogz)
        self.ui.pushButton_stage_moveToHomeXYZ.clicked.connect(self.homing_xyz)
        self.ui.pushButton_stage_stop.clicked.connect(self.stop_moves)
        self.ui.doubleSpinBox_z_jogstep_mm.valueChanged.connect(self.update_z_jogstep)
        self.ui.doubleSpinBox_vibratome_zStep_mm.valueChanged.connect(self.update_z_jogstep_vibratome)

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

        # Vibratome Signal/Slots
        self.ui.spinBox_vibratome_nSlices.valueChanged.connect(self.update_slicing_parameters)

        # Setup vibratome settings
        self.ui.doubleSpinBox_vibratomeCuttingLengthMm.setValue(self.config['vibratome']['cutting_distance'])
        self.ui.doubleSpinBox_vibratomeFeedingRate_mms.setValue(self.config['vibratome']['feeding_rate'])
        self.ui.doubleSpinBox_vibratomeSliceThicknessMm.setValue(self.config['vibratome']['slice_thickness'])
        self.ui.doubleSpinBox_vibratomeBladeFrequencyHz.setValue(self.config['vibratome']['cutting_frequency'])
        self.ui.doubleSpinBox_vibratomeBladeAmplitudeV.setValue(self.config['vibratome']['cutting_amplitude'])
        self.update_slicing_parameters()

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

    def update_status_and_log(self, msg, timeout:int = 5000):
        logging.info(msg)
        self.ui.statusbar.showMessage(msg, timeout=timeout)

    def update_image(self, image):
        self.image = image

    def update_view(self, img: np.ndarray=None):
        # Simulate an image
        if img is None:
            img = np.random.rand(100, 100)
        self.imageItem.setImage(img)

    def update_position(self, x, y, z):
        self.ui.lcdNumber_x_mm.display(x)
        self.ui.lcdNumber_y_mm.display(y)
        self.ui.lcdNumber_z_mm.display(z)
        self.ui.lineEdit_vibratome_cuttingHeight_mm.setText(f"{z:.3f}")

    def update_position_rot(self, rot_top, rot_bottom, z):
        self.ui.lcdNumber_rotTop.display(rot_top)
        self.ui.lcdNumber_rotBottom.display(rot_bottom)

    def update_z_jogstep(self):
        jog_step = self.ui.doubleSpinBox_z_jogstep_mm.value()
        self.ui.doubleSpinBox_vibratome_zStep_mm.setValue(jog_step)

    def update_z_jogstep_vibratome(self):
        jog_step = self.ui.doubleSpinBox_vibratome_zStep_mm.value()
        self.ui.doubleSpinBox_z_jogstep_mm.setValue(jog_step)

    def update_slicing_parameters(self):
        print("Updating the slicing parameters")
        n_slices = self.ui.spinBox_vibratome_nSlices.value()
        slice_thickness = self.ui.doubleSpinBox_vibratomeSliceThicknessMm.value()
        total_thickness = n_slices * slice_thickness
        self.ui.lineEdit_vibratome_totalCuttingDistance_mm.setText(f"{total_thickness:.3f}")

    def set_microscope_as_soct(self):

        self.update_status_and_log("Setting the microscope as soct.")

        # Display the XYZ Stage Control
        self.ui.groupBox_stageXYZ.show()
        self.ui.groupBox_stageRot.hide()

        if hasattr(self, "thread_stagexyz"):
            print("Exiting the thread")
            self.thread_stagexyz.stop()
            del self.thread_stagexyz

        self.stage_xyz = pdvStage.SOCTXYZStage()
        self.thread_stagexyz = StageXYZThread(self.stage_xyz)
        self.thread_stagexyz.sig_stage_position.connect(self.update_position)
        self.thread_stagexyz.start()




        # Hide the rotation control
        #self.ui.

    def set_microscope_as_pli(self):
        self.update_status_and_log("Setting the microscope as PLI.")

        # Update the controllers display
        self.ui.groupBox_stageXYZ.show()
        self.ui.groupBox_stageRot.show()

        if hasattr(self, "thread_stagexyz"):
            print("Exiting thread")
            self.thread_stagexyz.stop()
            del self.thread_stagexyz

        self.stage_rot = pdvStage.PLIRotStage()
        self.thread_stagerot = StageXYZThread(self.stage_rot)
        self.thread_stagerot.sig_stage_position.connect(self.update_position_rot)
        self.stage_xyz = pdvStage.PLIXYZStage()
        self.thread_stagexyz = StageXYZThread(self.stage_xyz)
        self.thread_stagexyz.sig_stage_position.connect(self.update_position)
        self.thread_stagerot.start()
        self.thread_stagexyz.start()


    def set_microscope_as_vibratome(self):
        self.update_status_and_log("Setting the microscope as vibratome.")

        # update the controllers display
        self.ui.groupBox_stageXYZ.show()
        self.ui.groupBox_stageRot.hide()
        self.ui.pliTab.setEnabled(False)
        self.ui.CameraTab.setEnabled(False)
        self.ui.vibratomeTab.show()
        self.ui.groupBox_viewer.hide()

        # Create a vibratome controller
        self.flag_vibratome = False
        self.vibratome = function_generator_jds6600.FunctionGeneratorJDS6600()
        self.vibratome.unarm()
        self.ui.pushButton_vibratome.clicked.connect(self.start_stop_vibratome)

        # Initialize the values
        frequency, unit = self.vibratome.get_frequency()
        amplitude = self.vibratome.get_amplitude() * 2
        self.ui.doubleSpinBox_vibratomeBladeFrequencyHz.setValue(frequency)
        self.ui.doubleSpinBox_vibratomeBladeAmplitudeV.setValue(amplitude)

        # Connect signals and slots
        self.ui.doubleSpinBox_vibratomeBladeFrequencyHz.valueChanged.connect(self.vibratome_update_frequency)
        self.ui.doubleSpinBox_vibratomeBladeAmplitudeV.valueChanged.connect(self.vibratome_update_amplitude)
        self.ui.pushButton_vibratomeArm.clicked.connect(self.arm_vibratome)

        # Setup the stage
        if hasattr(self, "thread_stagexyz"):
            print("Exiting the thread")
            self.thread_stagexyz.stop()
            del self.thread_stagexyz

        self.stage_xyz = pdvStage.SOCTXYZStage()
        self.thread_stagexyz = StageXYZThread(self.stage_xyz)
        self.thread_stagexyz.sig_stage_position.connect(self.update_position)
        self.thread_stagexyz.start()

    def arm_vibratome(self):
        # Get the button state
        isChecked = self.ui.pushButton_vibratomeArm.isChecked()
        if isChecked:
            self.update_status_and_log("Arming the vibratome.")
            self.vibratome.arm()
            self.ui.pushButton_vibratomeArm.setText("Unarm")
            self.ui.pushButton_vibratome.setEnabled(True)
        else:
            self.update_status_and_log("Unarming the vibratome.")
            self.vibratome.unarm()
            self.ui.pushButton_vibratomeArm.setText("Arm")
            if self.ui.pushButton_vibratome.isChecked():
                self.ui.pushButton_vibratome.click()
            self.ui.pushButton_vibratome.setEnabled(False)

    def start_stop_vibratome(self):
        if self.ui.pushButton_vibratome.isChecked():
            self.update_status_and_log("Starting the vibratome.")
            self.vibratome.start_blade()
            self.ui.pushButton_vibratome.setText("Stop blade")
            self.ui.pushButton_vibratome.setIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaPlaybackStop))
        else:
            self.update_status_and_log("Stopping the vibratome.")
            self.vibratome.stop_blade()
            self.ui.pushButton_vibratome.setText("Start blade")
            self.ui.pushButton_vibratome.setIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaPlaybackStart))


        self.update_vibratome_status()

    def vibratome_update_frequency(self):
        frequency = self.ui.doubleSpinBox_vibratomeBladeFrequencyHz.value()
        msg = f"Setting blade frequency to {frequency} Hz"
        self.update_status_and_log(msg)
        self.vibratome.set_frequency(frequency, channel=1)
        self.vibratome.set_frequency(frequency, channel=2)

    def vibratome_update_amplitude(self):
        amplitude = self.ui.doubleSpinBox_vibratomeBladeAmplitudeV.value() / 2
        msg = f"Setting amplitude to {amplitude} V"
        self.update_status_and_log(msg)
        self.vibratome.set_amplitude(amplitude)

    def update_vibratome_status(self):
        if self.flag_vibratome:
            status_msg = "Vibrating"
        else:
            status_msg = "Idle"
        self.ui.pushButton_vibratomeStatus.setText(status_msg)


    def jog_x(self):
        distance = self.ui.doubleSpinBox_xy_jogstep_mm.value()
        self.thread_stagexyz.move_by(dx=distance, blocking=False)

    def reverse_jogx(self):
        distance = self.ui.doubleSpinBox_xy_jogstep_mm.value()
        self.thread_stagexyz.move_by(dx=-distance, blocking=False)

    def jog_y(self):
        distance = self.ui.doubleSpinBox_xy_jogstep_mm.value()
        self.thread_stagexyz.move_by(dy=distance, blocking=False)

    def reverse_jogy(self):
        distance = self.ui.doubleSpinBox_xy_jogstep_mm.value()
        self.thread_stagexyz.move_by(dy=-distance, blocking=False)

    def jog_z(self):
        distance = self.ui.doubleSpinBox_z_jogstep_mm.value()
        self.thread_stagexyz.move_by(dz=distance, blocking=False)

    def reverse_jogz(self):
        distance = self.ui.doubleSpinBox_z_jogstep_mm.value()
        self.thread_stagexyz.move_by(dz=-distance, blocking=False)

    def jog_top_rot(self):
        angle_top = self.ui.doubleSpinBox_rot_jogstep_deg.value()
        angle_bottom = 0.0
        if self.ui.checkBox_linkTopBottomRot.isChecked():
            angle_bottom = angle_top
        self.stage_rot.move_relative(dx=angle_top, dy=angle_bottom, blocking=False)


    def jog_top_rot_reverse(self):
        angle_top = -self.ui.doubleSpinBox_rot_jogstep_deg.value()
        angle_bottom = 0.0
        if self.ui.checkBox_linkTopBottomRot.isChecked():
            angle_bottom = angle_top
        self.stage_rot.move_relative(dx=angle_top, dy=angle_bottom, blocking=False)

    def jog_bottom_rot(self):
        angle_bottom = self.ui.doubleSpinBox_rot_jogstep_deg.value()
        angle_top = 0
        if self.ui.checkBox_linkTopBottomRot.isChecked():
            angle_top = angle_bottom
        self.stage_rot.move_relative(dx=angle_top, dy=angle_bottom, blocking=False)

    def jog_bottom_rot_reverse(self):
        angle_bottom = -self.ui.doubleSpinBox_rot_jogstep_deg.value()
        angle_top = 0
        if self.ui.checkBox_linkTopBottomRot.isChecked():
            angle_top = angle_bottom
        self.stage_rot.move_relative(dx=angle_top, dy=angle_bottom, blocking=False)

    def homing_xyz(self):
        self.stage_xyz.homing()

    def homing_rot(self):
        self.stage_rot.homing()

    def stop_moves(self):
        if hasattr(self, "stage_xyz") and self.stage_xyz is not None:
            self.thread_stagexyz.addAction("stage_abort")
        if hasattr(self, "stage_rot") and self.stage_rot is not None:
            self.stage_rot.stop()

    def acquire_image(self):
        self.update_status_and_log("Acquiring an image")
        #img = pcoCamera.acquire_single_image()
        img = np.random.random((100,100))
        self.update_view(img)
        self.acquisitionStatus = True
        self.timer.start()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QPixmap("resources/linum-logo.svg"))
    qdarktheme.setup_theme("auto")  # Apply the system's color theme
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
