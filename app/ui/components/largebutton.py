from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (
    QLabel,
    QPushButton,
    QSizePolicy,
    QVBoxLayout,
)
from app.settings import SECONDARY_COLOR, GRAY_TEXT_COLOR

class LargeButton(QPushButton):
    """Custom button for the top section with icon, title, and subtitle."""
    def __init__(
        self, title: str, subtitle: str, icon_path: str, parent=None
    ):
        super().__init__(parent)
        self.setFixedHeight(130)
        self.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed
        )
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setStyleSheet(f"""
            QPushButton {{
                background-color: #ffffff;
                border: 1px solid {SECONDARY_COLOR};
            }}
            QPushButton:hover {{
                background-color: #f9f9f9;
            }}
        """)
        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.setSpacing(2)

        icon_label = QLabel()
        pixmap = QPixmap(icon_path)
        if not pixmap.isNull():
            pixmap = pixmap.scaled(
                50,
                50,
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation,
            )
            icon_label.setPixmap(pixmap)
        icon_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        icon_label.setStyleSheet("border: none; background: transparent;")
        layout.addWidget(icon_label)

        title_label = QLabel(title)
        title_label.setStyleSheet("""
            font-size: 18px; font-weight: 500; border: none;
            background: transparent; color: #000000;
        """)
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title_label)

        sub_label = QLabel(subtitle)
        sub_label.setStyleSheet(f"""
            font-size: 10px; color: {GRAY_TEXT_COLOR};
            border: none; background: transparent;
        """)
        sub_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(sub_label)
