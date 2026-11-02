from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)
from app.settings import GRAY_TEXT_COLOR

class ActivityItem(QWidget):
    def __init__(
        self, title: str, subtitle: str, time_text: str,
        status: str = 'o', parent=None
    ):
        super().__init__(parent)
        self.setFixedHeight(54)
        self.setStyleSheet("""
            QWidget {
                background-color: transparent; border: none;
            }
        """)
        layout = QHBoxLayout(self)
        layout.setContentsMargins(15, 6, 15, 6)
        layout.setSpacing(12)

        # Dictionary maps status code to: (Background Color, Icon Path)
        status_mapping = {
            'o': ("#d4edda", "assets/ok.png"),      # Ok (Light Green)
            'a': ("#cce5ff", "assets/add.png"),     # Add (Light Blue)
            'e': ("#fff3cd", "assets/edit.png"),    # Edit (Light Yellow)
            'd': ("#f8d7da", "assets/delete.png"),  # Delete (Light Red)
            'i': ("#ffe8cc", "assets/info.png"),    # Info (Light Orange)
        }
        bg_color, icon_path = status_mapping.get(status, status_mapping['o'])

        # 1. Create the indicator label with the background color
        indicator = QLabel()
        indicator.setFixedSize(30, 30)
        indicator.setAlignment(Qt.AlignmentFlag.AlignCenter)
        indicator.setStyleSheet(f"""
            QLabel {{
                background-color: {bg_color};
                border: none;
                border-radius: 15px;
            }}
        """)

        # 2. Load and set the specific icon based on status
        pixmap = QPixmap(icon_path)
        if not pixmap.isNull():
            # Scale the image to fit inside the 30x30 circle
            scaled_pixmap = pixmap.scaled(
                10, 10, 
                Qt.AspectRatioMode.KeepAspectRatio, 
                Qt.TransformationMode.SmoothTransformation
            )
            indicator.setPixmap(scaled_pixmap)
        else:
            # Optional: Fallback text if the image fails to load
            indicator.setText("?")
        layout.addWidget(indicator, alignment=Qt.AlignmentFlag.AlignVCenter)

        # Text Layout
        text_col = QWidget()
        text_col.setStyleSheet("background: transparent; border: none;")
        text_col.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed
        )
        text_col_layout = QVBoxLayout(text_col)
        text_col_layout.setContentsMargins(0, 0, 0, 0)
        text_col_layout.setSpacing(0)

        title_label = QLabel(title)
        title_label.setStyleSheet("""
            font-size: 16px; color: #000000;
            border: none; background: transparent;
        """)
        text_col_layout.addWidget(title_label)

        subtitle_label = QLabel(subtitle)
        subtitle_label.setStyleSheet(f"""
            font-size: 12px; color: {GRAY_TEXT_COLOR}; border: none;
            background: transparent;
        """)
        text_col_layout.addWidget(subtitle_label)
        layout.addWidget(text_col, 1)

        # Time Label
        time_label = QLabel(time_text)
        time_label.setAlignment(
            Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter
        )
        time_label.setStyleSheet(f"""
            font-size: 12px; color: {GRAY_TEXT_COLOR};
            border: none; background: transparent;
        """)
        layout.addWidget(time_label)
