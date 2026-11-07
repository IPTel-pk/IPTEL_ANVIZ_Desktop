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
    """
    ### ActivityItem
    This widget displays a single recent activity row with an icon, title, subtitle, and time label in the dashboard list.
    """

    def __init__(
        self, title: str, subtitle: str, time_text: str,
        status: str = 'o', parent=None
    ):
        """
        Initialize the recent activity item.

        This method builds the status indicator, text block, and time label used in the dashboard activity feed.
        """
        super().__init__(parent)
        self.setFixedHeight(54)
        self.setStyleSheet("""
            QWidget {
                background-color: transparent; border: none;
            }
        """)

        # 1. Build the main horizontal layout for the activity row
        layout = QHBoxLayout(self)
        layout.setContentsMargins(15, 6, 15, 6)
        layout.setSpacing(12)

        # 2. Map the status code to the matching icon and background color
        status_mapping = {
            'o': ("#d4edda", "assets/ok.png"),      # Ok (Light Green)
            'a': ("#cce5ff", "assets/add.png"),     # Add (Light Blue)
            'e': ("#fff3cd", "assets/edit.png"),    # Edit (Light Yellow)
            'd': ("#f8d7da", "assets/delete.png"),  # Delete (Light Red)
            'i': ("#ffe8cc", "assets/info.png"),    # Info (Light Orange)
        }
        bg_color, icon_path = status_mapping.get(status, status_mapping['o'])

        # 3. Create the circular indicator and color it based on the activity status
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

        # 4. Load and scale the icon image for the indicator
        pixmap = QPixmap(icon_path)
        if not pixmap.isNull():
            scaled_pixmap = pixmap.scaled(
                10, 10,
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            )
            indicator.setPixmap(scaled_pixmap)
        else:
            indicator.setText("?")
        layout.addWidget(indicator, alignment=Qt.AlignmentFlag.AlignVCenter)

        # 5. Create the text column for the title and subtitle
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

        # 6. Add the time text on the right side of the row
        time_label = QLabel(time_text)
        time_label.setAlignment(
            Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter
        )
        time_label.setStyleSheet(f"""
            font-size: 12px; color: {GRAY_TEXT_COLOR};
            border: none; background: transparent;
        """)
        layout.addWidget(time_label)
