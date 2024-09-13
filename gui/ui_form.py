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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDoubleSpinBox, QFormLayout,
    QFrame, QGridLayout, QGroupBox, QHBoxLayout,
    QLCDNumber, QLabel, QLayout, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QTabWidget, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 787)
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

        self.label_8 = QLabel(self.groupBox_stageXYZ_control)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_3.addWidget(self.label_8, 4, 0, 1, 1)

        self.label_9 = QLabel(self.groupBox_stageXYZ_control)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_3.addWidget(self.label_9, 5, 0, 1, 1)

        self.doubleSpinBox_xy_jogstep_mm = QDoubleSpinBox(self.groupBox_stageXYZ_control)
        self.doubleSpinBox_xy_jogstep_mm.setObjectName(u"doubleSpinBox_xy_jogstep_mm")
        self.doubleSpinBox_xy_jogstep_mm.setDecimals(3)
        self.doubleSpinBox_xy_jogstep_mm.setMaximum(10.000000000000000)
        self.doubleSpinBox_xy_jogstep_mm.setValue(1.000000000000000)

        self.gridLayout_3.addWidget(self.doubleSpinBox_xy_jogstep_mm, 4, 1, 1, 1)

        self.doubleSpinBox_z_jogstep_mm = QDoubleSpinBox(self.groupBox_stageXYZ_control)
        self.doubleSpinBox_z_jogstep_mm.setObjectName(u"doubleSpinBox_z_jogstep_mm")
        self.doubleSpinBox_z_jogstep_mm.setDecimals(3)
        self.doubleSpinBox_z_jogstep_mm.setMinimum(0.000000000000000)
        self.doubleSpinBox_z_jogstep_mm.setMaximum(10.000000000000000)
        self.doubleSpinBox_z_jogstep_mm.setValue(1.000000000000000)

        self.gridLayout_3.addWidget(self.doubleSpinBox_z_jogstep_mm, 5, 1, 1, 1)


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
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
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
        self.menuSettings.addAction(self.actionDark_mode)
        self.menuConfiguration.addAction(self.actionS_OCT_Serial_OCT)
        self.menuConfiguration.addAction(self.actionOCT_Optical_Coherence_Tomography)
        self.menuConfiguration.addAction(self.actionMUSE_Microscopy_by_UV_surface_excitation)
        self.menuConfiguration.addAction(self.actionOCRT_Optical_Coherence_Refraction_Tomography)
        self.menuConfiguration.addAction(self.actionPLI_Polarized_Light_Imaging)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


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
        self.groupBox_stageXYZ.setTitle(QCoreApplication.translate("MainWindow", u"XYZ Stage", None))
        self.groupBox_stageXYZ_position.setTitle(QCoreApplication.translate("MainWindow", u"Position", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"X (mm)", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Y (mm)", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Z (mm)", None))
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
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"XY Step (mm)", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Z Step (mm)", None))
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
        self.groupBox_viewer.setTitle(QCoreApplication.translate("MainWindow", u"Viewer", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.menuSettings.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.menuTools.setTitle(QCoreApplication.translate("MainWindow", u"Tools", None))
        self.menuConfiguration.setTitle(QCoreApplication.translate("MainWindow", u"Configuration", None))
    # retranslateUi

