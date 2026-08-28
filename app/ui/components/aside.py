from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QWidget, QVBoxLayout, QSizePolicy
from app.ui.components.asidebutton import AsideButton
from app.settings import ACTIVITIES

class Aside(QWidget):
    """**Aside Menu Bar**"""
    def __init__(self, parent, activity:str="") -> None:
        """Initialize the Side Bar Menu of the activity"""
        super().__init__(parent)
        self.setAutoFillBackground(True)
        self.setStyleSheet("background-color: #2c3e50;")
        self.setFixedWidth(260)
        self.content_layout = QVBoxLayout(self)
        self.content_layout.setContentsMargins(0, 0, 0, 0)
        self.content_layout.setSpacing(0)

        branding_widget = QWidget(self)
        branding_widget.setStyleSheet("background-color: #ffffff;")
        branding_widget.setFixedHeight(140)

        branding_layout = QVBoxLayout(branding_widget)
        branding_layout.setContentsMargins(0, 0, 0, 0)
        branding_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        logo_label = QLabel(branding_widget)
        logo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        logo_label.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        logo_label.setFixedSize(185, 80)

        pixmap = QPixmap("assets/iptel.png")
        if not pixmap.isNull():
            logo_label.setPixmap(
                pixmap.scaled(
                    185,
                    80,
                    Qt.AspectRatioMode.KeepAspectRatio,
                    Qt.TransformationMode.SmoothTransformation,
                )
            )

        branding_layout.addWidget(logo_label)
        self.content_layout.addWidget(branding_widget)

        menu_widget = QWidget(self)
        menu_layout = QVBoxLayout(menu_widget)
        menu_layout.setContentsMargins(0, 0, 0, 0)
        menu_layout.setSpacing(0)
        for item in ACTIVITIES:
            btn = AsideButton(item, item==activity)
            menu_layout.addWidget(btn)

        menu_layout.addWidget(QWidget(), 1)

        self.content_layout.addWidget(menu_widget, 1)