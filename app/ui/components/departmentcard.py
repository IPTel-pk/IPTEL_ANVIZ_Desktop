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

class DepartmentCard(QWidget):
    """Custom widget representing a single department."""
    def __init__(self, name: str, start_time: str, off_time: str, working_days: str, parent=None):
        super().__init__(parent)
        self.setMinimumWidth(250)
        self.setMaximumWidth(300)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        
        self.setStyleSheet("""
            DepartmentCard {
                background-color: #ffffff;
                border: 1px solid #d9d9d9;
            }
        """)
        
        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(5)

        # --- Top Row: Checkbox and Department Name ---
        top_row = QHBoxLayout()
        top_row.setSpacing(5)
        
        checkbox = QCheckBox()
        checkbox.setStyleSheet("border: none; background: transparent;")
        top_row.addWidget(checkbox)
        
        name_label = QLabel(name)
        name_label.setStyleSheet("font-size: 14px; font-weight: bold; color: #000000; border: none; background: transparent;")
        top_row.addWidget(name_label)
        top_row.addStretch()
        
        layout.addLayout(top_row)

        # --- Bottom Row: Image and Details ---
        bottom_row = QHBoxLayout()
        bottom_row.setSpacing(10)

        # Icon Placeholder
        icon_label = QLabel()
        pixmap = QPixmap("assets/icon.jpg")
        if not pixmap.isNull():
            icon_label.setPixmap(pixmap.scaled(
                45, 45, 
                Qt.AspectRatioMode.KeepAspectRatio, 
                Qt.TransformationMode.SmoothTransformation
            ))
        icon_label.setFixedSize(45, 45)
        icon_label.setStyleSheet("border: none; background: transparent;")
        bottom_row.addWidget(icon_label)

        # Details Layout
        details_layout = QVBoxLayout()
        details_layout.setSpacing(2)
        details_layout.setAlignment(Qt.AlignmentFlag.AlignVCenter)

        start_lbl = QLabel(f"Start: {start_time}")
        start_lbl.setStyleSheet("font-size: 12px; color: #000000; border: none; background: transparent;")
        
        off_lbl = QLabel(f"Off: {off_time}")
        off_lbl.setStyleSheet("font-size: 12px; color: #000000; border: none; background: transparent;")
        
        days_lbl = QLabel(f"Working Days: {working_days}")
        days_lbl.setStyleSheet("font-size: 12px; color: #000000; border: none; background: transparent;")

        details_layout.addWidget(start_lbl)
        details_layout.addWidget(off_lbl)
        details_layout.addWidget(days_lbl)
        
        bottom_row.addLayout(details_layout)
        bottom_row.addStretch()
        
        layout.addLayout(bottom_row)
