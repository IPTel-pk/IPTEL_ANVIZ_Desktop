from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QLabel,
    QScrollArea,
    QVBoxLayout,
    QWidget,
)
from app.ui.components.inputfield import InputField
from app.ui.components.selectfield import SelectField
from app.ui.components.primarybutton import PrimaryButton
from app.settings import SECONDARY_COLOR

class UserFormSidebar(QWidget):
    """
    ### UserFormSidebar
    This widget creates the right-side form used for adding or editing user records with their department and access details.
    """

    def __init__(self, parent=None):
        """
        Initialize the user form sidebar.

        This method builds the scrollable user form and adds the field set needed to capture user information.
        """
        super().__init__(parent)
        self.setFixedWidth(275)
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setStyleSheet(f"""
            UserFormSidebar {{
                background-color: #ffffff;
                border: 1px solid {SECONDARY_COLOR};
            }}
        """)

        # 1. Create the main layout for the sidebar
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # 2. Add a scroll area for the form content
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

        # 3. Create the content widget that holds the fields
        content_widget = QWidget()
        content_widget.setStyleSheet("background-color: transparent;")

        layout = QVBoxLayout(content_widget)
        layout.setContentsMargins(15, 15, 15, 15)
        layout.setSpacing(10)

        # 4. Add the form title
        title = QLabel("Add User")
        title.setStyleSheet("""
            font-size: 18px; font-weight: bold;
            border: none; background: transparent;
        """)
        layout.addWidget(title)

        # 5. Add the user identification and core details
        self.id_input = InputField("ID", "Auto-generated if empty")
        layout.addWidget(self.id_input)

        self.name_input = InputField("Name", "Enter full name")
        layout.addWidget(self.name_input)

        self.dept_combo = SelectField(
            "Department", [
                "Select department", "Teachers",
                "Student", "Engineering", "HR"
            ]
        )
        layout.addWidget(self.dept_combo)

        self.password_input = InputField(
            "Password", "Enter password", hidden=True
        )
        layout.addWidget(self.password_input)

        self.rfid_input = InputField("RFID", "Scan or enter RFID tag")
        layout.addWidget(self.rfid_input)

        self.type_combo = SelectField(
            "Type", [
                "Select user type", "Normal", "Admin"
            ]
        )
        layout.addWidget(self.type_combo)

        layout.addStretch()

        # 6. Add the save button at the bottom
        save_btn = PrimaryButton("Save User")
        save_btn.clicked.connect(self._on_save_clicked)
        layout.addWidget(save_btn)

        # 7. Finalize the scroll area layout
        scroll_area.setWidget(content_widget)
        main_layout.addWidget(scroll_area)

    def _on_save_clicked(self):
        """
        Save the user form data.

        This placeholder method is where validation and persistence logic can later be added.
        """
        user_data = self.get_data()
        print("Saving User:", user_data)

    def get_data(self) -> dict:
        """
        Gather all current user form values.

        This method returns a dictionary so the data can be saved, validated, or submitted to a backend.
        """
        return {
            "id": self.id_input.text(),
            "name": self.name_input.text(),
            "department": self.dept_combo.current_text(),
            "password": self.password_input.text(),
            "rfid": self.rfid_input.text(),
            "type": self.type_combo.current_text()
        }
