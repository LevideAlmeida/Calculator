import sys
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from main_window import MainWindow
from variables import ICON_PATH
from display import Display

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()

    # Add Display
    display = Display()
    window.addWidgetToLayout(display)

    # Add icon
    icon = QIcon(str(ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # Run
    window.show()
    app.exec()
