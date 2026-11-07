from PySide6.QtWidgets import (
    QHBoxLayout,
    QPushButton,
    QWidget,
)
from app.settings import ACCENT_COLOR, SECONDARY_COLOR, GRAY_TEXT_COLOR

class WorkingDaysWidget(QWidget):
    """
    ### WorkingDaysWidget
    This widget displays a row of circular toggle buttons for selecting active working days in a department schedule.
    """

    def __init__(self, parent=None):
        """
        Initialize the working day selector.

        This method builds the compact row of day buttons and styles the checked and unchecked states for clear selection.
        """
        super().__init__(parent)

        # 1. Create the horizontal layout for the day buttons
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(5)

        # 2. Define the weekday labels and create toggle buttons for each day
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

        # 3. Add stretch to keep the toggle buttons aligned to the left
        layout.addStretch()
