from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QScrollArea,
    QVBoxLayout,
    QWidget,
)
from app.ui.components.inputfield import InputField
from app.ui.components.primarybutton import PrimaryButton
from app.ui.components.workingdayswidget import WorkingDaysWidget
from app.settings import SECONDARY_COLOR

class DepartmentFormSidebar(QWidget):
    """Right sidebar for adding/editing a department."""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedWidth(275)
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setStyleSheet(f"""
            DepartmentFormSidebar {{
                background-color: #ffffff;
                border: 1px solid {SECONDARY_COLOR};
            }}
        """)

        # Main layout for the Sidebar
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # Scroll Area
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setHorizontalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff
        )
        scroll_area.setStyleSheet("""
            QScrollArea {
                border: none; background-color: transparent;
            }
        """)

        # Content Widget
        content_widget = QWidget()
        content_widget.setStyleSheet("background-color: transparent;")
        
        layout = QVBoxLayout(content_widget)
        layout.setContentsMargins(15, 15, 15, 15)
        layout.setSpacing(10)

        # Header
        title = QLabel("Add Department")
        title.setStyleSheet("""
            font-size: 18px; font-weight: bold;
            border: none; background: transparent;
        """)
        layout.addWidget(title)

        # Form Fields using Custom Components
        self.name_input = InputField("Department Name", "e.g. Accounts")
        layout.addWidget(self.name_input)
        
        # Start and Off Time Row (Side-by-side)
        time_layout = QHBoxLayout()
        time_layout.setSpacing(10)

        self.start_input = InputField("Start Time", "9:00 AM")
        self.off_input = InputField("Off Time", "5:00 PM")

        time_layout.addWidget(self.start_input)
        time_layout.addWidget(self.off_input)
        layout.addLayout(time_layout)

        # Working Days
        days_lbl = QLabel("Working Days")
        days_lbl.setStyleSheet("""
            font-size: 12px; font-weight: bold;
            border: none; background: transparent;
        """)
        layout.addWidget(days_lbl)

        self.working_days_widget = WorkingDaysWidget()
        layout.addWidget(self.working_days_widget)
        layout.addStretch()

        # Save Button
        save_btn = PrimaryButton("Save Department")
        save_btn.clicked.connect(self._on_save_clicked)
        layout.addWidget(save_btn)

        scroll_area.setWidget(content_widget)
        main_layout.addWidget(scroll_area)

    def _on_save_clicked(self):
        """Placeholder for your save logic."""
        department_data = self.get_data()
        print("Saving Department:", department_data)
        # Here you would typically emit a signal or call a database function

    def get_data(self) -> dict:
        """Helper method to extract all form data at once."""
        return {
            "name": self.name_input.text(),
            "start_time": self.start_input.text(),
            "off_time": self.off_input.text(),
        }
