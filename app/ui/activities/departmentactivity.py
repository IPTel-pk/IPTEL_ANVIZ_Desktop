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
    """**Department Page**"""
    def __init__(self, navigate: Callable, parent=None) -> None:
        """Initialize the Department Page Activity"""
        super().__init__(parent=parent, activity="Department", navigate=navigate)

        # 1. Main layout is Vertical (Toolbar on top, Content below)
        main_layout = QVBoxLayout(self.content)
        main_layout.setContentsMargins(0, 30, 0, 0)
        main_layout.setSpacing(20)

        # ==========================================
        # TOP: TOOLBAR
        # ==========================================
        toolbar_widget = QWidget()
        toolbar_widget.setStyleSheet("background: transparent;")
        toolbar_widget.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        
        toolbar_layout = FlowLayout(toolbar_widget, margin=0, h_spacing=10, v_spacing=10)
        
        buttons = [
            ("Add", "assets/icon.jpg"),
            ("Edit", "assets/icon.jpg"),
            ("Delete", "assets/icon.jpg"),
        ]
        
        for text, icon in buttons:
            toolbar_layout.addWidget(ToolbarButton(text, icon))
            
        main_layout.addWidget(toolbar_widget)

        # ==========================================
        # BOTTOM: SPLIT LAYOUT (Cards Left, Sidebar Right)
        # ==========================================
        content_split_layout = QHBoxLayout()
        content_split_layout.setSpacing(20)

        # --- LEFT PANE: Scrollable Cards ---
        left_pane = QWidget()
        left_pane.setStyleSheet("background: transparent;")
        left_layout = QVBoxLayout(left_pane)
        left_layout.setContentsMargins(0, 0, 0, 0)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        scroll_area.setStyleSheet("QScrollArea { border: none; background: transparent; }")
        
        scroll_content = QWidget()
        scroll_content.setStyleSheet("background: transparent;")
        
        self.cards_layout = FlowLayout(scroll_content, margin=0, h_spacing=15, v_spacing=15)

        for name, start, off, days in departments:
            card = DepartmentCard(name, start, off, days)
            self.cards_layout.addWidget(card)

        scroll_area.setWidget(scroll_content)
        left_layout.addWidget(scroll_area)

        # --- RIGHT PANE: Department Form Sidebar ---
        right_pane = DepartmentFormSidebar()

        # Add both panes to the split layout
        content_split_layout.addWidget(left_pane, 1) # Left pane expands
        content_split_layout.addWidget(right_pane)   # Right pane fixed width

        # Pass `1` as the stretch factor to take all extra vertical space
        main_layout.addLayout(content_split_layout, 1)