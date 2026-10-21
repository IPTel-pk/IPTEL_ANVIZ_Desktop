from typing import Callable
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtWidgets import (
    QCheckBox,
    QComboBox,
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
# Importing from the device activity file as requested
# Adjust the import path if your folder structure is different
from app.ui.activities.deviceactivity import FlowLayout, ToolbarButton


class UserCard(QWidget):
    """Custom widget representing a single user."""
    def __init__(self, name: str, department: str, parent=None):
        super().__init__(parent)
        self.setFixedHeight(70)
        self.setMinimumWidth(250)
        self.setMaximumWidth(350)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        
        self.setStyleSheet("""
            UserCard {
                background-color: #ffffff;
                border: 1px solid #d9d9d9;
            }
        """)
        
        layout = QHBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(15)

        # --- Checkbox (Moved to Left) ---
        checkbox = QCheckBox()
        checkbox.setStyleSheet("border: none; background: transparent;")
        layout.addWidget(checkbox, alignment=Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)

        # --- Image (90% of card height) ---
        # Card is 70px tall, 10px top margin + 10px bottom margin = 50px available. 
        # 90% of 70 is ~63px. We'll scale it to fit nicely.
        icon_label = QLabel()
        pixmap = QPixmap("assets/icon.jpg")
        if not pixmap.isNull():
            icon_label.setPixmap(pixmap.scaled(
                50, 50, 
                Qt.AspectRatioMode.KeepAspectRatio, 
                Qt.TransformationMode.SmoothTransformation
            ))
        icon_label.setFixedSize(50, 50)
        icon_label.setStyleSheet("border: none; background: transparent;")
        layout.addWidget(icon_label)

        # --- Text Labels ---
        text_layout = QVBoxLayout()
        text_layout.setSpacing(2)
        text_layout.setAlignment(Qt.AlignmentFlag.AlignVCenter)

        name_label = QLabel(name)
        name_label.setStyleSheet("font-size: 16px; font-weight: bold; color: #000000; border: none; background: transparent;")
        
        dept_label = QLabel(department)
        dept_label.setStyleSheet("font-size: 13px; color: #878787; border: none; background: transparent;")
        
        text_layout.addWidget(name_label)
        text_layout.addWidget(dept_label)
        layout.addLayout(text_layout)

        layout.addStretch() # Pushes everything to the left

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

class UsersActivity(Activity):
    """**Users Page**"""
    def __init__(self, navigate: Callable, parent=None) -> None:
        """Initialize the Users Page Activity"""
        super().__init__(parent=parent, activity="Users", navigate=navigate)

        # 1. Main layout is Vertical (Toolbar on top, Content below)
        main_layout = QVBoxLayout(self.content)
        main_layout.setContentsMargins(0, 30, 0, 0)
        main_layout.setSpacing(20)

        # ==========================================
        # TOP: TOOLBAR
        # ==========================================
        toolbar_widget = QWidget()
        toolbar_widget.setStyleSheet("background: transparent;")
        toolbar_widget.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        
        toolbar_layout = FlowLayout(toolbar_widget, margin=0, h_spacing=10, v_spacing=10)
        
        buttons = [
            ("Add", "assets/icon.jpg"),
            ("Edit", "assets/icon.jpg"),
            ("Delete", "assets/icon.jpg"),
            ("Download", "assets/icon.jpg"),
            ("Upload", "assets/icon.jpg"),
        ]
        
        for text, icon in buttons:
            toolbar_layout.addWidget(ToolbarButton(text, icon))
            
        main_layout.addWidget(toolbar_widget)

        # ==========================================
        # BOTTOM: SPLIT LAYOUT (Cards Left, Sidebar Right)
        # ==========================================
        content_split_layout = QHBoxLayout()
        content_split_layout.setSpacing(20)

        # --- LEFT PANE: Scrollable Cards ---
        left_pane = QWidget()
        left_pane.setStyleSheet("background: transparent;")
        left_layout = QVBoxLayout(left_pane)
        left_layout.setContentsMargins(0, 0, 0, 0)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        scroll_area.setStyleSheet("QScrollArea { border: none; background: transparent; }")
        
        scroll_content = QWidget()
        scroll_content.setStyleSheet("background: transparent;")
        
        # Using the imported FlowLayout
        self.cards_layout = FlowLayout(scroll_content, margin=0, h_spacing=15, v_spacing=15)

        # Dummy Data
        users = [
            ("John Doe", "Teachers"),
            ("John Smith", "Student"),
            ("Sarah Smith", "Student"),
            ("Mike Johnson", "Student"),
        ]

        for name, dept in users:
            card = UserCard(name, dept)
            self.cards_layout.addWidget(card)

        scroll_area.setWidget(scroll_content)
        left_layout.addWidget(scroll_area)

        # --- RIGHT PANE: User Form Sidebar ---
        right_pane = UserFormSidebar()

        # Add both panes to the split layout
        content_split_layout.addWidget(left_pane, 1) # Left pane expands
        content_split_layout.addWidget(right_pane)   # Right pane fixed width

        # Pass `1` as the stretch factor to take all extra vertical space
        main_layout.addLayout(content_split_layout, 1)