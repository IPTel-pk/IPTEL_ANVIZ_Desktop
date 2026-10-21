from typing import Callable
from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel
from PySide6.QtCore import Qt
from app.ui.components.aside import Aside
from app.ui.components.header import Header
from app.settings import VERSION

class Activity(QWidget):
    """Basic structure of all the activities in the app."""
    def __init__(self, parent=None, activity:str="", navigate:Callable=lambda:print("No event set!")) -> None:
        """Initialize the basic app activity."""
        super().__init__(parent=parent)
        self.setStyleSheet("background-color: #f5f5f5;")
        self.setAutoFillBackground(True)

        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        aside = Aside(self, activity, navigate)
        layout.addWidget(aside)


        main = QWidget(self)
        main.setAutoFillBackground(True)
        main.setStyleSheet("background-color: #f5f5f5;")
        main_layout = QVBoxLayout(main)
        main_layout.setContentsMargins(30, 30, 30, 0)
        main_layout.setSpacing(0)

        header = Header(activity)
        main_layout.addWidget(header)

        self.content = QWidget(main)
        # self.content.setStyleSheet("""
        #     background-color: #ffffff;
        #     border: 1px solid #d9d9d9;
        # """)
        main_layout.addWidget(self.content, 1)

        footer = QLabel(VERSION)
        footer.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(footer)

        layout.addWidget(main, 1)
