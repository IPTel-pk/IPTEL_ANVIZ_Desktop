from typing import Callable
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QWidget, QVBoxLayout, QSizePolicy
from app.ui.components.asidebutton import AsideButton
from app.settings import ACTIVITIES, ACCENT_COLOR

class Aside(QWidget):
    """
    ### Aside
    This widget creates the left navigation menu for switching between app sections and displays the brand header at the top.
    """

    def __init__(self, parent, activity:str, navigate:Callable) -> None:
        """
        Initialize the sidebar menu.

        This method creates the branding area and builds the list of navigation buttons for each activity in the app.
        """
        super().__init__(parent)
        self.setAutoFillBackground(True)
        self.setStyleSheet(f"background-color: {ACCENT_COLOR};")
        self.setFixedWidth(260)
        self.content_layout = QVBoxLayout(self)
        self.content_layout.setContentsMargins(0, 0, 0, 0)
        self.content_layout.setSpacing(0)

        # 1. Build the branding area at the top of the sidebar
        branding_widget = QWidget(self)
        branding_widget.setStyleSheet("background-color: #ffffff;")
        branding_widget.setFixedHeight(140)

        branding_layout = QVBoxLayout(branding_widget)
        branding_layout.setContentsMargins(0, 0, 0, 0)
        branding_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        logo_label = QLabel(branding_widget)
        logo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        logo_label.setSizePolicy(
            QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed
        )
        logo_label.setFixedSize(185, 80)

        pixmap = QPixmap("assets/iptel.png")
        if not pixmap.isNull():
            logo_label.setPixmap(pixmap.scaled(
                185,
                80,
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation,
            ))
        branding_layout.addWidget(logo_label)
        self.content_layout.addWidget(branding_widget)

        # 2. Build the activity list in the menu area
        menu_widget = QWidget(self)
        menu_layout = QVBoxLayout(menu_widget)
        menu_layout.setContentsMargins(0, 0, 0, 0)
        menu_layout.setSpacing(0)
        for item in ACTIVITIES:
            btn = AsideButton(
                text=item,
                navigate=lambda checked=False, current=item: navigate(current),
                active=item==activity,
            )
            menu_layout.addWidget(btn)
        menu_layout.addWidget(QWidget(), 1)
        self.content_layout.addWidget(menu_widget, 1)
