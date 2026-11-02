from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QPushButton,
    QWidget,
)
from app.settings import SECONDARY_COLOR, GRAY_TEXT_COLOR

class PaginationFooter(QWidget):
    """Reusable footer for pagination controls."""
    def __init__(
        self, showing_text: str = "Showing 1-20 of 100", parent=None
    ):
        super().__init__(parent)
        self.setStyleSheet("background: transparent;")
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 10, 0, 0)

        # Left label
        showing_lbl = QLabel(showing_text)
        showing_lbl.setStyleSheet(
            f"font-size: 12px; color: {GRAY_TEXT_COLOR}; border: none;"
        )
        layout.addWidget(showing_lbl)
        layout.addStretch()

        # Right buttons
        btn_style = f"""
            QPushButton {{
                background-color: #ffffff;
                color: #000000;
                border: 1px solid {SECONDARY_COLOR};
                font-size: 14px;
                font-weight: bold;
                padding-bottom: 2px;
            }}
            QPushButton:hover {{
                background-color: #f9f9f9;
            }}
        """
        left_btn = QPushButton("←")
        left_btn.setFixedSize(32, 32)
        left_btn.setStyleSheet(btn_style)
        layout.addWidget(left_btn)

        right_btn = QPushButton("→")
        right_btn.setFixedSize(32, 32)
        right_btn.setStyleSheet(btn_style)
        layout.addWidget(right_btn)
