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
from app.settings import SECONDARY_COLOR

class DeviceFormSidebar(QWidget):
    """
    ### DeviceFormSidebar
    This widget provides the compact form used for creating or editing device records inside the device management screen.
    """

    def __init__(self, parent=None):
        """
        Initialize the device form sidebar.

        This method creates the sidebar container, scrollable form, and all fields needed to add or modify a device.
        """
        super().__init__(parent)
        self.setFixedWidth(275)
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setStyleSheet(f"""
            DeviceFormSidebar {{
                background-color: #ffffff;
                border: 1px solid {SECONDARY_COLOR};
            }}
        """)

        # 1. Create the main layout for the sidebar container
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # 2. Add the scroll area so the form can grow without clipping
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setHorizontalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff
        )
        scroll_area.setStyleSheet("""
            QScrollArea {
                border: none;
                background-color: transparent;
            }
        """)

        # 3. Create the inner widget holding the actual form controls
        content_widget = QWidget()
        content_widget.setStyleSheet("background-color: transparent;")

        layout = QVBoxLayout(content_widget)
        layout.setContentsMargins(15, 15, 15, 15)
        layout.setSpacing(10)

        # 4. Add the sidebar title
        title = QLabel("Add Device")
        title.setStyleSheet("""
            font-size: 18px; font-weight: bold;
            border: none; background: transparent;
        """)
        layout.addWidget(title)

        # 5. Add the form fields for the device details
        self.name_input = InputField("Device Name *", "e.g. Reception")
        layout.addWidget(self.name_input)

        self.model_input = InputField("Device Model", "e.g. ANVIZ EP 300")
        layout.addWidget(self.model_input)

        self.dept_combo = SelectField(
            "Department", [
                "Select department", "Engineering", "HR", "Marketing"
            ]
        )
        layout.addWidget(self.dept_combo)

        # 6. Add the IP and port fields in one row
        ip_port_layout = QHBoxLayout()
        ip_port_layout.setSpacing(10)

        self.ip_input = InputField("IP Address *", "192.168.1.100")
        self.port_input = InputField("Port *", "3306")

        ip_port_layout.addWidget(self.ip_input)
        ip_port_layout.addWidget(self.port_input)
        layout.addLayout(ip_port_layout)

        self.serial_input = InputField("Serial Number", "Enter serial number")
        layout.addWidget(self.serial_input)

        # 7. Add the save button at the bottom of the form
        layout.addStretch()
        save_btn = PrimaryButton("Save Device")
        save_btn.clicked.connect(self._on_save_clicked)
        layout.addWidget(save_btn)

        # 8. Finalize the scroll area layout
        scroll_area.setWidget(content_widget)
        main_layout.addWidget(scroll_area)

    def _on_save_clicked(self):
        """
        Save the device data from the form.

        This method collects the form values and provides a place to hook validation or persistence logic later.
        """
        device_data = self.get_data()
        print("Saving Device:", device_data)

    def get_data(self) -> dict:
        """
        Return the current device form values as a dictionary.

        This is useful for validation, saving, or passing submitted data to a backend or database layer.
        """
        return {
            "name": self.name_input.text(),
            "model": self.model_input.text(),
            "department": self.dept_combo.current_text(),
            "ip_address": self.ip_input.text(),
            "port": self.port_input.text(),
            "serial": self.serial_input.text(),
        }
