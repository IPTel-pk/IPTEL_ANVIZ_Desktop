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
    """Header of the page representing the title and search functionality"""
    def __init__(self, title: str) -> None:
        """Initializes the Header and displays title of the Activity Page"""
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

        # 1. Main Horizontal Layout
        self.content_layout = QHBoxLayout(self)
        self.content_layout.setContentsMargins(15, 0, 15, 0)
        self.content_layout.setSpacing(15)
        self.content_layout.setAlignment(Qt.AlignmentFlag.AlignVCenter)

        # Title Label
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

        # Add Title to layout
        self.content_layout.addWidget(text)

        # Search Bar
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

        # Cancel Button
        cancel_btn = ToolbarButton("","assets/delete.png")

        # Add Search Input and Cancel Button to layout the '1' makes the search bar stretch to fill the space between the label and the cancel button
        self.content_layout.addWidget(search_input, 1) 
        self.content_layout.addWidget(cancel_btn)
