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

class UserFormSidebar(QWidget):
    """Right sidebar for adding/editing a user."""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedWidth(275)
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)

        self.setStyleSheet("""
            UserFormSidebar {
                background-color: #ffffff;
                border: 1px solid #d9d9d9;
            }
        """)
        
        # FIX: We need a main layout to force the scroll area to fill the widget
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0) # Zero margins
        main_layout.setSpacing(0)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        scroll_area.setStyleSheet("QScrollArea { border: none; background-color: transparent; }")

        content_widget = QWidget()
        content_widget.setStyleSheet("background-color: transparent;")
        
        layout = QVBoxLayout(content_widget)
        layout.setContentsMargins(15, 15, 15, 15)
        layout.setSpacing(10)

        # Header
        title = QLabel("Add User")
        title.setStyleSheet("font-size: 18px; font-weight: bold; border: none; background: transparent;")
        layout.addWidget(title)

        # Form Fields
        self.id_input = InputField("ID", "Auto-generated if empty")
        layout.addWidget(self.id_input)
        
        self.name_input = InputField("Name", "Enter full name")
        layout.addWidget(self.name_input)
        
        self.dept_combo = SelectField("Department", ["Select department", "Teachers", "Student", "Engineering", "HR"])
        layout.addWidget(self.dept_combo)

        self.password_input = InputField("Password", "Enter password", hidden=True)
        layout.addWidget(self.password_input)

        self.rfid_input = InputField("RFID", "Scan or enter RFID tag")
        layout.addWidget(self.rfid_input)

        self.type_combo = SelectField("Type", ["Select user type", "Normal", "Admin"])
        layout.addWidget(self.type_combo)

        layout.addStretch()

        # Save Button
        save_btn = PrimaryButton("Save User")
        save_btn.clicked.connect(self._on_save_clicked)
        layout.addWidget(save_btn)

        # Finalize layout
        scroll_area.setWidget(content_widget)
        main_layout.addWidget(scroll_area)

    def _on_save_clicked(self):
        """Placeholder for your save logic."""
        # Example of how to get the data:
        user_data = self.get_data()
        print("Saving User:", user_data)
        # Here you would typically emit a signal or call a database function

    def get_data(self) -> dict:
        """Helper method to extract all form data at once."""
        return {
            "id": self.id_input.text(),
            "name": self.name_input.text(),
            "department": self.dept_combo.current_text(),
            "password": self.password_input.text(),
            "rfid": self.rfid_input.text(),
            "type": self.type_combo.current_text()
        }