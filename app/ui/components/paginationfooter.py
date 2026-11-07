from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QPushButton,
    QWidget,
)
from app.settings import SECONDARY_COLOR, GRAY_TEXT_COLOR

class PaginationFooter(QWidget):
    """
    ### PaginationFooter
    This widget shows the current item range and provides previous/next pagination controls for table-based screens.
    """

    def __init__(
        self, showing_text: str = "Showing 1-20 of 100", parent=None
    ):
        """
        Initialize the pagination footer.

        This method sets up the summary label and the next/previous buttons used to move across paged records.
        """
        super().__init__(parent)
        self.setStyleSheet("background: transparent;")

        # 1. Create the footer layout
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 10, 0, 0)

        # 2. Add the summary text on the left side
        showing_lbl = QLabel(showing_text)
        showing_lbl.setStyleSheet(
            f"font-size: 12px; color: {GRAY_TEXT_COLOR}; border: none;"
        )
        layout.addWidget(showing_lbl)
        layout.addStretch()

        # 3. Add the navigation buttons on the right side
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
