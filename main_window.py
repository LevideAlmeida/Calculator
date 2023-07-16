from PySide6.QtWidgets import QMainWindow, QWidget, QGridLayout
from typing import Union


class MainWindow(QMainWindow):
    def __init__(self, parent: Union[QWidget, None] = None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        # Setting Layout
        self.cw = QWidget()
        self.setCentralWidget(self.cw)

        self.gridLayout = QGridLayout()

        self.cw.setLayout(self.gridLayout)

        # Set title
        self.setWindowTitle('Calculator')

    def adjustFixedSize(self):
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())

    def addWidgetToLayout(self, widget: QWidget):
        self.gridLayout.addWidget(widget)
        self.adjustFixedSize()
