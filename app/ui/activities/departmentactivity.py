from typing import Callable
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtWidgets import (
    QCheckBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QScrollArea,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)

from app.ui.components.activity import Activity
# Importing shared components from device activity
from app.ui.activities.deviceactivity import FlowLayout, ToolbarButton


class DepartmentCard(QWidget):
    """Custom widget representing a single department."""
    def __init__(self, name: str, start_time: str, off_time: str, working_days: str, parent=None):
        super().__init__(parent)
        self.setMinimumWidth(250)
        self.setMaximumWidth(300)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        
        self.setStyleSheet("""
            DepartmentCard {
                background-color: #ffffff;
                border: 1px solid #d9d9d9;
            }
        """)
        
        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(5)

        # --- Top Row: Checkbox and Department Name ---
        top_row = QHBoxLayout()
        top_row.setSpacing(5)
        
        checkbox = QCheckBox()
        checkbox.setStyleSheet("border: none; background: transparent;")
        top_row.addWidget(checkbox)
        
        name_label = QLabel(name)
        name_label.setStyleSheet("font-size: 14px; font-weight: bold; color: #000000; border: none; background: transparent;")
        top_row.addWidget(name_label)
        top_row.addStretch()
        
        layout.addLayout(top_row)

        # --- Bottom Row: Image and Details ---
        bottom_row = QHBoxLayout()
        bottom_row.setSpacing(10)

        # Icon Placeholder
        icon_label = QLabel()
        pixmap = QPixmap("assets/icon.jpg")
        if not pixmap.isNull():
            icon_label.setPixmap(pixmap.scaled(
                45, 45, 
                Qt.AspectRatioMode.KeepAspectRatio, 
                Qt.TransformationMode.SmoothTransformation
            ))
        icon_label.setFixedSize(45, 45)
        icon_label.setStyleSheet("border: none; background: transparent;")
        bottom_row.addWidget(icon_label)

        # Details Layout
        details_layout = QVBoxLayout()
        details_layout.setSpacing(2)
        details_layout.setAlignment(Qt.AlignmentFlag.AlignVCenter)

        start_lbl = QLabel(f"Start: {start_time}")
        start_lbl.setStyleSheet("font-size: 12px; color: #000000; border: none; background: transparent;")
        
        off_lbl = QLabel(f"Off: {off_time}")
        off_lbl.setStyleSheet("font-size: 12px; color: #000000; border: none; background: transparent;")
        
        days_lbl = QLabel(f"Working Days: {working_days}")
        days_lbl.setStyleSheet("font-size: 12px; color: #000000; border: none; background: transparent;")

        details_layout.addWidget(start_lbl)
        details_layout.addWidget(off_lbl)
        details_layout.addWidget(days_lbl)
        
        bottom_row.addLayout(details_layout)
        bottom_row.addStretch()
        
        layout.addLayout(bottom_row)


class WorkingDaysWidget(QWidget):
    """Custom widget for circular day toggle buttons."""
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(5)

        days = ["M", "T", "W", "T", "F", "S", "S"]
        for day in days:
            btn = QPushButton(day)
            btn.setCheckable(True)
            btn.setFixedSize(24, 24)
            btn.setStyleSheet("""
                QPushButton {
                    border-radius: 12px;
                    background-color: #f0f0f0;
                    color: #878787;
                    border: 1px solid #d9d9d9;
                    font-size: 11px;
                    font-weight: bold;
                }
                QPushButton:checked {
                    background-color: #21679A;
                    color: #ffffff;
                    border: 1px solid #21679A;
                }
            """)
            layout.addWidget(btn)
        
        layout.addStretch()


