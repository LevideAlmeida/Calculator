from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout
from typing import Union


class MainWindow(QMainWindow):
    def __init__(self, parent: Union[QWidget, None] = None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        # Setting Layout
        self.cw = QWidget()
        self.setCentralWidget(self.cw)

        self.vLayout = QVBoxLayout()

        self.cw.setLayout(self.vLayout)

        # Set title
        self.setWindowTitle('Calculator')

    def adjustFixedSize(self):
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())

    def addWidgetToLayout(self, widget: QWidget):
        self.vLayout.addWidget(widget)
