from PySide6.QtWidgets import QPushButton
from app.settings import ACCENT_COLOR, ACCENT_HOVER_COLOR

class PrimaryButton(QPushButton):
    """Reusable primary action button (e.g., Save, Submit, Export)."""
    
    def __init__(self, text: str, parent=None):
        super().__init__(text, parent)
        
        self.setFixedHeight(36)
        self.setStyleSheet(f"""
            QPushButton {{
                background-color: {ACCENT_COLOR};
                color: #ffffff;
                border: none;
                font-size: 13px;
                font-weight: bold;
            }}
            QPushButton:hover {{
                background-color: {ACCENT_HOVER_COLOR};
            }}
            QPushButton:disabled {{
                background-color: #a0a0a0;
                color: #e0e0e0;
            }}
        """)