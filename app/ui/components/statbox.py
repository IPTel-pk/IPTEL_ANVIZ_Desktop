from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QLabel,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)
from app.settings import SECONDARY_COLOR, GRAY_TEXT_COLOR

class StatBox(QWidget):
    """
    ### StatBox
    This widget displays a dashboard metric with a large numeric value and a smaller label beneath it.
    """

    def __init__(self, value: str, label: str, parent=None):
        """
        Initialize the summary stat box.

        This method creates the card style and arranges the numeric metric and label in a vertical stack.
        """
        super().__init__(parent)
        self.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed
        )

        # 1. Create the outer layout for the stat box
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # 2. Build the inner white card that holds the metric content
        container = QWidget()
        container.setObjectName("statBoxContainer")
        container.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        container.setStyleSheet(f"""
            QWidget#statBoxContainer {{
                background-color: #ffffff;
                border: 1px solid {SECONDARY_COLOR};
            }}
        """)

        layout = QVBoxLayout(container)
        layout.setContentsMargins(16, 10, 16, 10)
        layout.setSpacing(2)

        # 3. Add the large metric value
        value_label = QLabel(value)
        value_label.setStyleSheet("""
            font-size: 28px; font-weight: 600; color: #000000;
            border: none; background: transparent;
        """)
        layout.addWidget(value_label)

        # 4. Add the label beneath the numeric value
        title_label = QLabel(label)
        title_label.setStyleSheet(f"""
            font-size: 12px; color: {GRAY_TEXT_COLOR};
            border: none; background: transparent;
        """)
        layout.addWidget(title_label)
        main_layout.addWidget(container)
