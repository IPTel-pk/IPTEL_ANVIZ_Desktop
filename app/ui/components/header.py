from PySide6.QtWidgets import (
    QWidget, 
    QHBoxLayout, 
    QLabel,
    QLineEdit,
    QSizePolicy,
)
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt
from app.ui.components.toolbarbutton import ToolbarButton
from app.settings import ACCENT_COLOR, SECONDARY_COLOR

class Header(QWidget):
    """
    ### Header
    This widget displays the top page title and search controls that appear at the top of each activity screen.
    """

    def __init__(self, title: str) -> None:
        """
        Initialize the page header.

        This method builds the header container, sets the title label, and adds the search field with the action button.
        """
        super().__init__()

        self.setObjectName("headerWidget")
        self.setAutoFillBackground(True)
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed
        )
        self.setFixedHeight(80)

        self.setStyleSheet(f"""
            QWidget#headerWidget {{
                background-color: #ffffff;
                border: 1px solid {SECONDARY_COLOR};
            }}
        """)

        # 1. Create the main horizontal layout for the header row
        self.content_layout = QHBoxLayout(self)
        self.content_layout.setContentsMargins(15, 0, 15, 0)
        self.content_layout.setSpacing(15)
        self.content_layout.setAlignment(Qt.AlignmentFlag.AlignVCenter)

        # 2. Add the page title label
        text = QLabel(title, parent=self)
        text.setAlignment(
            Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter
        )
        text.setStyleSheet("""
            QLabel {
                border: none;
                background: transparent;
            }
        """)
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        text.setFont(font)
        self.content_layout.addWidget(text)

        # 3. Add the search input field
        search_input = QLineEdit()
        search_input.setPlaceholderText("Search...")
        search_input.setFixedHeight(36)
        search_input.setStyleSheet(f"""
            QLineEdit {{
                border: 1px solid {SECONDARY_COLOR};
                padding: 0 10px;
                font-size: 13px;
                background-color: #ffffff;
                color: #000000;
            }}
            QLineEdit:focus {{
                border: 1px solid {ACCENT_COLOR};
            }}
        """)

        # 4. Add the cancel button at the end of the row
        cancel_btn = ToolbarButton("","assets/delete.png")
        self.content_layout.addWidget(search_input, 1)
        self.content_layout.addWidget(cancel_btn)
