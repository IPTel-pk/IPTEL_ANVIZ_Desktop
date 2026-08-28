from typing import Callable
from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel
from app.ui.components.aside import Aside

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

        aside = Aside(self, activity)
        layout.addWidget(aside)

        content = QWidget(self)
        content.setAutoFillBackground(True)
        content.setStyleSheet("background-color: #f5f5f5;")
        content_layout = QHBoxLayout(content)
        content_layout.setContentsMargins(20, 20, 20, 20)
        content_layout.addWidget(QLabel("Devices Activity (file is open)"))

        layout.addWidget(content, 1)
