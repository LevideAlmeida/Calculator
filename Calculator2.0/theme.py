import qdarktheme
from values import PRIMARY_COLOR, DARKER_PRIMARY_COLOR, DARKEST_PRIMARY_COLOR

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


def setup_theme():
    qdarktheme.setup_theme(
        theme='dark',
        corner_shape='sharp',
        custom_colors={'primary': f'{PRIMARY_COLOR}'},
        additional_qss=qss
    )
