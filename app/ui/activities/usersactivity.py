from typing import Callable
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QHBoxLayout,
    QScrollArea,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)
from app.ui.components.activity import Activity
from app.ui.components.flowlayout import FlowLayout
from app.ui.components.toolbarbutton import ToolbarButton
from app.ui.components.usercard import UserCard
from app.ui.components.userformsidebar import UserFormSidebar
from data.users import users

class UsersActivity(Activity):
    """
    ### Users Activity
    This widget renders the user management page with action buttons, a scrollable user card grid, and a side form for creating or editing employee profiles.
    """

    def __init__(self, navigate: Callable, parent=None) -> None:
        """
        Initialize the Users Page Activity.

        This method creates the toolbar, user card list, and the right-side form sidebar used to manage user information.
        """
        super().__init__(
            parent=parent, activity="Users", navigate=navigate
        )

        # 1. Main Layout
        # This creates the vertical structure for the users screen, placing the toolbar above the user cards and sidebar.
        main_layout = QVBoxLayout(self.content)
        main_layout.setContentsMargins(0, 30, 0, 0)
        main_layout.setSpacing(20)

        # 2. TOOLBAR
        toolbar_widget = QWidget()
        toolbar_widget.setStyleSheet("background: transparent;")
        toolbar_widget.setSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed
        )
        toolbar_layout = FlowLayout(
            toolbar_widget, margin=0, h_spacing=10, v_spacing=10
        )
        buttons = [
            ("Add", "assets/add.png"),
            ("Edit", "assets/edit.png"),
            ("Delete", "assets/delete.png"),
            ("Download", "assets/download.png"),
            ("Upload", "assets/upload.png"),
        ]
        for text, icon in buttons:
            toolbar_layout.addWidget(ToolbarButton(text, icon))
        main_layout.addWidget(toolbar_widget)

        # BOTTOM: SPLIT LAYOUT (Cards Left, Sidebar Right)
        content_split_layout = QHBoxLayout()
        content_split_layout.setSpacing(20)

        # LEFT PANE: Scrollable Cards
        left_pane = QWidget()
        left_pane.setStyleSheet("background: transparent;")
        left_layout = QVBoxLayout(left_pane)
        left_layout.setContentsMargins(0, 0, 0, 0)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setHorizontalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff
        )
        scroll_area.setStyleSheet("""
            QScrollArea {
                border: none; background: transparent;
            }
        """)
        scroll_content = QWidget()
        scroll_content.setStyleSheet("background: transparent;")
        self.cards_layout = FlowLayout(
            scroll_content, margin=0, h_spacing=15, v_spacing=15
        )
        for name, dept in users:
            card = UserCard(name, dept)
            self.cards_layout.addWidget(card)

        scroll_area.setWidget(scroll_content)
        left_layout.addWidget(scroll_area)

        # RIGHT PANE: User Form Sidebar
        right_pane = UserFormSidebar()

        # Add both panes to the split layout
        content_split_layout.addWidget(left_pane, 1)
        content_split_layout.addWidget(right_pane)
        main_layout.addLayout(content_split_layout, 1)
