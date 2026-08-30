from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt

class Header(QWidget):
    """Header of the page representing the title"""
    def __init__(self, title: str) -> None:
        """Initializes the Header and display title of the Activity Page"""
        super().__init__()
        
        self.setFixedHeight(80)
        self.setStyleSheet("""
            background-color: #ffffff;
            border: 1px solid #d9d9d9;
            border-left: none;
        """)
        
        self.content_layout = QHBoxLayout(self)
        self.content_layout.setContentsMargins(0, 0, 0, 0)
        self.content_layout.setSpacing(0)

        # Creating a spacer
        spacer = QWidget(self)
        spacer.setFixedWidth(10)
        spacer.setContentsMargins(0,0,0,0)
        spacer.setStyleSheet("border: 1px solid #d9d9d9;border-right:none;")
        
        # Create title label
        text = QLabel(title, parent=self)
        text.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        
        # Set font
        font = QFont()
        font.setPointSize(28)
        font.setBold(True)
        text.setFont(font)
        
        self.content_layout.addWidget(spacer)
        self.content_layout.addWidget(text, 1)
