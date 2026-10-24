from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)

class ActivityItem(QWidget):
    def __init__(self, title: str, subtitle: str, time_text: str, parent=None):
        super().__init__(parent)
        self.setFixedHeight(54)
        self.setStyleSheet("QWidget { background-color: transparent; border: none; }")

        layout = QHBoxLayout(self)
        layout.setContentsMargins(15, 6, 15, 6)
        layout.setSpacing(12)

        indicator = QLabel()
        indicator.setFixedSize(30, 30)
        # Removed border-radius so the indicator is a sharp square
        indicator.setStyleSheet("background-color: #2d8cff; border: none;")
        layout.addWidget(indicator, alignment=Qt.AlignmentFlag.AlignVCenter)

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

        time_label = QLabel(time_text)
        time_label.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        time_label.setStyleSheet("font-size: 12px; color: #878787; border: none; background: transparent;")
        layout.addWidget(time_label)
