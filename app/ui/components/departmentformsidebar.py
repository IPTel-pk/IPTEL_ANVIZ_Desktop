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
    """
    ### DepartmentFormSidebar
    This widget provides the right-side form used to add or edit department details such as name, schedule, and working days.
    """

    def __init__(self, parent=None):
        """
        Initialize the department form sidebar.

        This method styles the sidebar and builds the scrollable form with name, time, working-day, and save controls.
        """
        super().__init__(parent)
        self.setFixedWidth(275)
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setStyleSheet(f"""
            DepartmentFormSidebar {{
                background-color: #ffffff;
                border: 1px solid {SECONDARY_COLOR};
            }}
        """)

        # 1. Create the main vertical layout for the sidebar
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # 2. Add a scroll area so the form fits smaller screens
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

        # 3. Create the content widget that holds the form fields
        content_widget = QWidget()
        content_widget.setStyleSheet("background-color: transparent;")
        
        layout = QVBoxLayout(content_widget)
        layout.setContentsMargins(15, 15, 15, 15)
        layout.setSpacing(10)

        # 4. Add the form title
        title = QLabel("Add Department")
        title.setStyleSheet("""
            font-size: 18px; font-weight: bold;
            border: none; background: transparent;
        """)
        layout.addWidget(title)

        # 5. Add the department name field
        self.name_input = InputField("Department Name", "e.g. Accounts")
        layout.addWidget(self.name_input)
        
        # 6. Add the start and off time fields side by side
        time_layout = QHBoxLayout()
        time_layout.setSpacing(10)

        self.start_input = InputField("Start Time", "9:00 AM")
        self.off_input = InputField("Off Time", "5:00 PM")

        time_layout.addWidget(self.start_input)
        time_layout.addWidget(self.off_input)
        layout.addLayout(time_layout)

        # 7. Add the working days section
        days_lbl = QLabel("Working Days")
        days_lbl.setStyleSheet("""
            font-size: 12px; font-weight: bold;
            border: none; background: transparent;
        """)
        layout.addWidget(days_lbl)

        self.working_days_widget = WorkingDaysWidget()
        layout.addWidget(self.working_days_widget)
        layout.addStretch()

        # 8. Add the save button at the bottom of the sidebar
        save_btn = PrimaryButton("Save Department")
        save_btn.clicked.connect(self._on_save_clicked)
        layout.addWidget(save_btn)

        scroll_area.setWidget(content_widget)
        main_layout.addWidget(scroll_area)

    def _on_save_clicked(self):
        """
        Save the department form data.

        This placeholder method collects the current form entries and can be replaced with a database or API call later.
        """
        department_data = self.get_data()
        print("Saving Department:", department_data)

    def get_data(self) -> dict:
        """
        Gather the currently entered department information.

        This method returns the field values in a dictionary format for saving or validation logic.
        """
        return {
            "name": self.name_input.text(),
            "start_time": self.start_input.text(),
            "off_time": self.off_input.text(),
        }
