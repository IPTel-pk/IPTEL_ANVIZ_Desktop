from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QPushButton,
    QWidget,
)
from data.attendance import data

class PaginationFooter(QWidget):
    """Reusable footer for pagination controls."""
    def __init__(self, showing_text: str = "Showing 1-20 of 100", parent=None):
        super().__init__(parent)
        self.setStyleSheet("background: transparent;")
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 10, 0, 0)

        # Left label
        showing_lbl = QLabel(showing_text)
        showing_lbl.setStyleSheet("font-size: 12px; color: #878787; border: none;")
        layout.addWidget(showing_lbl)

        layout.addStretch()

        # Right buttons
        btn_style = """
            QPushButton {
                background-color: #ffffff;
                color: #000000;
                border: 1px solid #d9d9d9;
                font-size: 14px;
                font-weight: bold;
                padding-bottom: 2px;
            }
            QPushButton:hover {
                background-color: #f9f9f9;
            }
        """
        left_btn = QPushButton("←")
        left_btn.setFixedSize(32, 32)
        left_btn.setStyleSheet(btn_style)
        layout.addWidget(left_btn)

        right_btn = QPushButton("→")
        right_btn.setFixedSize(32, 32)
        right_btn.setStyleSheet(btn_style)
        layout.addWidget(right_btn)
