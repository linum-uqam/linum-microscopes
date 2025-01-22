# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QFormLayout, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QLCDNumber, QLabel, QLayout,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QProgressBar, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QStatusBar, QTabWidget, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 850)
        self.actionDark_mode = QAction(MainWindow)
        self.actionDark_mode.setObjectName(u"actionDark_mode")
        self.actionPLI_Polarized_Light_Imaging = QAction(MainWindow)
        self.actionPLI_Polarized_Light_Imaging.setObjectName(u"actionPLI_Polarized_Light_Imaging")
        self.actionPLI_Polarized_Light_Imaging.setCheckable(True)
        self.actionMUSE_Microscopy_by_UV_surface_excitation = QAction(MainWindow)
        self.actionMUSE_Microscopy_by_UV_surface_excitation.setObjectName(u"actionMUSE_Microscopy_by_UV_surface_excitation")
        self.actionMUSE_Microscopy_by_UV_surface_excitation.setCheckable(True)
        self.actionOCT_Optical_Coherence_Tomography = QAction(MainWindow)
        self.actionOCT_Optical_Coherence_Tomography.setObjectName(u"actionOCT_Optical_Coherence_Tomography")
        self.actionOCT_Optical_Coherence_Tomography.setCheckable(True)
        self.actionS_OCT_Serial_OCT = QAction(MainWindow)
        self.actionS_OCT_Serial_OCT.setObjectName(u"actionS_OCT_Serial_OCT")
        self.actionS_OCT_Serial_OCT.setCheckable(True)
        self.actionOCRT_Optical_Coherence_Refraction_Tomography = QAction(MainWindow)
        self.actionOCRT_Optical_Coherence_Refraction_Tomography.setObjectName(u"actionOCRT_Optical_Coherence_Refraction_Tomography")
        self.actionOCRT_Optical_Coherence_Refraction_Tomography.setCheckable(True)
        self.actionMicroscope_Setup = QAction(MainWindow)
        self.actionMicroscope_Setup.setObjectName(u"actionMicroscope_Setup")
        self.actionVibratome = QAction(MainWindow)
        self.actionVibratome.setObjectName(u"actionVibratome")
        self.actionShow_advanded_vibratome_parameters = QAction(MainWindow)
        self.actionShow_advanded_vibratome_parameters.setObjectName(u"actionShow_advanded_vibratome_parameters")
        self.actionShow_advanded_vibratome_parameters.setCheckable(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMaximumSize(QSize(300, 16777215))
        self.StageTab = QWidget()
        self.StageTab.setObjectName(u"StageTab")
        self.verticalLayout_2 = QVBoxLayout(self.StageTab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox_stageXYZ = QGroupBox(self.StageTab)
        self.groupBox_stageXYZ.setObjectName(u"groupBox_stageXYZ")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_stageXYZ)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout_3.setContentsMargins(3, 3, 3, 3)
        self.groupBox_stageXYZ_position = QGroupBox(self.groupBox_stageXYZ)
        self.groupBox_stageXYZ_position.setObjectName(u"groupBox_stageXYZ_position")
        self.groupBox_stageXYZ_position.setFlat(True)
        self.formLayout_2 = QFormLayout(self.groupBox_stageXYZ_position)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setContentsMargins(9, 9, 9, 9)
        self.label = QLabel(self.groupBox_stageXYZ_position)
        self.label.setObjectName(u"label")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label)

        self.lcdNumber_x_mm = QLCDNumber(self.groupBox_stageXYZ_position)
        self.lcdNumber_x_mm.setObjectName(u"lcdNumber_x_mm")
        self.lcdNumber_x_mm.setEnabled(True)
        self.lcdNumber_x_mm.setFrameShape(QFrame.Shape.StyledPanel)
        self.lcdNumber_x_mm.setFrameShadow(QFrame.Shadow.Raised)
        self.lcdNumber_x_mm.setSmallDecimalPoint(False)
        self.lcdNumber_x_mm.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)
        self.lcdNumber_x_mm.setProperty("value", 0.000000000000000)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.lcdNumber_x_mm)

        self.label_2 = QLabel(self.groupBox_stageXYZ_position)
        self.label_2.setObjectName(u"label_2")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_2)

        self.lcdNumber_y_mm = QLCDNumber(self.groupBox_stageXYZ_position)
        self.lcdNumber_y_mm.setObjectName(u"lcdNumber_y_mm")
        self.lcdNumber_y_mm.setFrameShape(QFrame.Shape.StyledPanel)
        self.lcdNumber_y_mm.setFrameShadow(QFrame.Shadow.Raised)
        self.lcdNumber_y_mm.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.lcdNumber_y_mm)

        self.label_3 = QLabel(self.groupBox_stageXYZ_position)
        self.label_3.setObjectName(u"label_3")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_3)

        self.lcdNumber_z_mm = QLCDNumber(self.groupBox_stageXYZ_position)
        self.lcdNumber_z_mm.setObjectName(u"lcdNumber_z_mm")
        self.lcdNumber_z_mm.setFrameShape(QFrame.Shape.StyledPanel)
        self.lcdNumber_z_mm.setFrameShadow(QFrame.Shadow.Raised)
        self.lcdNumber_z_mm.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.lcdNumber_z_mm)

        self.label_8 = QLabel(self.groupBox_stageXYZ_position)
        self.label_8.setObjectName(u"label_8")

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.label_8)

        self.doubleSpinBox_xy_jogstep_mm = QDoubleSpinBox(self.groupBox_stageXYZ_position)
        self.doubleSpinBox_xy_jogstep_mm.setObjectName(u"doubleSpinBox_xy_jogstep_mm")
        self.doubleSpinBox_xy_jogstep_mm.setDecimals(3)
        self.doubleSpinBox_xy_jogstep_mm.setMaximum(10.000000000000000)
        self.doubleSpinBox_xy_jogstep_mm.setValue(1.000000000000000)

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.doubleSpinBox_xy_jogstep_mm)

        self.label_9 = QLabel(self.groupBox_stageXYZ_position)
        self.label_9.setObjectName(u"label_9")

        self.formLayout_2.setWidget(5, QFormLayout.LabelRole, self.label_9)

        self.doubleSpinBox_z_jogstep_mm = QDoubleSpinBox(self.groupBox_stageXYZ_position)
        self.doubleSpinBox_z_jogstep_mm.setObjectName(u"doubleSpinBox_z_jogstep_mm")
        self.doubleSpinBox_z_jogstep_mm.setDecimals(3)
        self.doubleSpinBox_z_jogstep_mm.setMinimum(0.000000000000000)
        self.doubleSpinBox_z_jogstep_mm.setMaximum(10.000000000000000)
        self.doubleSpinBox_z_jogstep_mm.setValue(1.000000000000000)

        self.formLayout_2.setWidget(5, QFormLayout.FieldRole, self.doubleSpinBox_z_jogstep_mm)


        self.verticalLayout_3.addWidget(self.groupBox_stageXYZ_position)

        self.groupBox_stageXYZ_control = QGroupBox(self.groupBox_stageXYZ)
        self.groupBox_stageXYZ_control.setObjectName(u"groupBox_stageXYZ_control")
        self.groupBox_stageXYZ_control.setFlat(True)
        self.gridLayout_3 = QGridLayout(self.groupBox_stageXYZ_control)
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(9, 9, 9, 9)
        self.pushButton_stage_jogXReverse = QPushButton(self.groupBox_stageXYZ_control)
        self.pushButton_stage_jogXReverse.setObjectName(u"pushButton_stage_jogXReverse")
        icon = QIcon(QIcon.fromTheme(u"go-previous"))
        self.pushButton_stage_jogXReverse.setIcon(icon)

        self.gridLayout_3.addWidget(self.pushButton_stage_jogXReverse, 1, 0, 1, 1)

        self.pushButton_stage_jogZ = QPushButton(self.groupBox_stageXYZ_control)
        self.pushButton_stage_jogZ.setObjectName(u"pushButton_stage_jogZ")
        icon1 = QIcon(QIcon.fromTheme(u"go-up"))
        self.pushButton_stage_jogZ.setIcon(icon1)

        self.gridLayout_3.addWidget(self.pushButton_stage_jogZ, 0, 3, 1, 1)

        self.pushButton_stage_jogX = QPushButton(self.groupBox_stageXYZ_control)
        self.pushButton_stage_jogX.setObjectName(u"pushButton_stage_jogX")
        icon2 = QIcon(QIcon.fromTheme(u"go-next"))
        self.pushButton_stage_jogX.setIcon(icon2)

        self.gridLayout_3.addWidget(self.pushButton_stage_jogX, 1, 3, 1, 1)

        self.pushButton_stage_jogY = QPushButton(self.groupBox_stageXYZ_control)
        self.pushButton_stage_jogY.setObjectName(u"pushButton_stage_jogY")
        self.pushButton_stage_jogY.setIcon(icon1)

        self.gridLayout_3.addWidget(self.pushButton_stage_jogY, 0, 1, 1, 1)

        self.pushButton_stage_jogYReverse = QPushButton(self.groupBox_stageXYZ_control)
        self.pushButton_stage_jogYReverse.setObjectName(u"pushButton_stage_jogYReverse")
        icon3 = QIcon(QIcon.fromTheme(u"go-down"))
        self.pushButton_stage_jogYReverse.setIcon(icon3)

        self.gridLayout_3.addWidget(self.pushButton_stage_jogYReverse, 2, 1, 1, 1)

        self.pushButton_stage_jogZReverse = QPushButton(self.groupBox_stageXYZ_control)
        self.pushButton_stage_jogZReverse.setObjectName(u"pushButton_stage_jogZReverse")
        self.pushButton_stage_jogZReverse.setIcon(icon3)

        self.gridLayout_3.addWidget(self.pushButton_stage_jogZReverse, 2, 3, 1, 1)

        self.pushButton_stage_moveToHomeXYZ = QPushButton(self.groupBox_stageXYZ_control)
        self.pushButton_stage_moveToHomeXYZ.setObjectName(u"pushButton_stage_moveToHomeXYZ")
        icon4 = QIcon(QIcon.fromTheme(u"go-home"))
        self.pushButton_stage_moveToHomeXYZ.setIcon(icon4)

        self.gridLayout_3.addWidget(self.pushButton_stage_moveToHomeXYZ, 0, 0, 1, 1)

        self.label_22 = QLabel(self.groupBox_stageXYZ_control)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_22, 3, 0, 1, 1)

        self.comboBox_stage_XYZ_moveTo = QComboBox(self.groupBox_stageXYZ_control)
        self.comboBox_stage_XYZ_moveTo.addItem("")
        self.comboBox_stage_XYZ_moveTo.addItem("")
        self.comboBox_stage_XYZ_moveTo.setObjectName(u"comboBox_stage_XYZ_moveTo")

        self.gridLayout_3.addWidget(self.comboBox_stage_XYZ_moveTo, 3, 1, 1, 1)

        self.pushButton_stageXYZ_moveTo = QPushButton(self.groupBox_stageXYZ_control)
        self.pushButton_stageXYZ_moveTo.setObjectName(u"pushButton_stageXYZ_moveTo")

        self.gridLayout_3.addWidget(self.pushButton_stageXYZ_moveTo, 3, 3, 1, 1)


        self.verticalLayout_3.addWidget(self.groupBox_stageXYZ_control)


        self.verticalLayout_2.addWidget(self.groupBox_stageXYZ)

        self.groupBox_stageRot = QGroupBox(self.StageTab)
        self.groupBox_stageRot.setObjectName(u"groupBox_stageRot")
        self.groupBox_stageRot.setEnabled(True)
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_stageRot)
        self.verticalLayout_4.setSpacing(1)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.groupBox_stageRot_position = QGroupBox(self.groupBox_stageRot)
        self.groupBox_stageRot_position.setObjectName(u"groupBox_stageRot_position")
        self.groupBox_stageRot_position.setFlat(True)
        self.formLayout = QFormLayout(self.groupBox_stageRot_position)
        self.formLayout.setObjectName(u"formLayout")
        self.lcdNumber_rotBottom = QLCDNumber(self.groupBox_stageRot_position)
        self.lcdNumber_rotBottom.setObjectName(u"lcdNumber_rotBottom")
        self.lcdNumber_rotBottom.setFrameShape(QFrame.Shape.StyledPanel)
        self.lcdNumber_rotBottom.setFrameShadow(QFrame.Shadow.Raised)
        self.lcdNumber_rotBottom.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lcdNumber_rotBottom)

        self.label_bottomRotPosition = QLabel(self.groupBox_stageRot_position)
        self.label_bottomRotPosition.setObjectName(u"label_bottomRotPosition")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_bottomRotPosition)

        self.label_topRotPosition = QLabel(self.groupBox_stageRot_position)
        self.label_topRotPosition.setObjectName(u"label_topRotPosition")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_topRotPosition)

        self.lcdNumber_rotTop = QLCDNumber(self.groupBox_stageRot_position)
        self.lcdNumber_rotTop.setObjectName(u"lcdNumber_rotTop")
        self.lcdNumber_rotTop.setFrameShape(QFrame.Shape.StyledPanel)
        self.lcdNumber_rotTop.setFrameShadow(QFrame.Shadow.Raised)
        self.lcdNumber_rotTop.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lcdNumber_rotTop)


        self.verticalLayout_4.addWidget(self.groupBox_stageRot_position)

        self.groupBox_stageRot_control = QGroupBox(self.groupBox_stageRot)
        self.groupBox_stageRot_control.setObjectName(u"groupBox_stageRot_control")
        self.groupBox_stageRot_control.setFlat(True)
        self.gridLayout = QGridLayout(self.groupBox_stageRot_control)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_pliRot_topJogReverse = QPushButton(self.groupBox_stageRot_control)
        self.pushButton_pliRot_topJogReverse.setObjectName(u"pushButton_pliRot_topJogReverse")
        self.pushButton_pliRot_topJogReverse.setIcon(icon)

        self.gridLayout.addWidget(self.pushButton_pliRot_topJogReverse, 1, 1, 1, 1)

        self.pushButton_pliRot_topJog = QPushButton(self.groupBox_stageRot_control)
        self.pushButton_pliRot_topJog.setObjectName(u"pushButton_pliRot_topJog")
        self.pushButton_pliRot_topJog.setIcon(icon2)

        self.gridLayout.addWidget(self.pushButton_pliRot_topJog, 1, 2, 1, 1)

        self.pushButton_pliRot_bottomJog = QPushButton(self.groupBox_stageRot_control)
        self.pushButton_pliRot_bottomJog.setObjectName(u"pushButton_pliRot_bottomJog")
        icon5 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.GoNext))
        self.pushButton_pliRot_bottomJog.setIcon(icon5)

        self.gridLayout.addWidget(self.pushButton_pliRot_bottomJog, 2, 2, 1, 1)

        self.pushButton_pliRot_home = QPushButton(self.groupBox_stageRot_control)
        self.pushButton_pliRot_home.setObjectName(u"pushButton_pliRot_home")
        icon6 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.GoHome))
        self.pushButton_pliRot_home.setIcon(icon6)

        self.gridLayout.addWidget(self.pushButton_pliRot_home, 0, 1, 1, 1)

        self.pushButton_pliRot_bottomJogReverse = QPushButton(self.groupBox_stageRot_control)
        self.pushButton_pliRot_bottomJogReverse.setObjectName(u"pushButton_pliRot_bottomJogReverse")
        icon7 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.GoPrevious))
        self.pushButton_pliRot_bottomJogReverse.setIcon(icon7)

        self.gridLayout.addWidget(self.pushButton_pliRot_bottomJogReverse, 2, 1, 1, 1)

        self.label_4 = QLabel(self.groupBox_stageRot_control)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)

        self.label_10 = QLabel(self.groupBox_stageRot_control)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 2, 0, 1, 1)

        self.label_6 = QLabel(self.groupBox_stageRot_control)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)

        self.doubleSpinBox_rot_jogstep_deg = QDoubleSpinBox(self.groupBox_stageRot_control)
        self.doubleSpinBox_rot_jogstep_deg.setObjectName(u"doubleSpinBox_rot_jogstep_deg")
        self.doubleSpinBox_rot_jogstep_deg.setValue(5.000000000000000)

        self.gridLayout.addWidget(self.doubleSpinBox_rot_jogstep_deg, 5, 1, 1, 1)

        self.checkBox_linkTopBottomRot = QCheckBox(self.groupBox_stageRot_control)
        self.checkBox_linkTopBottomRot.setObjectName(u"checkBox_linkTopBottomRot")

        self.gridLayout.addWidget(self.checkBox_linkTopBottomRot, 6, 1, 1, 1)


        self.verticalLayout_4.addWidget(self.groupBox_stageRot_control)


        self.verticalLayout_2.addWidget(self.groupBox_stageRot)

        self.pushButton_stage_stop = QPushButton(self.StageTab)
        self.pushButton_stage_stop.setObjectName(u"pushButton_stage_stop")
        icon8 = QIcon(QIcon.fromTheme(u"dialog-warning"))
        self.pushButton_stage_stop.setIcon(icon8)

        self.verticalLayout_2.addWidget(self.pushButton_stage_stop)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.tabWidget.addTab(self.StageTab, "")
        self.CameraTab = QWidget()
        self.CameraTab.setObjectName(u"CameraTab")
        self.verticalLayout_5 = QVBoxLayout(self.CameraTab)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.pushButton_camera_acquire = QPushButton(self.CameraTab)
        self.pushButton_camera_acquire.setObjectName(u"pushButton_camera_acquire")

        self.verticalLayout_5.addWidget(self.pushButton_camera_acquire)

        self.tabWidget.addTab(self.CameraTab, "")
        self.pliTab = QWidget()
        self.pliTab.setObjectName(u"pliTab")
        self.tabWidget.addTab(self.pliTab, "")
        self.vibratomeTab = QWidget()
        self.vibratomeTab.setObjectName(u"vibratomeTab")
        self.verticalLayout_6 = QVBoxLayout(self.vibratomeTab)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.groupBox_vibratomeInfo = QGroupBox(self.vibratomeTab)
        self.groupBox_vibratomeInfo.setObjectName(u"groupBox_vibratomeInfo")
        self.formLayout_4 = QFormLayout(self.groupBox_vibratomeInfo)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.label_20 = QLabel(self.groupBox_vibratomeInfo)
        self.label_20.setObjectName(u"label_20")

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.label_20)

        self.lineEdit_vibratome_currentZ_mm = QLineEdit(self.groupBox_vibratomeInfo)
        self.lineEdit_vibratome_currentZ_mm.setObjectName(u"lineEdit_vibratome_currentZ_mm")
        self.lineEdit_vibratome_currentZ_mm.setEnabled(True)
        self.lineEdit_vibratome_currentZ_mm.setAutoFillBackground(False)
        self.lineEdit_vibratome_currentZ_mm.setReadOnly(True)
        self.lineEdit_vibratome_currentZ_mm.setClearButtonEnabled(False)

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.lineEdit_vibratome_currentZ_mm)

        self.label_18 = QLabel(self.groupBox_vibratomeInfo)
        self.label_18.setObjectName(u"label_18")

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.label_18)

        self.lineEdit_vibratome_previousCut_mm = QLineEdit(self.groupBox_vibratomeInfo)
        self.lineEdit_vibratome_previousCut_mm.setObjectName(u"lineEdit_vibratome_previousCut_mm")
        self.lineEdit_vibratome_previousCut_mm.setEnabled(True)
        self.lineEdit_vibratome_previousCut_mm.setReadOnly(True)

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.lineEdit_vibratome_previousCut_mm)

        self.label_19 = QLabel(self.groupBox_vibratomeInfo)
        self.label_19.setObjectName(u"label_19")

        self.formLayout_4.setWidget(2, QFormLayout.LabelRole, self.label_19)

        self.lineEdit_vibratome_nextCut_mm = QLineEdit(self.groupBox_vibratomeInfo)
        self.lineEdit_vibratome_nextCut_mm.setObjectName(u"lineEdit_vibratome_nextCut_mm")
        self.lineEdit_vibratome_nextCut_mm.setEnabled(True)
        self.lineEdit_vibratome_nextCut_mm.setReadOnly(True)

        self.formLayout_4.setWidget(2, QFormLayout.FieldRole, self.lineEdit_vibratome_nextCut_mm)

        self.label_16 = QLabel(self.groupBox_vibratomeInfo)
        self.label_16.setObjectName(u"label_16")

        self.formLayout_4.setWidget(3, QFormLayout.LabelRole, self.label_16)

        self.lineEdit_vibratome_nextCuttingDistance_mm = QLineEdit(self.groupBox_vibratomeInfo)
        self.lineEdit_vibratome_nextCuttingDistance_mm.setObjectName(u"lineEdit_vibratome_nextCuttingDistance_mm")
        self.lineEdit_vibratome_nextCuttingDistance_mm.setEnabled(True)
        self.lineEdit_vibratome_nextCuttingDistance_mm.setReadOnly(True)

        self.formLayout_4.setWidget(3, QFormLayout.FieldRole, self.lineEdit_vibratome_nextCuttingDistance_mm)

        self.label_25 = QLabel(self.groupBox_vibratomeInfo)
        self.label_25.setObjectName(u"label_25")

        self.formLayout_4.setWidget(4, QFormLayout.LabelRole, self.label_25)

        self.lineEdit_vibratome_nextTotalThickness_mm = QLineEdit(self.groupBox_vibratomeInfo)
        self.lineEdit_vibratome_nextTotalThickness_mm.setObjectName(u"lineEdit_vibratome_nextTotalThickness_mm")
        self.lineEdit_vibratome_nextTotalThickness_mm.setReadOnly(True)

        self.formLayout_4.setWidget(4, QFormLayout.FieldRole, self.lineEdit_vibratome_nextTotalThickness_mm)

        self.label_23 = QLabel(self.groupBox_vibratomeInfo)
        self.label_23.setObjectName(u"label_23")

        self.formLayout_4.setWidget(5, QFormLayout.LabelRole, self.label_23)

        self.lineEdit_vibratome_remainingThickness_mm = QLineEdit(self.groupBox_vibratomeInfo)
        self.lineEdit_vibratome_remainingThickness_mm.setObjectName(u"lineEdit_vibratome_remainingThickness_mm")
        self.lineEdit_vibratome_remainingThickness_mm.setReadOnly(True)

        self.formLayout_4.setWidget(5, QFormLayout.FieldRole, self.lineEdit_vibratome_remainingThickness_mm)

        self.label_24 = QLabel(self.groupBox_vibratomeInfo)
        self.label_24.setObjectName(u"label_24")

        self.formLayout_4.setWidget(6, QFormLayout.LabelRole, self.label_24)

        self.lineEdit_vibratome_nSlicesRemaining = QLineEdit(self.groupBox_vibratomeInfo)
        self.lineEdit_vibratome_nSlicesRemaining.setObjectName(u"lineEdit_vibratome_nSlicesRemaining")
        self.lineEdit_vibratome_nSlicesRemaining.setReadOnly(True)

        self.formLayout_4.setWidget(6, QFormLayout.FieldRole, self.lineEdit_vibratome_nSlicesRemaining)

        self.progressBar_vibratome_cutting = QProgressBar(self.groupBox_vibratomeInfo)
        self.progressBar_vibratome_cutting.setObjectName(u"progressBar_vibratome_cutting")
        self.progressBar_vibratome_cutting.setValue(24)

        self.formLayout_4.setWidget(8, QFormLayout.FieldRole, self.progressBar_vibratome_cutting)

        self.label_5 = QLabel(self.groupBox_vibratomeInfo)
        self.label_5.setObjectName(u"label_5")

        self.formLayout_4.setWidget(8, QFormLayout.LabelRole, self.label_5)

        self.label_27 = QLabel(self.groupBox_vibratomeInfo)
        self.label_27.setObjectName(u"label_27")

        self.formLayout_4.setWidget(7, QFormLayout.LabelRole, self.label_27)

        self.lineEdit_vibratome_nSlicesDone = QLineEdit(self.groupBox_vibratomeInfo)
        self.lineEdit_vibratome_nSlicesDone.setObjectName(u"lineEdit_vibratome_nSlicesDone")
        self.lineEdit_vibratome_nSlicesDone.setReadOnly(True)

        self.formLayout_4.setWidget(7, QFormLayout.FieldRole, self.lineEdit_vibratome_nSlicesDone)


        self.verticalLayout_6.addWidget(self.groupBox_vibratomeInfo)

        self.groupBox_vibratomeParameters = QGroupBox(self.vibratomeTab)
        self.groupBox_vibratomeParameters.setObjectName(u"groupBox_vibratomeParameters")
        self.formLayout_5 = QFormLayout(self.groupBox_vibratomeParameters)
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.label_14 = QLabel(self.groupBox_vibratomeParameters)
        self.label_14.setObjectName(u"label_14")

        self.formLayout_5.setWidget(0, QFormLayout.LabelRole, self.label_14)

        self.doubleSpinBox_vibratomeSliceThicknessMm = QDoubleSpinBox(self.groupBox_vibratomeParameters)
        self.doubleSpinBox_vibratomeSliceThicknessMm.setObjectName(u"doubleSpinBox_vibratomeSliceThicknessMm")
        self.doubleSpinBox_vibratomeSliceThicknessMm.setEnabled(True)
        self.doubleSpinBox_vibratomeSliceThicknessMm.setDecimals(3)

        self.formLayout_5.setWidget(0, QFormLayout.FieldRole, self.doubleSpinBox_vibratomeSliceThicknessMm)

        self.label_15 = QLabel(self.groupBox_vibratomeParameters)
        self.label_15.setObjectName(u"label_15")

        self.formLayout_5.setWidget(1, QFormLayout.LabelRole, self.label_15)

        self.spinBox_vibratome_nSlices = QSpinBox(self.groupBox_vibratomeParameters)
        self.spinBox_vibratome_nSlices.setObjectName(u"spinBox_vibratome_nSlices")
        self.spinBox_vibratome_nSlices.setEnabled(True)
        self.spinBox_vibratome_nSlices.setMinimum(1)
        self.spinBox_vibratome_nSlices.setMaximum(10)

        self.formLayout_5.setWidget(1, QFormLayout.FieldRole, self.spinBox_vibratome_nSlices)

        self.label_21 = QLabel(self.groupBox_vibratomeParameters)
        self.label_21.setObjectName(u"label_21")

        self.formLayout_5.setWidget(2, QFormLayout.LabelRole, self.label_21)

        self.doubleSpinBox_vibratome_zStep_mm = QDoubleSpinBox(self.groupBox_vibratomeParameters)
        self.doubleSpinBox_vibratome_zStep_mm.setObjectName(u"doubleSpinBox_vibratome_zStep_mm")
        self.doubleSpinBox_vibratome_zStep_mm.setEnabled(True)
        self.doubleSpinBox_vibratome_zStep_mm.setDecimals(3)
        self.doubleSpinBox_vibratome_zStep_mm.setValue(1.000000000000000)

        self.formLayout_5.setWidget(2, QFormLayout.FieldRole, self.doubleSpinBox_vibratome_zStep_mm)

        self.label_26 = QLabel(self.groupBox_vibratomeParameters)
        self.label_26.setObjectName(u"label_26")

        self.formLayout_5.setWidget(3, QFormLayout.LabelRole, self.label_26)

        self.checkBox_vibratome_firstCutAtCurrentHeight = QCheckBox(self.groupBox_vibratomeParameters)
        self.checkBox_vibratome_firstCutAtCurrentHeight.setObjectName(u"checkBox_vibratome_firstCutAtCurrentHeight")

        self.formLayout_5.setWidget(3, QFormLayout.FieldRole, self.checkBox_vibratome_firstCutAtCurrentHeight)

        self.label_17 = QLabel(self.groupBox_vibratomeParameters)
        self.label_17.setObjectName(u"label_17")

        self.formLayout_5.setWidget(4, QFormLayout.LabelRole, self.label_17)

        self.checkBox_vibratome_pauseBetweenSlice = QCheckBox(self.groupBox_vibratomeParameters)
        self.checkBox_vibratome_pauseBetweenSlice.setObjectName(u"checkBox_vibratome_pauseBetweenSlice")

        self.formLayout_5.setWidget(4, QFormLayout.FieldRole, self.checkBox_vibratome_pauseBetweenSlice)


        self.verticalLayout_6.addWidget(self.groupBox_vibratomeParameters)

        self.groupBox_vibratome_advancedParameters = QGroupBox(self.vibratomeTab)
        self.groupBox_vibratome_advancedParameters.setObjectName(u"groupBox_vibratome_advancedParameters")
        self.formLayout_3 = QFormLayout(self.groupBox_vibratome_advancedParameters)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.label_7 = QLabel(self.groupBox_vibratome_advancedParameters)
        self.label_7.setObjectName(u"label_7")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_7)

        self.doubleSpinBox_vibratomeBladeFrequencyHz = QDoubleSpinBox(self.groupBox_vibratome_advancedParameters)
        self.doubleSpinBox_vibratomeBladeFrequencyHz.setObjectName(u"doubleSpinBox_vibratomeBladeFrequencyHz")
        self.doubleSpinBox_vibratomeBladeFrequencyHz.setDecimals(0)
        self.doubleSpinBox_vibratomeBladeFrequencyHz.setMaximum(200.000000000000000)

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.doubleSpinBox_vibratomeBladeFrequencyHz)

        self.label_13 = QLabel(self.groupBox_vibratome_advancedParameters)
        self.label_13.setObjectName(u"label_13")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_13)

        self.doubleSpinBox_vibratomeBladeAmplitudeV = QDoubleSpinBox(self.groupBox_vibratome_advancedParameters)
        self.doubleSpinBox_vibratomeBladeAmplitudeV.setObjectName(u"doubleSpinBox_vibratomeBladeAmplitudeV")
        self.doubleSpinBox_vibratomeBladeAmplitudeV.setDecimals(1)
        self.doubleSpinBox_vibratomeBladeAmplitudeV.setMaximum(10.000000000000000)
        self.doubleSpinBox_vibratomeBladeAmplitudeV.setSingleStep(0.100000000000000)

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.doubleSpinBox_vibratomeBladeAmplitudeV)

        self.label_11 = QLabel(self.groupBox_vibratome_advancedParameters)
        self.label_11.setObjectName(u"label_11")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.label_11)

        self.doubleSpinBox_vibratomeCuttingLengthMm = QDoubleSpinBox(self.groupBox_vibratome_advancedParameters)
        self.doubleSpinBox_vibratomeCuttingLengthMm.setObjectName(u"doubleSpinBox_vibratomeCuttingLengthMm")
        self.doubleSpinBox_vibratomeCuttingLengthMm.setEnabled(True)

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.doubleSpinBox_vibratomeCuttingLengthMm)

        self.label_12 = QLabel(self.groupBox_vibratome_advancedParameters)
        self.label_12.setObjectName(u"label_12")

        self.formLayout_3.setWidget(3, QFormLayout.LabelRole, self.label_12)

        self.doubleSpinBox_vibratomeFeedingRate_mms = QDoubleSpinBox(self.groupBox_vibratome_advancedParameters)
        self.doubleSpinBox_vibratomeFeedingRate_mms.setObjectName(u"doubleSpinBox_vibratomeFeedingRate_mms")
        self.doubleSpinBox_vibratomeFeedingRate_mms.setEnabled(True)

        self.formLayout_3.setWidget(3, QFormLayout.FieldRole, self.doubleSpinBox_vibratomeFeedingRate_mms)


        self.verticalLayout_6.addWidget(self.groupBox_vibratome_advancedParameters)

        self.groupBox_vibratomeControls = QGroupBox(self.vibratomeTab)
        self.groupBox_vibratomeControls.setObjectName(u"groupBox_vibratomeControls")
        self.gridLayout_2 = QGridLayout(self.groupBox_vibratomeControls)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pushButton_vibratome_jogZ_down = QPushButton(self.groupBox_vibratomeControls)
        self.pushButton_vibratome_jogZ_down.setObjectName(u"pushButton_vibratome_jogZ_down")
        self.pushButton_vibratome_jogZ_down.setEnabled(True)
        self.pushButton_vibratome_jogZ_down.setIcon(icon3)

        self.gridLayout_2.addWidget(self.pushButton_vibratome_jogZ_down, 4, 0, 1, 1)

        self.pushButton_vibratome_jogZ_up = QPushButton(self.groupBox_vibratomeControls)
        self.pushButton_vibratome_jogZ_up.setObjectName(u"pushButton_vibratome_jogZ_up")
        self.pushButton_vibratome_jogZ_up.setEnabled(True)
        self.pushButton_vibratome_jogZ_up.setIcon(icon1)

        self.gridLayout_2.addWidget(self.pushButton_vibratome_jogZ_up, 3, 0, 1, 1)

        self.pushButton_vibratome_stageGotoVibratome = QPushButton(self.groupBox_vibratomeControls)
        self.pushButton_vibratome_stageGotoVibratome.setObjectName(u"pushButton_vibratome_stageGotoVibratome")
        self.pushButton_vibratome_stageGotoVibratome.setEnabled(True)

        self.gridLayout_2.addWidget(self.pushButton_vibratome_stageGotoVibratome, 2, 0, 1, 1)

        self.pushButton_vibratome = QPushButton(self.groupBox_vibratomeControls)
        self.pushButton_vibratome.setObjectName(u"pushButton_vibratome")
        self.pushButton_vibratome.setEnabled(True)
        icon9 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaPlaybackStart))
        self.pushButton_vibratome.setIcon(icon9)
        self.pushButton_vibratome.setCheckable(True)

        self.gridLayout_2.addWidget(self.pushButton_vibratome, 2, 1, 1, 1)

        self.pushButton_vibratomeCut = QPushButton(self.groupBox_vibratomeControls)
        self.pushButton_vibratomeCut.setObjectName(u"pushButton_vibratomeCut")
        self.pushButton_vibratomeCut.setEnabled(True)

        self.gridLayout_2.addWidget(self.pushButton_vibratomeCut, 3, 1, 1, 1)

        self.pushButton_vibratomeAbort = QPushButton(self.groupBox_vibratomeControls)
        self.pushButton_vibratomeAbort.setObjectName(u"pushButton_vibratomeAbort")
        self.pushButton_vibratomeAbort.setEnabled(False)

        self.gridLayout_2.addWidget(self.pushButton_vibratomeAbort, 4, 1, 1, 1)


        self.verticalLayout_6.addWidget(self.groupBox_vibratomeControls)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_2)

        self.tabWidget.addTab(self.vibratomeTab, "")

        self.horizontalLayout.addWidget(self.tabWidget)

        self.groupBox_viewer = QGroupBox(self.centralwidget)
        self.groupBox_viewer.setObjectName(u"groupBox_viewer")
        self.groupBox_viewer.setEnabled(True)
        self.verticalLayout = QVBoxLayout(self.groupBox_viewer)
        self.verticalLayout.setObjectName(u"verticalLayout")

        self.horizontalLayout.addWidget(self.groupBox_viewer)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuSettings = QMenu(self.menubar)
        self.menuSettings.setObjectName(u"menuSettings")
        self.menuTools = QMenu(self.menubar)
        self.menuTools.setObjectName(u"menuTools")
        self.menuConfiguration = QMenu(self.menubar)
        self.menuConfiguration.setObjectName(u"menuConfiguration")
        self.menuConfiguration.setSeparatorsCollapsible(False)
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuConfiguration.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuSettings.addAction(self.actionShow_advanded_vibratome_parameters)
        self.menuConfiguration.addAction(self.actionS_OCT_Serial_OCT)
        self.menuConfiguration.addAction(self.actionOCT_Optical_Coherence_Tomography)
        self.menuConfiguration.addAction(self.actionMUSE_Microscopy_by_UV_surface_excitation)
        self.menuConfiguration.addAction(self.actionOCRT_Optical_Coherence_Refraction_Tomography)
        self.menuConfiguration.addAction(self.actionPLI_Polarized_Light_Imaging)
        self.menuConfiguration.addAction(self.actionVibratome)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"LINUM Microscopes - GUI", None))
        self.actionDark_mode.setText(QCoreApplication.translate("MainWindow", u"Dark mode", None))
        self.actionPLI_Polarized_Light_Imaging.setText(QCoreApplication.translate("MainWindow", u"PLI - Polarized Light Imaging", None))
        self.actionMUSE_Microscopy_by_UV_surface_excitation.setText(QCoreApplication.translate("MainWindow", u"MUSE - Microscopy by UV surface excitation", None))
        self.actionOCT_Optical_Coherence_Tomography.setText(QCoreApplication.translate("MainWindow", u"OCT - Optical Coherence Tomography", None))
        self.actionS_OCT_Serial_OCT.setText(QCoreApplication.translate("MainWindow", u"S-OCT - Serial OCT", None))
        self.actionOCRT_Optical_Coherence_Refraction_Tomography.setText(QCoreApplication.translate("MainWindow", u"OCRT - Optical Coherence Refraction Tomography", None))
        self.actionMicroscope_Setup.setText(QCoreApplication.translate("MainWindow", u"Microscope Setup", None))
        self.actionVibratome.setText(QCoreApplication.translate("MainWindow", u"Vibratome", None))
        self.actionShow_advanded_vibratome_parameters.setText(QCoreApplication.translate("MainWindow", u"Show advanded vibratome parameters", None))
        self.groupBox_stageXYZ.setTitle(QCoreApplication.translate("MainWindow", u"XYZ Stage", None))
        self.groupBox_stageXYZ_position.setTitle(QCoreApplication.translate("MainWindow", u"Position", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"X (mm)", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Y (mm)", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Z (mm)", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"XY Step (mm)", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Z Step (mm)", None))
        self.groupBox_stageXYZ_control.setTitle(QCoreApplication.translate("MainWindow", u"Control", None))
        self.pushButton_stage_jogXReverse.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.pushButton_stage_jogZ.setText(QCoreApplication.translate("MainWindow", u"Z", None))
        self.pushButton_stage_jogX.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.pushButton_stage_jogY.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.pushButton_stage_jogYReverse.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.pushButton_stage_jogZReverse.setText(QCoreApplication.translate("MainWindow", u"Z", None))
#if QT_CONFIG(statustip)
        self.pushButton_stage_moveToHomeXYZ.setStatusTip(QCoreApplication.translate("MainWindow", u"Homing XYZ", None))
#endif // QT_CONFIG(statustip)
        self.pushButton_stage_moveToHomeXYZ.setText("")
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Move to", None))
        self.comboBox_stage_XYZ_moveTo.setItemText(0, QCoreApplication.translate("MainWindow", u"Objective", None))
        self.comboBox_stage_XYZ_moveTo.setItemText(1, QCoreApplication.translate("MainWindow", u"Vibratome", None))

        self.pushButton_stageXYZ_moveTo.setText(QCoreApplication.translate("MainWindow", u"Go", None))
        self.groupBox_stageRot.setTitle(QCoreApplication.translate("MainWindow", u"Rotation Stage", None))
        self.groupBox_stageRot_position.setTitle(QCoreApplication.translate("MainWindow", u"Position", None))
        self.label_bottomRotPosition.setText(QCoreApplication.translate("MainWindow", u"Bottom (deg)", None))
        self.label_topRotPosition.setText(QCoreApplication.translate("MainWindow", u"Top (deg)", None))
        self.groupBox_stageRot_control.setTitle(QCoreApplication.translate("MainWindow", u"Control", None))
        self.pushButton_pliRot_topJogReverse.setText(QCoreApplication.translate("MainWindow", u"\u03b8", None))
        self.pushButton_pliRot_topJog.setText(QCoreApplication.translate("MainWindow", u"\u03b8", None))
        self.pushButton_pliRot_bottomJog.setText(QCoreApplication.translate("MainWindow", u"\u03c6", None))
        self.pushButton_pliRot_home.setText("")
        self.pushButton_pliRot_bottomJogReverse.setText(QCoreApplication.translate("MainWindow", u"\u03c6", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Top", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Bottom", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Step deg)", None))
        self.checkBox_linkTopBottomRot.setText(QCoreApplication.translate("MainWindow", u"Link top / bot", None))
#if QT_CONFIG(tooltip)
        self.pushButton_stage_stop.setToolTip(QCoreApplication.translate("MainWindow", u"Abort all moves", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_stage_stop.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.StageTab), QCoreApplication.translate("MainWindow", u"Stage", None))
        self.pushButton_camera_acquire.setText(QCoreApplication.translate("MainWindow", u"Acquire", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.CameraTab), QCoreApplication.translate("MainWindow", u"Camera", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.pliTab), QCoreApplication.translate("MainWindow", u"PLI", None))
        self.groupBox_vibratomeInfo.setTitle(QCoreApplication.translate("MainWindow", u"Vibratome Info", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Current Z (mm)", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_vibratome_currentZ_mm.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Current z position of the stage</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_vibratome_currentZ_mm.setText(QCoreApplication.translate("MainWindow", u"0.000", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Previous cut (mm)", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_vibratome_previousCut_mm.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Z height of the previous cut</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_vibratome_previousCut_mm.setText(QCoreApplication.translate("MainWindow", u"0.000", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Next cut (mm)", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_vibratome_nextCut_mm.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Z height of the next cut</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_vibratome_nextCut_mm.setText(QCoreApplication.translate("MainWindow", u"0.000", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Initial thickness (mm)", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_vibratome_nextCuttingDistance_mm.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Cutting thickness (next - previous)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_vibratome_nextCuttingDistance_mm.setText(QCoreApplication.translate("MainWindow", u"0.000", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Total thickness (mm)", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_vibratome_nextTotalThickness_mm.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Thickness for the next automated cutting procedure</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_vibratome_nextTotalThickness_mm.setText(QCoreApplication.translate("MainWindow", u"0.200", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Remaining (mm)", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_vibratome_remainingThickness_mm.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Remaining sample thickness to slice, according to the calibrated maximum cutting height</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_vibratome_remainingThickness_mm.setText(QCoreApplication.translate("MainWindow", u"0.000", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"# slices remaining", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_vibratome_nSlicesRemaining.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Number of slices remaining, computed using the remaining thickness and the configured slice thickness.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_vibratome_nSlicesRemaining.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Cutting progress", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"# slices done", None))
        self.lineEdit_vibratome_nSlicesDone.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.groupBox_vibratomeParameters.setTitle(QCoreApplication.translate("MainWindow", u"Vibratome Parameters", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Slice Thickness (mm)", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Number of slices", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Z Step (mm)", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"First cut at current Z", None))
        self.checkBox_vibratome_firstCutAtCurrentHeight.setText("")
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Pause between slices", None))
        self.checkBox_vibratome_pauseBetweenSlice.setText("")
        self.groupBox_vibratome_advancedParameters.setTitle(QCoreApplication.translate("MainWindow", u"Advanced Vibratome Parameters", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Blade Frequency (Hz)", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Blade amplitude (V)", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Cutting length (mm)", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Feeding rate (mm/s)", None))
        self.groupBox_vibratomeControls.setTitle(QCoreApplication.translate("MainWindow", u"Vibratome Controls", None))
        self.pushButton_vibratome_jogZ_down.setText(QCoreApplication.translate("MainWindow", u"Z", None))
        self.pushButton_vibratome_jogZ_up.setText(QCoreApplication.translate("MainWindow", u"Z", None))
#if QT_CONFIG(tooltip)
        self.pushButton_vibratome_stageGotoVibratome.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Moves the stage to position the sample in front of the vibratome blade</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_vibratome_stageGotoVibratome.setText(QCoreApplication.translate("MainWindow", u"Go to vibratome", None))
        self.pushButton_vibratome.setText(QCoreApplication.translate("MainWindow", u"Start blade", None))
        self.pushButton_vibratomeCut.setText(QCoreApplication.translate("MainWindow", u"Cut", None))
        self.pushButton_vibratomeAbort.setText(QCoreApplication.translate("MainWindow", u"Abort", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.vibratomeTab), QCoreApplication.translate("MainWindow", u"Vibratome", None))
        self.groupBox_viewer.setTitle(QCoreApplication.translate("MainWindow", u"Viewer", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.menuSettings.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.menuTools.setTitle(QCoreApplication.translate("MainWindow", u"Tools", None))
        self.menuConfiguration.setTitle(QCoreApplication.translate("MainWindow", u"Configuration", None))
    # retranslateUi

