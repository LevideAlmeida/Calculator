from PySide6.QtWidgets import QMainWindow, QWidget, QGridLayout
from typing import Union


class MainWindow(QMainWindow):
    def __init__(self, parent: Union[QWidget, None] = None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        # Setting Layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.grid_layout = QGridLayout()

        self.central_widget.setLayout(self.grid_layout)

        # Set title
        self.setWindowTitle('Calculator')

    def adjustFixedSize(self):
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())
