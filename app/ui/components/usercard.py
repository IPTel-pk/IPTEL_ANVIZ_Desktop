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
from app.settings import ACCENT_COLOR, SECONDARY_COLOR, GRAY_TEXT_COLOR

class UserCard(QWidget):
    """Custom widget representing a single user."""
    def __init__(self, name: str, department: str, parent=None):
        super().__init__(parent)
        self.setFixedHeight(70)
        self.setMinimumWidth(250)
        self.setMaximumWidth(350)
        self.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed
        )
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        
        layout = QHBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(5)

        # Checkbox (Moved to Left)
        self.checkbox = QCheckBox()
        self.checkbox.setStyleSheet("border: none; background: transparent;")

        # Connect checkbox state to the styling function
        self.checkbox.stateChanged.connect(self._update_card_style)
        layout.addWidget(
            self.checkbox,
            alignment=Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft
        )

        # Image
        icon_label = QLabel()
        pixmap = QPixmap("assets/user.png")
        if not pixmap.isNull():
            icon_label.setPixmap(pixmap.scaled(
                50, 50, 
                Qt.AspectRatioMode.KeepAspectRatio, 
                Qt.TransformationMode.SmoothTransformation
            ))
        icon_label.setFixedSize(50, 50)
        icon_label.setStyleSheet("border: none; background: transparent;")
        layout.addWidget(icon_label)

        # Text Labels
        text_layout = QVBoxLayout()
        text_layout.setSpacing(2)
        text_layout.setAlignment(Qt.AlignmentFlag.AlignVCenter)

        name_label = QLabel(name)
        name_label.setStyleSheet("""
            font-size: 16px; font-weight: bold; color: #000000;
            border: none; background: transparent;
        """)
        name_label.setTextInteractionFlags(
            Qt.TextInteractionFlag.TextSelectableByMouse
        )
        dept_label = QLabel(department)
        dept_label.setStyleSheet(f"""
            font-size: 13px; color: {GRAY_TEXT_COLOR};
            border: none; background: transparent;
        """)
        dept_label.setTextInteractionFlags(
            Qt.TextInteractionFlag.TextSelectableByMouse
        )

        text_layout.addWidget(name_label)
        text_layout.addWidget(dept_label)
        layout.addLayout(text_layout)

        # Pushes everything to the left
        layout.addStretch()

        # Initialize border styling based on default checkbox state
        self._update_card_style()

    def _update_card_style(self) -> None:
        """Changes the card border to ACCENT_COLOR when checked."""
        if self.checkbox.isChecked():
            border_color = ACCENT_COLOR
        else: border_color = SECONDARY_COLOR
        self.setStyleSheet(f"""
            UserCard {{
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
