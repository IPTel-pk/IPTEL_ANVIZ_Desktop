from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (
    QCheckBox,
    QHBoxLayout,
    QLabel,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)

class UserCard(QWidget):
    """Custom widget representing a single user."""
    def __init__(self, name: str, department: str, parent=None):
        super().__init__(parent)
        self.setFixedHeight(70)
        self.setMinimumWidth(250)
        self.setMaximumWidth(350)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        
        self.setStyleSheet("""
            UserCard {
                background-color: #ffffff;
                border: 1px solid #d9d9d9;
            }
        """)
        
        layout = QHBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(15)

        # --- Checkbox (Moved to Left) ---
        checkbox = QCheckBox()
        checkbox.setStyleSheet("border: none; background: transparent;")
        layout.addWidget(checkbox, alignment=Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)

        # --- Image (90% of card height) ---
        # Card is 70px tall, 10px top margin + 10px bottom margin = 50px available. 
        # 90% of 70 is ~63px. We'll scale it to fit nicely.
        icon_label = QLabel()
        pixmap = QPixmap("assets/icon.jpg")
        if not pixmap.isNull():
            icon_label.setPixmap(pixmap.scaled(
                50, 50, 
                Qt.AspectRatioMode.KeepAspectRatio, 
                Qt.TransformationMode.SmoothTransformation
            ))
        icon_label.setFixedSize(50, 50)
        icon_label.setStyleSheet("border: none; background: transparent;")
        layout.addWidget(icon_label)

        # --- Text Labels ---
        text_layout = QVBoxLayout()
        text_layout.setSpacing(2)
        text_layout.setAlignment(Qt.AlignmentFlag.AlignVCenter)

        name_label = QLabel(name)
        name_label.setStyleSheet("font-size: 16px; font-weight: bold; color: #000000; border: none; background: transparent;")
        
        dept_label = QLabel(department)
        dept_label.setStyleSheet("font-size: 13px; color: #878787; border: none; background: transparent;")
        
        text_layout.addWidget(name_label)
        text_layout.addWidget(dept_label)
        layout.addLayout(text_layout)

        layout.addStretch() # Pushes everything to the left
