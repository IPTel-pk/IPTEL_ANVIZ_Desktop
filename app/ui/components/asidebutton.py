from typing import Callable
from PySide6.QtWidgets import QPushButton
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize
import os

class AsideButton(QPushButton):
    def __init__(self, text:str, navigate:Callable, active:bool=False):
        super().__init__(text)
        self.setFixedHeight(50)
        self.clicked.connect(navigate)
        
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
            self.setStyleSheet("""
                QPushButton {
                    background-color: #2c3e50;
                    color: #ffffff;
                    border: none;
                    text-align: left;
                    padding-left: 10px;
                }
                QPushButton:hover {
                    background-color: #34495e;
                }
            """)
