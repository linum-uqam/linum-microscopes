# This Python file uses the following encoding: utf-8
import sys

import numpy as np
import pyqtgraph as pg
import qdarktheme
from PySide6 import QtCore
from PySide6.QtCore import QThread, Signal
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QPixmap, QActionGroup
import logging
from pathlib import Path
import time


from linum_microscopes.controllers import pcoCamera
from linum_microscopes.controllers import pdvStage

# TODO: put the camera capture in a different thread to avoid freezing the GUI
# TODO: problem with the z range for the PLI
# TODO: add tools to set the min-max range in software for the ocnfig (ex: max height for PLI).

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

        # AVAILABLE_MOVEBY_ACTIONS = ["stage_x_moveby", "stage_y_moveby", "stage_z_moveby"]
        # for i, moveby_action in enumerate(AVAILABLE_MOVEBY_ACTIONS):
        #     distance = [0.0] * 3
        #     if action.startswith(moveby_action):
        #         pattern = re.compile(rf"{moveby_action} \((.*) mm\)")
        #         match = pattern.match(action)
        #         distance[i] = float(match.group(1))
        #
        #         if action.startswith("stage_x"):
        #             response = sbh.stage_xy.move_x_by(distance[0])
        #         elif action.startswith("stage_y"):
        #             response = sbh.stage_xy.move_y_by(distance[1])
        #         elif action.startswith("stage_z"):
        #             response = sbh.stage_z.move_by(distance[2])
        #
        #         if response == -1:
        #             self.display_warning(f"Move by {distance[i]} mm failed")
        #         break
        #
        # if action == "stage_home_all":
        #     sbh.stage_z.home()
        #     sbh.stage_xy.move_to_home()
        # elif action == "stage_home_z":
        #     sbh.stage_z.home()
        # elif action == "stage_home_x":
        #     sbh.stage_xy.home_x()
        # elif action == "stage_home_y":
        #     sbh.stage_xy.home_y()
        # elif action == "stage_moveto_agarose_center":
        #     sbh.move_xy_to(sbh.agarose_center_position)
        # elif action == "stage_moveto_mosaic_center":
        #     sbh.move_xy_to(sbh.mosaic_center_position)
        # elif action == "stage_moveto_stage_center":
        #     sbh.move_xy_to(sbh.stage_center_position)
        # elif action == "stage_moveto_vibratome":
        #     sbh.move_xy_to(sbh.cutting_position_xy)
        # elif action == "stage_moveto_focus_z":
        #     sbh.move_z_to(sbh.focus_height)
        # elif action == "stage_moveto_safe_z":
        #     sbh.move_z_to(sbh.safe_moving_height)
        # elif action == "stage_moveto_nextCuttingHeight":  # TODO: test the move to next cutting height action
        #     sbh.move_z_to(sbh.next_cutting_height)
        # elif action.startswith("vibratome_start"):
        #     # Get the vibratome frequency
        #     pattern = re.compile(r"vibratome_start_freq_(\d+)")
        #     match = pattern.match(action)
        #     frequency = int(match.group(1))
        #     sbh.vibratome.set_blade_frequency(frequency)
        # elif action == "vibratome_stop":
        #     sbh.vibratome.stop()
        # elif action.startswith("slicer_multicut_thickness"):
        #     pattern = re.compile(r"slicer_multicut_thickness_(\d+.\d+)mm")
        #     match = pattern.match(action)
        #     total_thickness = float(match.group(1))
        #     sbh.cut_multiple_slices(sbh.slice_thickness, total_thickness=total_thickness, auto_accept=True)
        # elif action.startswith("soct_multislice"):
        #     pattern = re.compile(r"soct_multislice_(\d+)_updateROI_(True|False)_performLastCut_(True|False)")
        #     match = pattern.match(action)
        #     n_slices = int(match.group(1))
        #     if match.group(2) == "True":
        #         update_roi = True
        #     else:
        #         update_roi = False
        #     if match.group(3) == "True":
        #         perform_lastCut = True
        #     else:
        #         perform_lastCut = False
        #     sbh.acquire_multiple_mosaics(n_slices, update_roi=update_roi, perform_last_cut=perform_lastCut)
        # elif action.startswith("calibrate_vibratome_z"):
        #     pattern = re.compile(r"calibrate_vibratome_z_(\d+.\d+)")
        #     match = pattern.match(action)
        #     z = float(match.group(1))
        #     sbh.calibrate_vibratome(cutting_height=z, perform_cut=True)
        #
        # elif action.startswith("detect_roi_z"):
        #     pattern = re.compile(r"detect_roi_z_(\d+)")
        #     match = pattern.match(action)
        #     z = int(match.group(1))
        #     sbh.detect_mosaic_roi(z)
        # elif action.startswith("acquire_single_OCT_scan"):
        #     print("Acquiring single OCT scan")
        #     # Update the tiles directory
        #     sbh.acquire_volume()

        # Post action processing
        try:
            self.sig_stage_position.emit(*self.stage.position)
        except:
            print("Unable to process stage position")
        # if action != "None":
        #     self.sig_stage_action_done.emit(action)
        #     self.sig_current_action.emit("")

    def run(self):
        while not self.isInterruptionRequested():
            self.process_next_action()
            time.sleep(1 / 30)

    def stop(self):
         self.stage.disconnect()
         self.requestInterruption()
         self.wait()

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
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

        # Stage XYZ job control
        self.ui.pushButton_stage_jogX.clicked.connect(self.jog_x)
        self.ui.pushButton_stage_jogXReverse.clicked.connect(self.reverse_jogx)
        self.ui.pushButton_stage_jogY.clicked.connect(self.jog_y)
        self.ui.pushButton_stage_jogYReverse.clicked.connect(self.reverse_jogy)
        self.ui.pushButton_stage_jogZ.clicked.connect(self.jog_z)
        self.ui.pushButton_stage_jogZReverse.clicked.connect(self.reverse_jogz)
        self.ui.pushButton_stage_moveToHomeXYZ.clicked.connect(self.homing_xyz)
        self.ui.pushButton_stage_stop.clicked.connect(self.stop_moves)

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

    def update_position_rot(self, rot_top, rot_bottom, z):
        self.ui.lcdNumber_rotTop.display(rot_top)
        self.ui.lcdNumber_rotBottom.display(rot_bottom)

    def set_microscope_as_soct(self):
        logging.info("Setting the microscope as soct.")

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
        logging.info("Setting the microscope as PLI.")

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




    def jog_x(self):
        distance = self.ui.doubleSpinBox_xy_jogstep_mm.value()
        self.stage_xyz.move_relative(dx=distance, blocking=False)

    def reverse_jogx(self):
        distance = self.ui.doubleSpinBox_xy_jogstep_mm.value()
        self.stage_xyz.move_relative(dx=-distance, blocking=False)

    def jog_y(self):
        distance = self.ui.doubleSpinBox_xy_jogstep_mm.value()
        self.stage_xyz.move_relative(dy=distance, blocking=False)

    def reverse_jogy(self):
        distance = self.ui.doubleSpinBox_xy_jogstep_mm.value()
        self.stage_xyz.move_relative(dy=-distance, blocking=False)

    def jog_z(self):
        distance = self.ui.doubleSpinBox_z_jogstep_mm.value()
        self.stage_xyz.move_relative(dz=distance, blocking=False)

    def reverse_jogz(self):
        distance = self.ui.doubleSpinBox_z_jogstep_mm.value()
        self.stage_xyz.move_relative(dz=-distance, blocking=False)

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
            self.stage_xyz.stop()
        if hasattr(self, "stage_rot") and self.stage_rot is not None:
            self.stage_rot.stop()

    def acquire_image(self):
        logging.info("Acquiring an image")
        img = pcoCamera.acquire_single_image()
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
