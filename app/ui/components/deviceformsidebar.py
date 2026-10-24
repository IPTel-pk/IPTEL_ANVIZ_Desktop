from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QComboBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QScrollArea,
    QVBoxLayout,
    QWidget,
)

class DeviceFormSidebar(QWidget):
    """Reduced size right sidebar for adding/editing a device."""
    def __init__(self, parent=None):
        super().__init__(parent)
        # Increased slightly to accommodate the scrollbar width
        self.setFixedWidth(275)
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)

        self.setStyleSheet("""
            DeviceFormSidebar {
                background-color: #ffffff;
                border: 1px solid #d9d9d9;
            }
        """)
        
        # 1. Main layout for the Sidebar (holds the ScrollArea)
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # 2. Scroll Area
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        # Hide horizontal scrollbar
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        scroll_area.setStyleSheet("""
            QScrollArea {
                border: none;
                background-color: transparent;
            }
        """)

        # 3. Content Widget (holds your form)
        content_widget = QWidget()
        content_widget.setStyleSheet("background-color: transparent;")
        
        layout = QVBoxLayout(content_widget)
        layout.setContentsMargins(15, 15, 15, 15)
        layout.setSpacing(10)

        # Header
        title = QLabel("Add Device")
        title.setStyleSheet("font-size: 18px; font-weight: bold; border: none; background: transparent;")
        layout.addWidget(title)

        # Helper function to create form fields
        def add_field(label_text: str, placeholder: str, required: bool = False) -> QLineEdit:
            lbl = QLabel(label_text + (" *" if required else ""))
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

        self.name_input = add_field("Device Name", "e.g. Reception", required=True)
        self.model_input = add_field("Device Model", "e.g. ANVIZ EP 300")
        
        # Department ComboBox
        dept_lbl = QLabel("Department")
        dept_lbl.setStyleSheet("font-size: 12px; font-weight: bold; border: none; background: transparent;")
        self.dept_combo = QComboBox()
        self.dept_combo.addItems(["Select department", "Engineering", "HR", "Marketing"])
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

        # IP & Port Row
        ip_port_layout = QHBoxLayout()
        ip_port_layout.setSpacing(10)
        
        # IP Column
        ip_col = QVBoxLayout()
        ip_lbl = QLabel("IP Address *")
        ip_lbl.setStyleSheet("font-size: 12px; font-weight: bold; border: none; background: transparent;")
        self.ip_input = QLineEdit()
        self.ip_input.setPlaceholderText("192.168.1.100")
        self.ip_input.setFixedHeight(32)
        self.ip_input.setStyleSheet("QLineEdit { border: 1px solid #d9d9d9; padding: 0 8px; font-size: 12px; }")
        ip_col.addWidget(ip_lbl)
        ip_col.addWidget(self.ip_input)
        
        # Port Column
        port_col = QVBoxLayout()
        port_lbl = QLabel("Port *")
        port_lbl.setStyleSheet("font-size: 12px; font-weight: bold; border: none; background: transparent;")
        self.port_input = QLineEdit()
        self.port_input.setPlaceholderText("3306")
        self.port_input.setFixedHeight(32)
        self.port_input.setStyleSheet("QLineEdit { border: 1px solid #d9d9d9; padding: 0 8px; font-size: 12px; }")
        port_col.addWidget(port_lbl)
        port_col.addWidget(self.port_input)

        ip_port_layout.addLayout(ip_col)
        ip_port_layout.addLayout(port_col)
        layout.addLayout(ip_port_layout)

        self.serial_input = add_field("Serial Number", "Enter serial number")
        
        # Push button to the bottom of the form content
        layout.addStretch()

        # Save Button
        save_btn = QPushButton("Save Device")
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

        # 4. Finalize the Scroll Area
        scroll_area.setWidget(content_widget)
        main_layout.addWidget(scroll_area)
