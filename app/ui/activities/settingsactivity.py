from typing import Callable
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QScrollArea,
    QVBoxLayout,
    QWidget,
)
from app.ui.components.activity import Activity
from app.ui.components.inputfield import InputField
from app.ui.components.selectfield import SelectField
from app.settings import ACCENT_COLOR, SECONDARY_COLOR

class SettingsActivity(Activity):
    """
    ### Settings Activity
    This widget creates the application settings screen with company details, regional preferences, system options, and action buttons for saving or resetting configuration.
    """

    def __init__(self, navigate: Callable, parent=None) -> None:
        """
        Initialize the Settings Page Activity.

        This method builds the scrollable settings page, card sections, and action controls for configuration management.
        """
        super().__init__(
            parent=parent, activity="Settings", navigate=navigate
        )

        # 1. Main Layout
        # This sets up the scrollable settings container so the page can fit smaller screens without clipping content.
        main_scroll = QScrollArea()
        main_scroll.setWidgetResizable(True)
        main_scroll.setHorizontalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff
        )
        main_scroll.setStyleSheet(
            "QScrollArea { border: none; background: transparent; }"
        )
        scroll_content = QWidget()
        scroll_content.setStyleSheet("background: transparent;")
        
        main_layout = QVBoxLayout(scroll_content)
        main_layout.setContentsMargins(0, 30, 0, 0)
        main_layout.setSpacing(20)

        # 1. COMPANY DETAILS CARD
        company_card = QWidget()
        company_card.setStyleSheet(f"""
            QWidget {{
                background-color: #ffffff;
                border: 1px solid {SECONDARY_COLOR};
            }}
        """)
        company_layout = QVBoxLayout(company_card)
        company_layout.setContentsMargins(20, 20, 20, 20)
        company_layout.setSpacing(15)

        # Card Title
        company_title = QLabel("Company Details")
        company_title.setStyleSheet("""
            font-size: 16px; font-weight: bold;
            border: none; background: transparent;
        """)
        company_layout.addWidget(company_title)

        # Card Content
        company_content = QHBoxLayout()
        company_content.setSpacing(20)

        # Logo Placeholder (Left)
        logo_box = QLabel("Upload\nLogo")
        logo_box.setAlignment(Qt.AlignmentFlag.AlignCenter)
        logo_box.setFixedSize(100, 100)
        logo_box.setStyleSheet(f"""
            background-color: #f0f0f0; border: 1px solid {SECONDARY_COLOR};
            color: #878787; font-size: 12px;
        """)
        company_content.addWidget(logo_box)

        # Fields Grid (Right) using InputField
        company_fields = QGridLayout()
        company_fields.setSpacing(10)

        company_fields.addWidget(InputField(
            "Company Name", "e.g. IP Tel Services"
        ), 0, 0)
        company_fields.addWidget(InputField(
            "Contact Email", "info@company.com"
        ), 0, 1)
        company_fields.addWidget(InputField(
            "Contact Phone", "+92 300 0000000"
        ), 1, 0)
        company_fields.addWidget(InputField(
            "Address", "Street, City, Country"
        ), 1, 1)
        company_fields.setColumnStretch(0, 1)
        company_fields.setColumnStretch(1, 1)

        company_content.addLayout(company_fields, 1)
        company_layout.addLayout(company_content)

        main_layout.addWidget(company_card)

        # 2. SPLIT CARDS (Regional & System)
        split_layout = QHBoxLayout()
        split_layout.setSpacing(20)

        # LEFT CARD: Regional & Display
        regional_card = QWidget()
        regional_card.setStyleSheet(f"""
            QWidget {{
                background-color: #ffffff;
                border: 1px solid {SECONDARY_COLOR};
            }}
        """)
        regional_layout = QVBoxLayout(regional_card)
        regional_layout.setContentsMargins(20, 20, 20, 20)
        regional_layout.setSpacing(15)

        regional_title = QLabel("Regional & Display")
        regional_title.setStyleSheet("""
            font-size: 16px; font-weight: bold;
            border: none; background: transparent;
        """)
        regional_layout.addWidget(regional_title)
        regional_fields = QGridLayout()
        regional_fields.setSpacing(10)

        # Using SelectField
        regional_fields.addWidget(SelectField(
            "Date Format", ["DD-MM-YYYY", "MM-DD-YYYY", "YYYY-MM-DD"]
        ), 0, 0)
        regional_fields.addWidget(SelectField(
            "Time Format", ["12-hour", "24-hour"]
        ), 0, 1)
        regional_fields.addWidget(SelectField(
            "Start of Week", ["Monday", "Sunday", "Saturday"]
        ), 1, 0)
        regional_fields.addWidget(SelectField(
            "Language", ["English", "Urdu", "Arabic"]
        ), 1, 1)
        regional_fields.addWidget(SelectField(
            "Pagination Limit", ["20", "50", "100"]
        ), 2, 0)
        regional_fields.addWidget(SelectField(
            "Theme", ["Light", "Dark"]
        ), 2, 1)
        regional_fields.addWidget(SelectField(
            "Timezone", ["(GMT+5:00) Islamabad", "(GMT+0:00) London"]
        ), 3, 0, 1, 2)

        regional_fields.setColumnStretch(0, 1)
        regional_fields.setColumnStretch(1, 1)
        regional_layout.addLayout(regional_fields)
        regional_layout.addStretch()

        split_layout.addWidget(regional_card, 1)

        # RIGHT CARD: System & Data
        system_card = QWidget()
        system_card.setStyleSheet(f"""
            QWidget {{
                background-color: #ffffff;
                border: 1px solid {SECONDARY_COLOR};
            }}
        """)
        system_layout = QVBoxLayout(system_card)
        system_layout.setContentsMargins(20, 20, 20, 20)
        system_layout.setSpacing(15)

        system_title = QLabel("System & Data")
        system_title.setStyleSheet("""
            font-size: 16px; font-weight: bold;
            border: none; background: transparent;
        """)
        system_layout.addWidget(system_title)

        system_fields = QGridLayout()
        system_fields.setSpacing(10)
        system_fields.addWidget(SelectField(
            "Auto Backup", ["Daily at 12:00 AM", "Weekly", "Disabled"]
        ), 0, 0)
        system_fields.addWidget(InputField(
            "Backup Location", "C:/Users/name/Backups/", disable=True
        ), 0, 1)
        system_fields.addWidget(InputField(
            "Session Timeout (minutes)", "30"
            ), 1, 0)
        system_fields.addWidget(InputField(
            "Attendance Grace Period (minutes)", "10"
        ), 1, 1)
        system_fields.setColumnStretch(0, 1)
        system_fields.setColumnStretch(1, 1)
        system_layout.addLayout(system_fields)
        system_layout.addStretch()

        split_layout.addWidget(system_card, 1)
        main_layout.addLayout(split_layout)

        # 3. BOTTOM ACTION BUTTONS
        main_layout.addStretch()

        action_layout = QHBoxLayout()
        action_layout.setSpacing(15)

        reset_btn = QPushButton("Reset to Defaults")
        reset_btn.setFixedSize(150, 36)
        reset_btn.setStyleSheet(f"""
            QPushButton {{
                background-color: #ffffff;
                color: #000000;
                border: 1px solid {SECONDARY_COLOR};
                font-size: 13px;
                font-weight: 500;
            }}
            QPushButton:hover {{
                background-color: #f9f9f9;
            }}
        """)
        action_layout.addWidget(reset_btn)
        action_layout.addStretch()

        save_btn = QPushButton("Save Settings")
        save_btn.setFixedSize(150, 36)
        save_btn.setStyleSheet(f"""
            QPushButton {{
                background-color: {ACCENT_COLOR};
                color: #ffffff;
                border: none;
                font-size: 13px;
                font-weight: bold;
            }}
            QPushButton:hover {{
                background-color: #1a527c;
            }}
        """)
        action_layout.addWidget(save_btn)
        main_layout.addLayout(action_layout)

        # 4. FINALIZE LAYOUT
        main_scroll.setWidget(scroll_content)

        # Safely get or create the layout to avoid Pylance warnings
        layout = self.content.layout()
        if layout is None:
            layout = QVBoxLayout(self.content)
            layout.setContentsMargins(0, 0, 0, 0)
            layout.setSpacing(0)
        layout.addWidget(main_scroll)
