from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QComboBox,
    QLabel,
    QLineEdit,
    QPushButton,
    QScrollArea,
    QVBoxLayout,
    QWidget,
)

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
        title = QLabel("Add User")
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
        # ID field is now writable and uses the default input styling
        self.id_input = add_field("ID", "Auto-generated if empty")
        
        self.name_input = add_field("Name", "Enter full name")
        
        # Department ComboBox
        dept_lbl = QLabel("Department")
        dept_lbl.setStyleSheet("font-size: 12px; font-weight: bold; border: none; background: transparent;") # Restored styling
        self.dept_combo = QComboBox()
        self.dept_combo.addItems(["Select department", "Teachers", "Student", "Engineering", "HR"])
        self.dept_combo.setFixedHeight(32)
        self.dept_combo.setStyleSheet("""
            QComboBox {
                border: 1px solid #d9d9d9;
                padding: 0 8px;
                font-size: 12px;
                background-color: #ffffff;
                color: #000000;
            }
            QComboBox::drop-down { border: none; }
        """)
        layout.addWidget(dept_lbl)
        layout.addWidget(self.dept_combo)

        self.password_input = add_field("Password", "Enter password")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.rfid_input = add_field("RFID", "Scan or enter RFID tag")

        # Type ComboBox
        type_lbl = QLabel("Type")
        type_lbl.setStyleSheet("font-size: 12px; font-weight: bold; border: none; background: transparent;")
        self.type_combo = QComboBox()
        self.type_combo.addItems(["Select user type", "Normal", "Admin"])
        self.type_combo.setFixedHeight(32)
        self.type_combo.setStyleSheet("""
            QComboBox {
                border: 1px solid #d9d9d9;
                padding: 0 8px;
                font-size: 12px;
                background-color: #ffffff;
                color: #000000;
            }
            QComboBox::drop-down { border: none; }
        """)
        layout.addWidget(type_lbl)
        layout.addWidget(self.type_combo)

        layout.addStretch()

        # Save Button
        save_btn = QPushButton("Save User")
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
