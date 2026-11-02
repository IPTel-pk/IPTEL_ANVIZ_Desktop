from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QMouseEvent
from PySide6.QtWidgets import (
    QCheckBox,
    QHBoxLayout,
    QLabel,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
    QGridLayout,
)
from app.settings import ACCENT_COLOR, SECONDARY_COLOR

class DeviceCard(QWidget):
    """Custom widget representing a single device."""
    def __init__(
        self, name: str, model: str, ip: str, port: str, serial: str,
        last_seen: str, is_online: bool, parent=None
    ):
        super().__init__(parent)
        self.setMinimumWidth(200)
        self.setMaximumWidth(280)
        self.setSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed
        )
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        
        layout = QVBoxLayout(self)
        layout.setContentsMargins(15, 15, 15, 15)
        layout.setSpacing(10)

        # Top Row: Checkbox
        top_row = QHBoxLayout()
        self.checkbox = QCheckBox() # Stored as instance variable
        self.checkbox.setStyleSheet(
            "border: none; background: transparent;"
        )
        # Connect checkbox state to the styling function
        self.checkbox.stateChanged.connect(self._update_card_style)
        top_row.addWidget(self.checkbox)
        top_row.addStretch()
        layout.addLayout(top_row)

        # Centered Icon
        icon_layout = QHBoxLayout()
        icon_label = QLabel()
        pixmap = QPixmap("assets/device.jpg")
        if not pixmap.isNull():
            icon_label.setPixmap(pixmap.scaled(
                50, 50,
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            ))
        icon_label.setFixedSize(50, 50)
        icon_label.setStyleSheet("border: none; background: transparent;")
        icon_layout.addStretch()
        icon_layout.addWidget(icon_label)
        icon_layout.addStretch()
        layout.addLayout(icon_layout)

        # Status Indicator
        status_layout = QHBoxLayout()
        status_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        status_layout.setSpacing(5)

        dot = QLabel()
        dot.setFixedSize(10, 10)
        color = "#2ecc71" if is_online else "#bdc3c7"
        dot.setStyleSheet(
            f"background-color: {color}; border-radius: 5px; border: none;"
        )
        status_text = QLabel("Online" if is_online else "Offline")
        status_text.setStyleSheet("""
            font-size: 11px; color: #000000; border: none;
            background: transparent;
        """)
        status_text.setTextInteractionFlags(
            Qt.TextInteractionFlag.TextSelectableByMouse
        )
        status_layout.addWidget(dot)
        status_layout.addWidget(status_text)
        layout.addLayout(status_layout)

        # Title & Subtitle
        title_label = QLabel(name)
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setWordWrap(True)
        title_label.setStyleSheet("""
            font-size: 18px; font-weight: bold; color: #000000;
            border: none; background: transparent;
        """)
        title_label.setTextInteractionFlags(
            Qt.TextInteractionFlag.TextSelectableByMouse
        )
        layout.addWidget(title_label)

        subtitle_label = QLabel(model)
        subtitle_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        subtitle_label.setWordWrap(True)
        subtitle_label.setStyleSheet("""
            font-size: 14px; color: #000000;
            border: none; background: transparent;
        """)
        subtitle_label.setTextInteractionFlags(
            Qt.TextInteractionFlag.TextSelectableByMouse
        )
        layout.addWidget(subtitle_label)

        # Properties Grid
        props_layout = QGridLayout()
        props_layout.setContentsMargins(0, 10, 0, 0)
        props_layout.setVerticalSpacing(4)
        props = [
            ("IP", ip), ("Port", port), 
            ("Serial No.", serial), ("Last Seen", last_seen)
        ]
        for row, (key, value) in enumerate(props):
            key_label = QLabel(key)
            key_label.setStyleSheet("""
                font-size: 11px; font-weight: bold; color: #000000;
                border: none; background: transparent;
            """)
            key_label.setTextInteractionFlags(
                Qt.TextInteractionFlag.TextSelectableByMouse
            )
            val_label = QLabel(value)
            val_label.setWordWrap(True)
            val_label.setStyleSheet("""
                font-size: 11px; color: #878787;
                border: none; background: transparent;
            """)
            val_label.setTextInteractionFlags(
                Qt.TextInteractionFlag.TextSelectableByMouse
            )
            props_layout.addWidget(
                key_label, row, 0,
                Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft
            )
            props_layout.addWidget(
                val_label, row, 1,
                Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft
            )
        props_layout.setColumnStretch(1, 1)
        layout.addLayout(props_layout)
        self._update_card_style()

    def _update_card_style(self) -> None:
        """Changes the card border to ACCENT_COLOR when checked."""
        if self.checkbox.isChecked():
            border_color = ACCENT_COLOR
        else:
            border_color = SECONDARY_COLOR
        self.setStyleSheet(f"""
            DeviceCard {{
                background-color: #ffffff;
                border: 1px solid {border_color};
            }}
        """)

    def mousePressEvent(self, event: QMouseEvent) -> None:
        """Toggle checkbox when clicking anywhere on the card."""
        if event.button() == Qt.MouseButton.LeftButton:
            child = self.childAt(event.pos())

            # If clicked on the card but NOT
            # On the checkbox itself, toggle it manually
            if child != self.checkbox:
                self.checkbox.setChecked(not self.checkbox.isChecked())

        super().mousePressEvent(event)
