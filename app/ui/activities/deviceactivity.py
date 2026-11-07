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
from app.ui.components.devicecard import DeviceCard
from app.ui.components.deviceformsidebar import DeviceFormSidebar
from data.devices import devices

class DeviceActivity(Activity):
    """
    ### Device Activity
    This widget displays the device management page with action buttons, a scrollable device card list, and a fixed side form for managing device details.
    """

    def __init__(self, navigate: Callable, parent=None) -> None:
        """
        Initialize the device page activity.

        This method sets up the toolbar actions, device card grid, and the right-side form sidebar used for device records.
        """
        super().__init__(parent=parent, activity="Device", navigate=navigate)

        # 1. Main Layout
        # This builds the main vertical layout used to stack the toolbar and the split content area for the device page.
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
            ("Add", "assets/add.png"), ("Edit", "assets/edit.png"),
            ("Delete", "assets/delete.png"), ("Ping", "assets/signal.png"),
            ("Sync Time", "assets/signal.png"),
            ("Download Users", "assets/download.png"),
            ("Download Logs", "assets/download.png"),
        ]
        for text, icon in buttons:
            toolbar_layout.addWidget(ToolbarButton(text, icon))
        main_layout.addWidget(toolbar_widget)

        # 3. BOTTOM: SPLIT LAYOUT (Cards Left, Sidebar Right)
        content_split_layout = QHBoxLayout()
        content_split_layout.setSpacing(20)

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
            scroll_content, margin=0, h_spacing=20, v_spacing=20
        )
        for dev in devices:
            card = DeviceCard(*dev)
            self.cards_layout.addWidget(card)

        scroll_area.setWidget(scroll_content)
        left_layout.addWidget(scroll_area)

        # 5. RIGHT PANE: Device Form Sidebar
        right_pane = DeviceFormSidebar()

        # 6. Add both panes to the split layout
        content_split_layout.addWidget(left_pane, 1)
        content_split_layout.addWidget(right_pane)
        main_layout.addLayout(content_split_layout, 1)
