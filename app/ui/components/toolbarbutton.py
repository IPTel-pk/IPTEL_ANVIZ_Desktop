from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QPushButton, QSizePolicy

class ToolbarButton(QPushButton):
    """Helper class for the top action buttons."""
    def __init__(self, text: str, icon_path: str, parent=None):
        super().__init__(text, parent)
        self.setIcon(QIcon(icon_path))
        self.setIconSize(QSize(16, 16))
        self.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.setFixedHeight(36)
        self.setStyleSheet("""
            QPushButton {
                background-color: #ffffff;
                color: #000000;
                border: 1px solid #d9d9d9;
                padding: 0 15px;
                font-size: 13px;
            }
            QPushButton:hover {
                background-color: #f9f9f9;
            }
            QPushButton:pressed {
                background-color: #e0e0e0;
            }
        """)
