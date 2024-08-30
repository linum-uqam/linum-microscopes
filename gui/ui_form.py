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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFormLayout, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QLCDNumber,
    QLabel, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QTabWidget, QVBoxLayout, QWidget)

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
        self.groupBox_6 = QGroupBox(self.StageTab)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.gridLayout = QGridLayout(self.groupBox_6)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lcdNumber_2 = QLCDNumber(self.groupBox_6)
        self.lcdNumber_2.setObjectName(u"lcdNumber_2")

        self.gridLayout.addWidget(self.lcdNumber_2, 1, 1, 1, 1)

        self.lcdNumber_5 = QLCDNumber(self.groupBox_6)
        self.lcdNumber_5.setObjectName(u"lcdNumber_5")

        self.gridLayout.addWidget(self.lcdNumber_5, 4, 1, 1, 1)

        self.checkBox = QCheckBox(self.groupBox_6)
        self.checkBox.setObjectName(u"checkBox")

        self.gridLayout.addWidget(self.checkBox, 5, 0, 1, 1)

        self.label_5 = QLabel(self.groupBox_6)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)

        self.label_2 = QLabel(self.groupBox_6)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_3 = QLabel(self.groupBox_6)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.lcdNumber = QLCDNumber(self.groupBox_6)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setEnabled(True)
        self.lcdNumber.setFrameShape(QFrame.Box)
        self.lcdNumber.setFrameShadow(QFrame.Raised)
        self.lcdNumber.setSmallDecimalPoint(False)
        self.lcdNumber.setSegmentStyle(QLCDNumber.Filled)
        self.lcdNumber.setProperty("value", 0.000000000000000)

        self.gridLayout.addWidget(self.lcdNumber, 0, 1, 1, 1)

        self.label = QLabel(self.groupBox_6)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.lcdNumber_3 = QLCDNumber(self.groupBox_6)
        self.lcdNumber_3.setObjectName(u"lcdNumber_3")

        self.gridLayout.addWidget(self.lcdNumber_3, 2, 1, 1, 1)

        self.lcdNumber_4 = QLCDNumber(self.groupBox_6)
        self.lcdNumber_4.setObjectName(u"lcdNumber_4")

        self.gridLayout.addWidget(self.lcdNumber_4, 3, 1, 1, 1)

        self.label_4 = QLabel(self.groupBox_6)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.groupBox_6)

        self.groupBox_3 = QGroupBox(self.StageTab)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_2 = QGridLayout(self.groupBox_3)
        self.gridLayout_2.setSpacing(1)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pushButton_16 = QPushButton(self.groupBox_3)
        self.pushButton_16.setObjectName(u"pushButton_16")

        self.gridLayout_2.addWidget(self.pushButton_16, 0, 1, 1, 1)

        self.pushButton_pliRot_topJogReverse = QPushButton(self.groupBox_3)
        self.pushButton_pliRot_topJogReverse.setObjectName(u"pushButton_pliRot_topJogReverse")
        icon = QIcon(QIcon.fromTheme(u"go-previous"))
        self.pushButton_pliRot_topJogReverse.setIcon(icon)

        self.gridLayout_2.addWidget(self.pushButton_pliRot_topJogReverse, 0, 0, 1, 1)

        self.pushButton_pliRot_topJog = QPushButton(self.groupBox_3)
        self.pushButton_pliRot_topJog.setObjectName(u"pushButton_pliRot_topJog")
        icon1 = QIcon(QIcon.fromTheme(u"go-next"))
        self.pushButton_pliRot_topJog.setIcon(icon1)

        self.gridLayout_2.addWidget(self.pushButton_pliRot_topJog, 0, 2, 1, 1)


        self.verticalLayout_2.addWidget(self.groupBox_3)

        self.groupBox_4 = QGroupBox(self.StageTab)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_3 = QGridLayout(self.groupBox_4)
        self.gridLayout_3.setSpacing(1)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.pushButton_10 = QPushButton(self.groupBox_4)
        self.pushButton_10.setObjectName(u"pushButton_10")

        self.gridLayout_3.addWidget(self.pushButton_10, 0, 2, 1, 1)

        self.pushButton_ = QPushButton(self.groupBox_4)
        self.pushButton_.setObjectName(u"pushButton_")

        self.gridLayout_3.addWidget(self.pushButton_, 0, 0, 1, 1)

        self.pushButton_15 = QPushButton(self.groupBox_4)
        self.pushButton_15.setObjectName(u"pushButton_15")

        self.gridLayout_3.addWidget(self.pushButton_15, 0, 1, 1, 1)


        self.verticalLayout_2.addWidget(self.groupBox_4)

        self.groupBox_xyzStageControls = QGroupBox(self.StageTab)
        self.groupBox_xyzStageControls.setObjectName(u"groupBox_xyzStageControls")
        self.gridLayout_4 = QGridLayout(self.groupBox_xyzStageControls)
        self.gridLayout_4.setSpacing(1)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(12, 12, 12, 12)
        self.pushButton_stage_jogXReverse = QPushButton(self.groupBox_xyzStageControls)
        self.pushButton_stage_jogXReverse.setObjectName(u"pushButton_stage_jogXReverse")
        self.pushButton_stage_jogXReverse.setIcon(icon)

        self.gridLayout_4.addWidget(self.pushButton_stage_jogXReverse, 2, 0, 1, 1)

        self.pushButton_stage_moveToHomeXYZ = QPushButton(self.groupBox_xyzStageControls)
        self.pushButton_stage_moveToHomeXYZ.setObjectName(u"pushButton_stage_moveToHomeXYZ")
        icon2 = QIcon(QIcon.fromTheme(u"go-home"))
        self.pushButton_stage_moveToHomeXYZ.setIcon(icon2)

        self.gridLayout_4.addWidget(self.pushButton_stage_moveToHomeXYZ, 3, 0, 1, 1)

        self.pushButton_stage_moveToHomeY = QPushButton(self.groupBox_xyzStageControls)
        self.pushButton_stage_moveToHomeY.setObjectName(u"pushButton_stage_moveToHomeY")
        self.pushButton_stage_moveToHomeY.setIcon(icon2)

        self.gridLayout_4.addWidget(self.pushButton_stage_moveToHomeY, 1, 2, 1, 1)

        self.pushButton_stage_jogZReverse = QPushButton(self.groupBox_xyzStageControls)
        self.pushButton_stage_jogZReverse.setObjectName(u"pushButton_stage_jogZReverse")
        icon3 = QIcon(QIcon.fromTheme(u"go-down"))
        self.pushButton_stage_jogZReverse.setIcon(icon3)

        self.gridLayout_4.addWidget(self.pushButton_stage_jogZReverse, 3, 3, 1, 1)

        self.pushButton_stage_jogZ = QPushButton(self.groupBox_xyzStageControls)
        self.pushButton_stage_jogZ.setObjectName(u"pushButton_stage_jogZ")
        icon4 = QIcon(QIcon.fromTheme(u"go-up"))
        self.pushButton_stage_jogZ.setIcon(icon4)

        self.gridLayout_4.addWidget(self.pushButton_stage_jogZ, 1, 3, 1, 1)

        self.pushButton_stage_moveToHomeX = QPushButton(self.groupBox_xyzStageControls)
        self.pushButton_stage_moveToHomeX.setObjectName(u"pushButton_stage_moveToHomeX")
        self.pushButton_stage_moveToHomeX.setIcon(icon2)

        self.gridLayout_4.addWidget(self.pushButton_stage_moveToHomeX, 1, 0, 1, 1)

        self.pushButton_stage_jogY = QPushButton(self.groupBox_xyzStageControls)
        self.pushButton_stage_jogY.setObjectName(u"pushButton_stage_jogY")
        self.pushButton_stage_jogY.setIcon(icon4)

        self.gridLayout_4.addWidget(self.pushButton_stage_jogY, 1, 1, 1, 1)

        self.pushButton_stage_jogYReverse = QPushButton(self.groupBox_xyzStageControls)
        self.pushButton_stage_jogYReverse.setObjectName(u"pushButton_stage_jogYReverse")
        self.pushButton_stage_jogYReverse.setIcon(icon3)

        self.gridLayout_4.addWidget(self.pushButton_stage_jogYReverse, 3, 1, 1, 1)

        self.pushButton_stage_moveToHomeZ = QPushButton(self.groupBox_xyzStageControls)
        self.pushButton_stage_moveToHomeZ.setObjectName(u"pushButton_stage_moveToHomeZ")
        self.pushButton_stage_moveToHomeZ.setIcon(icon2)

        self.gridLayout_4.addWidget(self.pushButton_stage_moveToHomeZ, 3, 2, 1, 1)

        self.pushButton_stage_jogX = QPushButton(self.groupBox_xyzStageControls)
        self.pushButton_stage_jogX.setObjectName(u"pushButton_stage_jogX")
        self.pushButton_stage_jogX.setIcon(icon1)

        self.gridLayout_4.addWidget(self.pushButton_stage_jogX, 2, 2, 1, 1)


        self.verticalLayout_2.addWidget(self.groupBox_xyzStageControls)

        self.groupBox_7 = QGroupBox(self.StageTab)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.formLayout = QFormLayout(self.groupBox_7)
        self.formLayout.setObjectName(u"formLayout")
        self.label_6 = QLabel(self.groupBox_7)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_6)

        self.lineEdit_6 = QLineEdit(self.groupBox_7)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit_6)

        self.label_8 = QLabel(self.groupBox_7)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_8)

        self.lineEdit_8 = QLineEdit(self.groupBox_7)
        self.lineEdit_8.setObjectName(u"lineEdit_8")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit_8)

        self.label_9 = QLabel(self.groupBox_7)
        self.label_9.setObjectName(u"label_9")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_9)

        self.lineEdit_9 = QLineEdit(self.groupBox_7)
        self.lineEdit_9.setObjectName(u"lineEdit_9")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineEdit_9)


        self.verticalLayout_2.addWidget(self.groupBox_7)

        self.pushButton_stage_abort = QPushButton(self.StageTab)
        self.pushButton_stage_abort.setObjectName(u"pushButton_stage_abort")
        icon5 = QIcon(QIcon.fromTheme(u"dialog-warning"))
        self.pushButton_stage_abort.setIcon(icon5)

        self.verticalLayout_2.addWidget(self.pushButton_stage_abort)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.tabWidget.addTab(self.StageTab, "")
        self.CameraTab = QWidget()
        self.CameraTab.setObjectName(u"CameraTab")
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
        self.menubar.setGeometry(QRect(0, 0, 800, 37))
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
        QWidget.setTabOrder(self.checkBox, self.pushButton_pliRot_topJogReverse)
        QWidget.setTabOrder(self.pushButton_pliRot_topJogReverse, self.pushButton_16)
        QWidget.setTabOrder(self.pushButton_16, self.pushButton_pliRot_topJog)
        QWidget.setTabOrder(self.pushButton_pliRot_topJog, self.pushButton_)
        QWidget.setTabOrder(self.pushButton_, self.pushButton_15)
        QWidget.setTabOrder(self.pushButton_15, self.pushButton_10)
        QWidget.setTabOrder(self.pushButton_10, self.pushButton_stage_moveToHomeX)
        QWidget.setTabOrder(self.pushButton_stage_moveToHomeX, self.pushButton_stage_jogY)
        QWidget.setTabOrder(self.pushButton_stage_jogY, self.pushButton_stage_moveToHomeY)
        QWidget.setTabOrder(self.pushButton_stage_moveToHomeY, self.pushButton_stage_jogZ)
        QWidget.setTabOrder(self.pushButton_stage_jogZ, self.pushButton_stage_jogXReverse)
        QWidget.setTabOrder(self.pushButton_stage_jogXReverse, self.pushButton_stage_jogX)
        QWidget.setTabOrder(self.pushButton_stage_jogX, self.pushButton_stage_moveToHomeXYZ)
        QWidget.setTabOrder(self.pushButton_stage_moveToHomeXYZ, self.pushButton_stage_jogYReverse)
        QWidget.setTabOrder(self.pushButton_stage_jogYReverse, self.pushButton_stage_moveToHomeZ)
        QWidget.setTabOrder(self.pushButton_stage_moveToHomeZ, self.pushButton_stage_jogZReverse)
        QWidget.setTabOrder(self.pushButton_stage_jogZReverse, self.lineEdit_6)
        QWidget.setTabOrder(self.lineEdit_6, self.lineEdit_8)
        QWidget.setTabOrder(self.lineEdit_8, self.lineEdit_9)
        QWidget.setTabOrder(self.lineEdit_9, self.pushButton_stage_abort)
        QWidget.setTabOrder(self.pushButton_stage_abort, self.tabWidget)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuConfiguration.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuSettings.addAction(self.actionDark_mode)
        self.menuConfiguration.addAction(self.actionMUSE_Microscopy_by_UV_surface_excitation)
        self.menuConfiguration.addAction(self.actionOCT_Optical_Coherence_Tomography)
        self.menuConfiguration.addAction(self.actionOCRT_Optical_Coherence_Refraction_Tomography)
        self.menuConfiguration.addAction(self.actionPLI_Polarized_Light_Imaging)
        self.menuConfiguration.addAction(self.actionS_OCT_Serial_OCT)

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
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Position", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Link top / bottom", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"BottomRot (deg)", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Y (mm)", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Z (mm)", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"X (mm)", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"TopRot (deg)", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Top Rotation", None))
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"H", None))
        self.pushButton_pliRot_topJogReverse.setText(QCoreApplication.translate("MainWindow", u"\u03b8", None))
        self.pushButton_pliRot_topJog.setText(QCoreApplication.translate("MainWindow", u"\u03b8", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Bottom Rotation", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"+Rot", None))
        self.pushButton_.setText(QCoreApplication.translate("MainWindow", u"-Rot", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"H", None))
        self.groupBox_xyzStageControls.setTitle(QCoreApplication.translate("MainWindow", u"XYZ Stage", None))
        self.pushButton_stage_jogXReverse.setText(QCoreApplication.translate("MainWindow", u"X", None))
#if QT_CONFIG(statustip)
        self.pushButton_stage_moveToHomeXYZ.setStatusTip(QCoreApplication.translate("MainWindow", u"Homing XYZ", None))
#endif // QT_CONFIG(statustip)
        self.pushButton_stage_moveToHomeXYZ.setText("")
        self.pushButton_stage_moveToHomeY.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.pushButton_stage_jogZReverse.setText(QCoreApplication.translate("MainWindow", u"Z", None))
        self.pushButton_stage_jogZ.setText(QCoreApplication.translate("MainWindow", u"Z", None))
        self.pushButton_stage_moveToHomeX.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.pushButton_stage_jogY.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.pushButton_stage_jogYReverse.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.pushButton_stage_moveToHomeZ.setText(QCoreApplication.translate("MainWindow", u"Z", None))
        self.pushButton_stage_jogX.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"Jog Step", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Rotation (deg)", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"XY (mm)", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Z (mm)", None))
#if QT_CONFIG(tooltip)
        self.pushButton_stage_abort.setToolTip(QCoreApplication.translate("MainWindow", u"Abort all moves", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_stage_abort.setText(QCoreApplication.translate("MainWindow", u"Abort", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.StageTab), QCoreApplication.translate("MainWindow", u"Stage", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.CameraTab), QCoreApplication.translate("MainWindow", u"Camera", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.pliTab), QCoreApplication.translate("MainWindow", u"PLI", None))
        self.groupBox_viewer.setTitle(QCoreApplication.translate("MainWindow", u"Viewer", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.menuSettings.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.menuTools.setTitle(QCoreApplication.translate("MainWindow", u"Tools", None))
        self.menuConfiguration.setTitle(QCoreApplication.translate("MainWindow", u"Configuration", None))
    # retranslateUi

