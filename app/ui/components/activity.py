from typing import Callable
from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel
from PySide6.QtCore import Qt
from app.ui.components.aside import Aside
from app.ui.components.header import Header
from app.settings import VERSION, HIGHLIGHT_COLOR

class Activity(QWidget):
    """
    ### Activity
    This widget provides the shared base layout used by all application screens, including the left navigation, page header, content area, and footer.
    """

    def __init__(
        self, parent=None, activity:str="",
        navigate:Callable=lambda:print("No event set!")
    ) -> None:
        """
        Initialize the shared activity shell.

        This method creates the app frame, side menu, header, and dynamic content panel used by every activity page.
        """
        super().__init__(parent=parent)
        self.setStyleSheet(F"background-color: {HIGHLIGHT_COLOR};")
        self.setAutoFillBackground(True)

        # 1. Build the horizontal root layout
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        # 2. Add the left sidebar navigation
        aside = Aside(self, activity, navigate)
        layout.addWidget(aside)

        # 3. Create the main content panel
        main = QWidget(self)
        main.setAutoFillBackground(True)
        main.setStyleSheet(F"background-color: {HIGHLIGHT_COLOR};")
        main_layout = QVBoxLayout(main)
        main_layout.setContentsMargins(30, 30, 30, 0)
        main_layout.setSpacing(0)

        # 4. Add the top page header
        header = Header(activity)
        main_layout.addWidget(header)

        # 5. Add the dynamic activity content container
        self.content = QWidget(main)
        main_layout.addWidget(self.content, 1)

        # 6. Add the footer label with the version text
        footer = QLabel(VERSION)
        footer.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(footer)

        # 7. Attach the main area to the root layout
        layout.addWidget(main, 1)
