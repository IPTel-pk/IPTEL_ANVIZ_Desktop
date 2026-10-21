from typing import Callable
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QComboBox,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QScrollArea,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)

from app.ui.components.activity import Activity


class SettingsActivity(Activity):
    """**Settings Page**"""
    def __init__(self, navigate: Callable, parent=None) -> None:
        """Initialize the Settings Page Activity"""
        super().__init__(parent=parent, activity="Settings", navigate=navigate)

        # Main Scroll Area (in case the screen is small)
        main_scroll = QScrollArea()
        main_scroll.setWidgetResizable(True)
        main_scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        main_scroll.setStyleSheet("QScrollArea { border: none; background: transparent; }")

        scroll_content = QWidget()
        scroll_content.setStyleSheet("background: transparent;")
        
        main_layout = QVBoxLayout(scroll_content)
        main_layout.setContentsMargins(0, 30, 0, 0)
        main_layout.setSpacing(20)

        # Helper to create a styled input field
        def create_input(placeholder: str, is_readonly: bool = False) -> QLineEdit:
            inp = QLineEdit()
            inp.setPlaceholderText(placeholder)
            inp.setFixedHeight(32)
            bg_color = "#f2f2f2" if is_readonly else "#ffffff"
            color = "#878787" if is_readonly else "#000000"
            inp.setStyleSheet(f"""
                QLineEdit {{
                    border: 1px solid #d9d9d9;
                    padding: 0 8px;
                    font-size: 12px;
                    background-color: {bg_color};
                    color: {color};
                }}
                QLineEdit:focus {{
                    border: 1px solid #21679A;
                }}
            """)
            return inp

        # Helper to create a styled combo box
        def create_combo(items: list) -> QComboBox:
            combo = QComboBox()
            combo.addItems(items)
            combo.setFixedHeight(32)
            combo.setStyleSheet("""
                QComboBox {
                    border: 1px solid #d9d9d9;
                    padding: 0 8px;
                    font-size: 12px;
                    background-color: #ffffff;
                    color: #000000;
                }
                QComboBox::drop-down { border: none; }
            """)
            return combo

        # Helper to create a standard label
        def create_label(text: str, bold: bool = True) -> QLabel:
            lbl = QLabel(text)
            weight = "bold" if bold else "normal"
            lbl.setStyleSheet(f"font-size: 12px; font-weight: {weight}; border: none; background: transparent; color: #000000;")
            return lbl

        # ==========================================
        # 1. COMPANY DETAILS CARD
        # ==========================================
        company_card = QWidget()
        company_card.setStyleSheet("QWidget { background-color: #ffffff; border: 1px solid #d9d9d9; }")
        company_layout = QVBoxLayout(company_card)
        company_layout.setContentsMargins(20, 20, 20, 20)
        company_layout.setSpacing(15)

        # Card Title
        company_title = QLabel("Company Details")
        company_title.setStyleSheet("font-size: 16px; font-weight: bold; border: none; background: transparent;")
        company_layout.addWidget(company_title)

        # Card Content
        company_content = QHBoxLayout()
        company_content.setSpacing(20)

        # Logo Placeholder (Left)
        logo_box = QLabel("Upload\nLogo")
        logo_box.setAlignment(Qt.AlignmentFlag.AlignCenter)
        logo_box.setFixedSize(100, 100)
        logo_box.setStyleSheet("background-color: #f0f0f0; border: 1px solid #d9d9d9; color: #878787; font-size: 12px;")
        company_content.addWidget(logo_box)

        # Fields Grid (Right)
        company_fields = QGridLayout()
        company_fields.setSpacing(10)
        
        company_fields.addWidget(create_label("Company Name"), 0, 0)
        company_fields.addWidget(create_input("e.g. IP Tel Services"), 1, 0)
        
        company_fields.addWidget(create_label("Contact Email"), 0, 1)
        company_fields.addWidget(create_input("info@company.com"), 1, 1)
        
        company_fields.addWidget(create_label("Contact Phone"), 2, 0)
        company_fields.addWidget(create_input("+92 300 0000000"), 3, 0)
        
        company_fields.addWidget(create_label("Address"), 2, 1)
        company_fields.addWidget(create_input("Street, City, Country"), 3, 1)
        
        company_fields.setColumnStretch(0, 1)
        company_fields.setColumnStretch(1, 1)
        
        company_content.addLayout(company_fields, 1) # 1 means take available space
        company_layout.addLayout(company_content)

        main_layout.addWidget(company_card)

        # ==========================================
        # 2. SPLIT CARDS (Regional & System)
        # ==========================================
        split_layout = QHBoxLayout()
        split_layout.setSpacing(20)

        # --- LEFT CARD: Regional & Display ---
        regional_card = QWidget()
        regional_card.setStyleSheet("QWidget { background-color: #ffffff; border: 1px solid #d9d9d9; }")
        regional_layout = QVBoxLayout(regional_card)
        regional_layout.setContentsMargins(20, 20, 20, 20)
        regional_layout.setSpacing(15)

        regional_title = QLabel("Regional & Display")
        regional_title.setStyleSheet("font-size: 16px; font-weight: bold; border: none; background: transparent;")
        regional_layout.addWidget(regional_title)

        regional_fields = QGridLayout()
        regional_fields.setSpacing(10)

        regional_fields.addWidget(create_label("Date Format"), 0, 0)
        regional_fields.addWidget(create_combo(["DD-MM-YYYY", "MM-DD-YYYY", "YYYY-MM-DD"]), 1, 0)

        regional_fields.addWidget(create_label("Time Format"), 0, 1)
        regional_fields.addWidget(create_combo(["12-hour", "24-hour"]), 1, 1)

        regional_fields.addWidget(create_label("Start of Week"), 2, 0)
        regional_fields.addWidget(create_combo(["Monday", "Sunday", "Saturday"]), 3, 0)

        regional_fields.addWidget(create_label("Language"), 2, 1)
        regional_fields.addWidget(create_combo(["English", "Urdu", "Arabic"]), 3, 1)

        regional_fields.addWidget(create_label("Pagination Limit"), 4, 0)
        regional_fields.addWidget(create_combo(["20", "50", "100"]), 5, 0)

        regional_fields.addWidget(create_label("Theme"), 4, 1)
        regional_fields.addWidget(create_combo(["Light", "Dark"]), 5, 1)

        regional_fields.addWidget(create_label("Timezone"), 6, 0)
        regional_fields.addWidget(create_combo(["(GMT+5:00) Islamabad", "(GMT+0:00) London"]), 7, 0, 1, 2) # Span 2 cols

        regional_fields.setColumnStretch(0, 1)
        regional_fields.setColumnStretch(1, 1)
        regional_layout.addLayout(regional_fields)
        regional_layout.addStretch()

        split_layout.addWidget(regional_card, 1)

        # --- RIGHT CARD: System & Data ---
        system_card = QWidget()
        system_card.setStyleSheet("QWidget { background-color: #ffffff; border: 1px solid #d9d9d9; }")
        system_layout = QVBoxLayout(system_card)
        system_layout.setContentsMargins(20, 20, 20, 20)
        system_layout.setSpacing(15)

        system_title = QLabel("System & Data")
        system_title.setStyleSheet("font-size: 16px; font-weight: bold; border: none; background: transparent;")
        system_layout.addWidget(system_title)

        system_fields = QGridLayout()
        system_fields.setSpacing(10)

        system_fields.addWidget(create_label("Auto Backup"), 0, 0)
        system_fields.addWidget(create_combo(["Daily at 12:00 AM", "Weekly", "Disabled"]), 1, 0)

        system_fields.addWidget(create_label("Backup Location"), 0, 1)
        system_fields.addWidget(create_input("C:/Users/name/Backups/", is_readonly=True), 1, 1)

        system_fields.addWidget(create_label("Session Timeout (minutes)"), 2, 0)
        system_fields.addWidget(create_input("30"), 3, 0)

        system_fields.addWidget(create_label("Attendance Grace Period (minutes)"), 2, 1)
        system_fields.addWidget(create_input("10"), 3, 1)

        system_fields.setColumnStretch(0, 1)
        system_fields.setColumnStretch(1, 1)
        system_layout.addLayout(system_fields)
        system_layout.addStretch()

        split_layout.addWidget(system_card, 1)

        main_layout.addLayout(split_layout)

        # ==========================================
        # 3. BOTTOM ACTION BUTTONS
        # ==========================================
        # Add a stretch before the buttons to push them to the bottom
        main_layout.addStretch()

        action_layout = QHBoxLayout()
        action_layout.setSpacing(15)

        # Reset Button
        reset_btn = QPushButton("Reset to Defaults")
        reset_btn.setFixedSize(150, 36)
        reset_btn.setStyleSheet("""
            QPushButton {
                background-color: #ffffff;
                color: #000000;
                border: 1px solid #d9d9d9;
                font-size: 13px;
                font-weight: 500;
            }
            QPushButton:hover {
                background-color: #f9f9f9;
            }
        """)
        action_layout.addWidget(reset_btn)

        action_layout.addStretch()

        # Save Button
        save_btn = QPushButton("Save Settings")
        save_btn.setFixedSize(150, 36)
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
        action_layout.addWidget(save_btn)

        main_layout.addLayout(action_layout)

        # Set the scroll area widget
        main_scroll.setWidget(scroll_content)

        # `self.content` is a QWidget in Activity, so attach a layout before adding children.
        content_layout = QVBoxLayout(self.content)
        content_layout.setContentsMargins(0, 0, 0, 0)
        content_layout.setSpacing(0)
        content_layout.addWidget(main_scroll)