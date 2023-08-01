import sys
from info import Info
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from main_window import MainWindow
from variables import ICON_PATH
from display import Display
from style import setupTheme

if __name__ == '__main__':

    # Set application
    app = QApplication(sys.argv)
    setupTheme()

    # Set window
    window = MainWindow()

    # Add icon
    icon = QIcon(str(ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # last equation info
    last_equation = Info('2.0 ^ 10.0 = 1024')
    window.gridLayout.addWidget(last_equation)

    # Add Display
    display = Display()
    window.addWidgetToLayout(display)

    # Run
    window.show()
    app.exec()
