from typing import Callable
from PySide6.QtWidgets import QPushButton, QHBoxLayout
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize
from app.settings import ACCENT_COLOR, ACCENT_HOVER_COLOR
import os

class AsideButton(QPushButton):
    """
    ### AsideButton
    This widget represents a single navigation item in the left sidebar and highlights the active section.
    """

    def __init__(self, text:str, navigate:Callable, active:bool=False):
        """
        Initialize the sidebar action button.

        This method sets up the label, icon, click callback, and active/inactive styling for a single navigation button.
        """
        super().__init__(" "+text)
        self.setFixedHeight(50)
        self.clicked.connect(navigate)
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        # 1. Add an icon before the menu text when the asset exists
        icon_path = f"assets/{text}.png"
        if os.path.exists(icon_path):
            icon = QIcon(icon_path)
            self.setIcon(icon)
            self.setIconSize(QSize(24, 24))

        # 2. Apply styling for the active menu item
        if active:
            self.setStyleSheet(self.styleSheet() + """
                QPushButton {
                    background-color: #415162;
                    border-left: 4px solid #21679A;
                    color: #ffffff;
                    text-align: left;
                    padding-left: 10px;
                    border-right: none;
                    border-top: none;
                    border-bottom: none;
                }
            """)
        else:
            # 3. Apply the default sidebar button styling
            self.setStyleSheet(f"""
                QPushButton {{
                    background-color: {ACCENT_COLOR};
                    color: #ffffff;
                    border: none;
                    text-align: left;
                    padding-left: 10px;
                }}
                QPushButton:hover {{
                    background-color: {ACCENT_HOVER_COLOR};
                }}
            """)
