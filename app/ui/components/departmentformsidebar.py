from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QScrollArea,
    QVBoxLayout,
    QWidget,
)
from app.ui.components.workingdayswidget import WorkingDaysWidget

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
