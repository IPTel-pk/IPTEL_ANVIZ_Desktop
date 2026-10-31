from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)


class ActivityItem(QWidget):
    def __init__(self, title: str, subtitle: str, time_text: str, status: str = 'o', parent=None):
        super().__init__(parent)
        self.setFixedHeight(54)
        self.setStyleSheet("QWidget { background-color: transparent; border: none; }")

        layout = QHBoxLayout(self)
        layout.setContentsMargins(15, 6, 15, 6)
        layout.setSpacing(12)

        # --- Status Indicator Mapping ---
        # Dictionary maps status code to: (Background Color, Text Color, Icon)
        status_styles = {
            'o': ("#d4edda", "#155724", "✔"),  # Ok (Light Green / Dark Green)
            'a': ("#cce5ff", "#004085", "+"),  # Add (Light Blue / Dark Blue)
            'e': ("#fff3cd", "#856404", "✎"),  # Edit (Light Yellow / Dark Yellow)
            'd': ("#f8d7da", "#721c24", "✕"),  # Delete (Light Red / Dark Red)
            'i': ("#ffe8cc", "#d9480f", "!"),  # Info (Light Orange / Dark Orange)
        }
        
        # Fallback to 'o' if an invalid status code is passed
        bg_color, text_color, icon_text = status_styles.get(status, status_styles['o'])

        indicator = QLabel(icon_text)
        indicator.setFixedSize(30, 30)
        indicator.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # Using 15px border-radius to make a 30x30 box a perfect circle
        indicator.setStyleSheet(f"""
            QLabel {{
                background-color: {bg_color};
                color: {text_color};
                border: none;
                border-radius: 15px;
                font-size: 16px;
                font-weight: bold;
            }}
        """)
        layout.addWidget(indicator, alignment=Qt.AlignmentFlag.AlignVCenter)

        # --- Text Layout ---
        text_col = QWidget()
        text_col.setStyleSheet("background: transparent; border: none;")
        text_col.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        text_col_layout = QVBoxLayout(text_col)
        text_col_layout.setContentsMargins(0, 0, 0, 0)
        text_col_layout.setSpacing(0)

        title_label = QLabel(title)
        title_label.setStyleSheet("font-size: 16px; color: #000000; border: none; background: transparent;")
        text_col_layout.addWidget(title_label)

        subtitle_label = QLabel(subtitle)
        subtitle_label.setStyleSheet("font-size: 12px; color: #878787; border: none; background: transparent;")
        text_col_layout.addWidget(subtitle_label)

        layout.addWidget(text_col, 1)

        # --- Time Label ---
        time_label = QLabel(time_text)
        time_label.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        time_label.setStyleSheet("font-size: 12px; color: #878787; border: none; background: transparent;")
        layout.addWidget(time_label)
