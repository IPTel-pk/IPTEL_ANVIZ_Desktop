from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QLabel,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)

class StatBox(QWidget):
    def __init__(self, value: str, label: str, parent=None):
        super().__init__(parent)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)

        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        container = QWidget()
        container.setObjectName("statBoxContainer")
        container.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        
        # Removed border-radius for sharp edges
        container.setStyleSheet("""
            QWidget#statBoxContainer {
                background-color: #ffffff;
                border: 1px solid #d9d9d9;
            }
        """)

        layout = QVBoxLayout(container)
        layout.setContentsMargins(16, 10, 16, 10)
        layout.setSpacing(2)

        value_label = QLabel(value)
        value_label.setStyleSheet("font-size: 28px; font-weight: 600; color: #000000; border: none; background: transparent;")
        layout.addWidget(value_label)

        title_label = QLabel(label)
        title_label.setStyleSheet("font-size: 12px; color: #878787; border: none; background: transparent;")
        layout.addWidget(title_label)

        main_layout.addWidget(container)
