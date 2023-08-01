import sys
from info import Info
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from main_window import MainWindow
from variables import ICON_PATH
from display import Display
from style import setupTheme
from buttons import Button

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

    # Buttons
    plus_button = Button('+')
    minus_button = Button('-')
    times_button = Button('*')
    division_button = Button('/')

    window.addWidgetToLayout(plus_button)
    window.addWidgetToLayout(minus_button)
    window.addWidgetToLayout(times_button)
    window.addWidgetToLayout(division_button)

    # Run
    window.adjustFixedSize()
    window.show()
    app.exec()
