from PySide6.QtWidgets import (
    QHBoxLayout,
    QPushButton,
    QWidget,
)
from app.settings import ACCENT_COLOR, SECONDARY_COLOR, GRAY_TEXT_COLOR

class WorkingDaysWidget(QWidget):
    """Custom widget for circular day toggle buttons."""
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(5)

        days = ["M", "T", "W", "T", "F", "S", "S"]
        for day in days:
            btn = QPushButton(day)
            btn.setCheckable(True)
            btn.setFixedSize(24, 24)
            btn.setStyleSheet(f"""
                QPushButton {{
                    border-radius: 12px;
                    background-color: #f0f0f0;
                    color: {GRAY_TEXT_COLOR};
                    border: 1px solid {SECONDARY_COLOR};
                    font-size: 11px;
                    font-weight: bold;
                }}
                QPushButton:checked {{
                    background-color: {ACCENT_COLOR};
                    color: #ffffff;
                    border: 1px solid {ACCENT_COLOR};
                }}
            """)
            layout.addWidget(btn)
        layout.addStretch()
