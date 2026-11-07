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
from app.ui.components.departmentformsidebar import DepartmentFormSidebar
from app.ui.components.departmentcard import DepartmentCard
from app.ui.components.flowlayout import FlowLayout
from app.ui.components.toolbarbutton import ToolbarButton
from data.departments import departments

class DepartmentActivity(Activity):
    """
    ### Department Activity
    This widget renders the department management screen with action buttons, a scrollable department card grid, and a side form for editing department details.
    """

    def __init__(self, navigate: Callable, parent=None) -> None:
        """
        Initialize the department page activity.

        This method builds the toolbar, the card-based department list, and the split layout containing the sidebar form.
        """
        super().__init__(
            parent=parent, activity="Department", navigate=navigate
        )

        # 1. Main Layout
        # This creates the vertical structure for the department screen, keeping the toolbar above the main content area.
        main_layout = QVBoxLayout(self.content)
        main_layout.setContentsMargins(0, 30, 0, 0)
        main_layout.setSpacing(20)

        # 2. TOOL BAR
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
        ]
        for text, icon in buttons:
            toolbar_layout.addWidget(ToolbarButton(text, icon))
        main_layout.addWidget(toolbar_widget)

        # 3. BOTTOM: SPLIT LAYOUT (Cards Left, Sidebar Right)
        content_split_layout = QHBoxLayout()
        content_split_layout.setSpacing(30)

        # 4. LEFT PANE: Scrollable Cards
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
        for name, start, off, days in departments:
            card = DepartmentCard(name, start, off, days)
            self.cards_layout.addWidget(card)
        scroll_area.setWidget(scroll_content)
        left_layout.addWidget(scroll_area)

        # 5. RIGHT PANE: Department Form Sidebar
        right_pane = DepartmentFormSidebar()

        # 6. Add both panes to the split layout
        content_split_layout.addWidget(left_pane, 1)
        content_split_layout.addWidget(right_pane)
        main_layout.addLayout(content_split_layout, 1)