class DepartmentFormSidebar(QWidget):
    """Right sidebar for adding/editing a department."""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedWidth(275)
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)

        self.setStyleSheet("""
            DepartmentFormSidebar {
                background-color: #ffffff;
                border: 1px solid #d9d9d9;
            }
        """)
        
        # Main layout for the Sidebar
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # Scroll Area
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        scroll_area.setStyleSheet("QScrollArea { border: none; background-color: transparent; }")

        # Content Widget
        content_widget = QWidget()
        content_widget.setStyleSheet("background-color: transparent;")
        
        layout = QVBoxLayout(content_widget)
        layout.setContentsMargins(15, 15, 15, 15)
        layout.setSpacing(10)

        # Header
        title = QLabel("Add Department")
        title.setStyleSheet("font-size: 18px; font-weight: bold; border: none; background: transparent;")
        layout.addWidget(title)

        # Helper function to create form fields
        def add_field(label_text: str, placeholder: str) -> QLineEdit:
            lbl = QLabel(label_text)
            lbl.setStyleSheet("font-size: 12px; font-weight: bold; border: none; background: transparent;")
            inp = QLineEdit()
            inp.setPlaceholderText(placeholder)
            inp.setFixedHeight(32)
            inp.setStyleSheet("""
                QLineEdit {
                    border: 1px solid #d9d9d9;
                    padding: 0 8px;
                    font-size: 12px;
                    background-color: #ffffff;
                    color: #000000;
                }
                QLineEdit:focus {
                    border: 1px solid #21679A;
                }
            """)
            layout.addWidget(lbl)
            layout.addWidget(inp)
            return inp

        # Form Fields
        self.name_input = add_field("Department Name", "e.g. Accounts")
        
        # Start and Off Time Row
        time_layout = QHBoxLayout()
        time_layout.setSpacing(10)
        
        # Start Time
        start_col = QVBoxLayout()
        start_lbl = QLabel("Start Time")
        start_lbl.setStyleSheet("font-size: 12px; font-weight: bold; border: none; background: transparent;")
        self.start_input = QLineEdit()
        self.start_input.setPlaceholderText("9:00 AM")
        self.start_input.setFixedHeight(32)
        self.start_input.setStyleSheet("QLineEdit { border: 1px solid #d9d9d9; padding: 0 8px; font-size: 12px; }")
        start_col.addWidget(start_lbl)
        start_col.addWidget(self.start_input)

        # Off Time
        off_col = QVBoxLayout()
        off_lbl = QLabel("Off Time")
        off_lbl.setStyleSheet("font-size: 12px; font-weight: bold; border: none; background: transparent;")
        self.off_input = QLineEdit()
        self.off_input.setPlaceholderText("5:00 PM")
        self.off_input.setFixedHeight(32)
        self.off_input.setStyleSheet("QLineEdit { border: 1px solid #d9d9d9; padding: 0 8px; font-size: 12px; }")
        off_col.addWidget(off_lbl)
        off_col.addWidget(self.off_input)

        time_layout.addLayout(start_col)
        time_layout.addLayout(off_col)
        layout.addLayout(time_layout)

        # Working Days
        days_lbl = QLabel("Working Days")
        days_lbl.setStyleSheet("font-size: 12px; font-weight: bold; border: none; background: transparent;")
        layout.addWidget(days_lbl)
        
        self.working_days_widget = WorkingDaysWidget()
        layout.addWidget(self.working_days_widget)

        layout.addStretch()

        # Save Button
        save_btn = QPushButton("Save Department")
        save_btn.setFixedHeight(36)
        save_btn.setStyleSheet("""
            QPushButton {
                background-color: #21679A;
                color: #ffffff;
                border: none;
                font-size: 13px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #1a527c;
            }
        """)
        layout.addWidget(save_btn)

        scroll_area.setWidget(content_widget)
        main_layout.addWidget(scroll_area)


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

        # Dummy Data
        departments = [
            ("Teacher", "8:00 am", "4:00 pm", "M,T,W,T,F"),
            ("Students", "8:00 am", "2:00 pm", "M,T,W,T,F"),
            ("Accountant", "9:00 am", "5:00 pm", "M,T,W,T,F"),
        ]

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