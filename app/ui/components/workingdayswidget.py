from PySide6.QtWidgets import (
    QHBoxLayout,
    QPushButton,
    QWidget,
)

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
            btn.setStyleSheet("""
                QPushButton {
                    border-radius: 12px;
                    background-color: #f0f0f0;
                    color: #878787;
                    border: 1px solid #d9d9d9;
                    font-size: 11px;
                    font-weight: bold;
                }
                QPushButton:checked {
                    background-color: #21679A;
                    color: #ffffff;
                    border: 1px solid #21679A;
                }
            """)
            layout.addWidget(btn)
        layout.addStretch()
