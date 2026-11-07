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
    """
    ### LargeButton
    This widget creates a wide action button with an icon, primary title, and smaller subtitle for launcher-style actions.
    """

    def __init__(
        self, title: str, subtitle: str, icon_path: str, parent=None
    ):
        """
        Initialize the large action button.

        This method sets the button size, adds the icon and text labels, and applies the card-like styling for launcher actions.
        """
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

        # 1. Build the main vertical layout for icon and text
        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.setSpacing(2)

        # 2. Add the icon to the top of the button
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

        # 3. Add the main action title
        title_label = QLabel(title)
        title_label.setStyleSheet("""
            font-size: 18px; font-weight: 500; border: none;
            background: transparent; color: #000000;
        """)
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title_label)

        # 4. Add the subtitle text below the title
        sub_label = QLabel(subtitle)
        sub_label.setStyleSheet(f"""
            font-size: 10px; color: {GRAY_TEXT_COLOR};
            border: none; background: transparent;
        """)
        sub_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(sub_label)
