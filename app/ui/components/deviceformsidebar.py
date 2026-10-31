from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QScrollArea,
    QVBoxLayout,
    QWidget,
)
from app.ui.components.inputfield import InputField
from app.ui.components.selectfield import SelectField
from app.ui.components.primarybutton import PrimaryButton

class DeviceFormSidebar(QWidget):
    """Reduced size right sidebar for adding/editing a device."""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedWidth(275)
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)

        self.setStyleSheet("""
            DeviceFormSidebar {
                background-color: #ffffff;
                border: 1px solid #d9d9d9;
            }
        """)
        
        # Main layout for the Sidebar (holds the ScrollArea)
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # Scroll Area
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        scroll_area.setStyleSheet("""
            QScrollArea {
                border: none;
                background-color: transparent;
            }
        """)

        # Content Widget (holds the form)
        content_widget = QWidget()
        content_widget.setStyleSheet("background-color: transparent;")
        
        layout = QVBoxLayout(content_widget)
        layout.setContentsMargins(15, 15, 15, 15)
        layout.setSpacing(10)

        # Header
        title = QLabel("Add Device")
        title.setStyleSheet("font-size: 18px; font-weight: bold; border: none; background: transparent;")
        layout.addWidget(title)

        # --- Form Fields using Custom Components ---
        
        self.name_input = InputField("Device Name *", "e.g. Reception")
        layout.addWidget(self.name_input)
        
        self.model_input = InputField("Device Model", "e.g. ANVIZ EP 300")
        layout.addWidget(self.model_input)
        
        self.dept_combo = SelectField("Department", ["Select department", "Engineering", "HR", "Marketing"])
        layout.addWidget(self.dept_combo)

        # IP & Port Row (Side-by-side using QHBoxLayout)
        ip_port_layout = QHBoxLayout()
        ip_port_layout.setSpacing(10)
        
        self.ip_input = InputField("IP Address *", "192.168.1.100")
        self.port_input = InputField("Port *", "3306")
        
        ip_port_layout.addWidget(self.ip_input)
        ip_port_layout.addWidget(self.port_input)
        layout.addLayout(ip_port_layout)

        self.serial_input = InputField("Serial Number", "Enter serial number")
        layout.addWidget(self.serial_input)
        
        # Push button to the bottom of the form content
        layout.addStretch()

        save_btn = PrimaryButton("Save Device")
        save_btn.clicked.connect(self._on_save_clicked)
        layout.addWidget(save_btn)
        save_btn.clicked.connect(self._on_save_clicked)
        layout.addWidget(save_btn)

        # Finalize the Scroll Area
        scroll_area.setWidget(content_widget)
        main_layout.addWidget(scroll_area)

    def _on_save_clicked(self):
        """Placeholder for your save logic."""
        device_data = self.get_data()
        print("Saving Device:", device_data)
        # Here you would typically emit a signal or call a database function

    def get_data(self) -> dict:
        """Helper method to extract all form data at once."""
        return {
            "name": self.name_input.text(),
            "model": self.model_input.text(),
            "department": self.dept_combo.current_text(),
            "ip_address": self.ip_input.text(),
            "port": self.port_input.text(),
            "serial": self.serial_input.text(),
        }