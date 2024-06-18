# This Python file uses the following encoding: utf-8
import sys

import numpy as np
import pyqtgraph as pg
import qdarktheme
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QPixmap

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.update_image(np.random.rand(100, 100))
        self.init_viewer()
        self.update_view()

    def init_ui(self):
        # Set the icons
        self.ui.actionOpen.setIcon(QPixmap("resources/open.svg"))

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

    def update_view(self):
        # Simulate an image
        img = np.random.rand(100, 100)
        self.imageItem.setImage(img)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QPixmap("resources/linum-logo.svg"))
    qdarktheme.setup_theme("auto")  # Apply the system's color theme
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
