# Calculator theme style

# QT style for python Doc:
# https://doc.qt.io/qtforpython/tutorials/basictutorial/widgetstyling.html

# Used theme:
# https://pyqtdarktheme.readthedocs.io/en/latest/how_to_use.html

from variables import (PRIMARY_COLOR, DARKER_PRIMARY_COLOR,
                       DARKEST_PRIMARY_COLOR)

import qdarktheme

qss = f"""
    QPushButton[cssClass="specialButton"] {{
        color: #fff;
        background: {PRIMARY_COLOR};
    }}
    QPushButton[cssClass="specialButton"]:hover {{
        color: #fff;
        background: {DARKER_PRIMARY_COLOR};
    }}
    QPushButton[cssClass="specialButton"]:pressed {{
        color: #fff;
        background: {DARKEST_PRIMARY_COLOR};
    }}
"""


def setupTheme():
    qdarktheme.setup_theme(
        theme='dark',
        corner_shape='sharp',
        custom_colors={
            "primary": f"{PRIMARY_COLOR}"
        },
        additional_qss=qss
    )
