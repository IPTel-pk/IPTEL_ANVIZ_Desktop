from typing import Callable
from PySide6.QtWidgets import QPushButton, QHBoxLayout
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize
from app.settings import ACCENT_COLOR
import os

class AsideButton(QPushButton):
    """Basic Template for Buttons in the Aside Bar"""
    def __init__(self, text:str, navigate:Callable, active:bool=False):
        """Initializes a button for Aside Bar Menu"""
        super().__init__(" "+text)
        self.setFixedHeight(50)
        self.clicked.connect(navigate)
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        
        # Add icon before the text
        icon_path = f"assets/{text}.png"
        if os.path.exists(icon_path):
            icon = QIcon(icon_path)
            self.setIcon(icon)
            self.setIconSize(QSize(24, 24))

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
            self.setStyleSheet(f"""
                QPushButton {{
                    background-color: {ACCENT_COLOR};
                    color: #ffffff;
                    border: none;
                    text-align: left;
                    padding-left: 10px;
                }}
                QPushButton:hover {{
                    background-color: #34495e;
                }}
            """)
