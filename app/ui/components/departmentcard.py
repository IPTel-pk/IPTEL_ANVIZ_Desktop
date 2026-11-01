from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QMouseEvent
from PySide6.QtWidgets import (
    QCheckBox,
    QHBoxLayout,
    QLabel,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)

# Assuming you have this in your settings file
from app.settings import ACCENT_COLOR


class DepartmentCard(QWidget):
    """Custom widget representing a single department."""
    def __init__(self, name: str, start_time: str, off_time: str, working_days: str, parent=None):
        super().__init__(parent)
        self.setMinimumWidth(250)
        self.setMaximumWidth(300)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        
        # Add a pointing hand cursor
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        
        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(5)

        # --- Top Row: Checkbox and Department Name ---
        top_row = QHBoxLayout()
        top_row.setSpacing(5)
        
        self.checkbox = QCheckBox() # Stored as instance variable
        self.checkbox.setStyleSheet("border: none; background: transparent;")
        # Connect checkbox state to the styling function
        self.checkbox.stateChanged.connect(self._update_card_style)
        top_row.addWidget(self.checkbox)
        
        name_label = QLabel(name)
        name_label.setStyleSheet("font-size: 14px; font-weight: bold; color: #000000; border: none; background: transparent;")
        name_label.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
        top_row.addWidget(name_label)
        top_row.addStretch()
        
        layout.addLayout(top_row)

        # --- Bottom Row: Image and Details ---
        bottom_row = QHBoxLayout()
        bottom_row.setSpacing(10)

        # Icon Placeholder
        icon_label = QLabel()
        pixmap = QPixmap("assets/group.png")
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
        start_lbl.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
        
        off_lbl = QLabel(f"Off: {off_time}")
        off_lbl.setStyleSheet("font-size: 12px; color: #000000; border: none; background: transparent;")
        off_lbl.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
        
        days_lbl = QLabel(f"Working Days: {working_days}")
        days_lbl.setStyleSheet("font-size: 12px; color: #000000; border: none; background: transparent;")
        days_lbl.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)

        details_layout.addWidget(start_lbl)
        details_layout.addWidget(off_lbl)
        details_layout.addWidget(days_lbl)
        
        bottom_row.addLayout(details_layout)
        bottom_row.addStretch()
        
        layout.addLayout(bottom_row)

        # Initialize border styling based on default checkbox state
        self._update_card_style()

    def _update_card_style(self) -> None:
        """Changes the card border to ACCENT_COLOR when checked."""
        border_color = ACCENT_COLOR if self.checkbox.isChecked() else "#d9d9d9"
        self.setStyleSheet(f"""
            DepartmentCard {{
                background-color: #ffffff;
                border: 1px solid {border_color};
            }}
        """)

    def mousePressEvent(self, event: QMouseEvent) -> None:
        """Toggle checkbox when clicking anywhere on the card."""
        if event.button() == Qt.MouseButton.LeftButton:
            # Check if the user clicked directly on the checkbox
            child = self.childAt(event.pos())
            
            # If clicked on the card but NOT on the checkbox itself, toggle it manually
            if child != self.checkbox:
                self.checkbox.setChecked(not self.checkbox.isChecked())
                
        super().mousePressEvent(event)