from typing import Callable
from PySide6.QtCore import Qt, QSize, QRect, QPoint
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtWidgets import (
    QCheckBox,
    QComboBox,
    QHBoxLayout,
    QLabel,
    QLayout,
    QLineEdit,
    QPushButton,
    QScrollArea,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
    QGridLayout,
)

from app.ui.components.activity import Activity


# ==========================================
# Custom FlowLayout for flex-wrap behavior
# ==========================================
class FlowLayout(QLayout):
    def __init__(self, parent=None, margin=0, h_spacing=20, v_spacing=20):
        super().__init__(parent)
        self.item_list = []
        self.h_spacing = h_spacing
        self.v_spacing = v_spacing
        self.setContentsMargins(margin, margin, margin, margin)

    def addItem(self, item):
        self.item_list.append(item)

    def count(self):
        return len(self.item_list)

    def itemAt(self, index):
        if 0 <= index < len(self.item_list):
            return self.item_list[index]
        return None

    def takeAt(self, index):
        if 0 <= index < len(self.item_list):
            return self.item_list.pop(index)
        return None

    def expandingDirections(self):
        return Qt.Orientation.Vertical

    def hasHeightForWidth(self):
        return True

    def heightForWidth(self, width):
        return self.doLayout(QRect(0, 0, width, 0), True)

    def setGeometry(self, rect):
        super().setGeometry(rect)
        self.doLayout(rect, False)

    def sizeHint(self):
        return self.minimumSize()

    def minimumSize(self):
        size = QSize()
        for item in self.item_list:
            size = size.expandedTo(item.minimumSize())
        margins = self.contentsMargins()
        size += QSize(margins.left() + margins.right(), margins.top() + margins.bottom())
        return size

    def doLayout(self, rect, test_only):
        x = rect.x()
        y = rect.y()
        line_height = 0

        for item in self.item_list:
            widget = item.widget()
            space_x = self.h_spacing
            space_y = self.v_spacing

            item_size = item.sizeHint()
            next_x = x + item_size.width() + space_x
            if next_x - space_x > rect.right() and line_height > 0:
                x = rect.x()
                y = y + line_height + space_y
                next_x = x + item_size.width() + space_x
                line_height = 0

            if not test_only:
                item.setGeometry(QRect(QPoint(x, y), item_size))

            x = next_x
            line_height = max(line_height, item_size.height())

        return y + line_height - rect.y()


# ==========================================
# UI Components
# ==========================================
class ToolbarButton(QPushButton):
    """Helper class for the top action buttons."""
    def __init__(self, text: str, icon_path: str, parent=None):
        super().__init__(text, parent)
        self.setIcon(QIcon(icon_path))
        self.setIconSize(QSize(16, 16))
        self.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.setFixedHeight(36)
        self.setStyleSheet("""
            QPushButton {
                background-color: #ffffff;
                color: #000000;
                border: 1px solid #d9d9d9;
                padding: 0 15px;
                font-size: 13px;
            }
            QPushButton:hover {
                background-color: #f9f9f9;
            }
            QPushButton:pressed {
                background-color: #e0e0e0;
            }
        """)


class DeviceCard(QWidget):
    """Custom widget representing a single device."""
    def __init__(self, name: str, model: str, ip: str, port: str, serial: str, last_seen: str, is_online: bool, parent=None):
        super().__init__(parent)
        self.setMinimumWidth(200)
        self.setMaximumWidth(280)
        self.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        
        self.setStyleSheet("""
            DeviceCard {
                background-color: #ffffff;
                border: 1px solid #d9d9d9;
            }
        """)
        
        layout = QVBoxLayout(self)
        layout.setContentsMargins(15, 15, 15, 15)
        layout.setSpacing(10)

        # --- Top Row: Checkbox ---
        top_row = QHBoxLayout()
        checkbox = QCheckBox()
        checkbox.setStyleSheet("border: none; background: transparent;")
        top_row.addWidget(checkbox)
        top_row.addStretch()
        layout.addLayout(top_row)

        # --- Centered Icon ---
        icon_layout = QHBoxLayout()
        icon_label = QLabel()
        pixmap = QPixmap("assets/device.jpg")
        if not pixmap.isNull():
            icon_label.setPixmap(pixmap.scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))
        icon_label.setFixedSize(50, 50)
        icon_label.setStyleSheet("border: none; background: transparent;")
        icon_layout.addStretch()
        icon_layout.addWidget(icon_label)
        icon_layout.addStretch()
        layout.addLayout(icon_layout)

        # --- Status Indicator ---
        status_layout = QHBoxLayout()
        status_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        status_layout.setSpacing(5)
        
        dot = QLabel()
        dot.setFixedSize(10, 10)
        color = "#2ecc71" if is_online else "#bdc3c7"
        dot.setStyleSheet(f"background-color: {color}; border-radius: 5px; border: none;")
        
        status_text = QLabel("Online" if is_online else "Offline")
        status_text.setStyleSheet("font-size: 11px; color: #000000; border: none; background: transparent;")
        
        status_layout.addWidget(dot)
        status_layout.addWidget(status_text)
        layout.addLayout(status_layout)

        # --- Title & Subtitle ---
        title_label = QLabel(name)
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setWordWrap(True)
        title_label.setStyleSheet("font-size: 18px; font-weight: bold; color: #000000; border: none; background: transparent;")
        layout.addWidget(title_label)

        subtitle_label = QLabel(model)
        subtitle_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        subtitle_label.setWordWrap(True)
        subtitle_label.setStyleSheet("font-size: 14px; color: #000000; border: none; background: transparent;")
        layout.addWidget(subtitle_label)

        # --- Properties Grid ---
        props_layout = QGridLayout()
        props_layout.setContentsMargins(0, 10, 0, 0)
        props_layout.setVerticalSpacing(4)
        
        props = [
            ("IP", ip), ("Port", port), 
            ("Serial No.", serial), ("Last Seen", last_seen)
        ]
        
        for row, (key, value) in enumerate(props):
            key_label = QLabel(key)
            key_label.setStyleSheet("font-size: 11px; font-weight: bold; color: #000000; border: none; background: transparent;")
            val_label = QLabel(value)
            val_label.setWordWrap(True)
            val_label.setStyleSheet("font-size: 11px; color: #878787; border: none; background: transparent;")
            
            props_layout.addWidget(key_label, row, 0, Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
            props_layout.addWidget(val_label, row, 1, Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
            
        props_layout.setColumnStretch(1, 1)
        layout.addLayout(props_layout)


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


class DeviceActivity(Activity):
    """**Device Page**"""
    def __init__(self, navigate: Callable, parent=None) -> None:
        super().__init__(parent=parent, activity="Device", navigate=navigate)

        # 1. Main layout is Vertical (Toolbar on top, Content below)
        main_layout = QVBoxLayout(self.content)
        main_layout.setContentsMargins(0, 30, 0, 0)
        main_layout.setSpacing(20)

        # ==========================================
        # TOP: TOOLBAR
        # ==========================================
        toolbar_widget = QWidget()
        toolbar_widget.setStyleSheet("background: transparent;")
        # FIX 1: Force the toolbar to only take the height it needs
        toolbar_widget.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        
        toolbar_layout = FlowLayout(toolbar_widget, margin=0, h_spacing=10, v_spacing=10)
        
        buttons = [
            ("Add", "assets/add.png"), ("Edit", "assets/edit.png"),
            ("Delete", "assets/delete.png"), ("Ping", "assets/signal.png"),
            ("Sync Time", "assets/signal.png"), ("Download Users", "assets/download.png"),
            ("Download Logs", "assets/download.png"),
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
        
        self.cards_layout = FlowLayout(scroll_content, margin=0, h_spacing=20, v_spacing=20)

        # Dummy Data
        devices = [
            ("Boys Department", "ANVIZ EP 300", "192.168.1.110", "3306", "SN44328", "2026-15-8 1:15 PM", True),
            ("Girls Department", "ANVIZ EP 300", "192.168.1.111", "3306", "SN44358", "2026-15-8 1:15 PM", False),
            ("Reception", "ANVIZ EP 300", "192.168.1.113", "3306", "SN44328", "2026-15-8 1:15 PM", False),
            ("Floor-2", "ANVIZ EP 300", "192.168.1.111", "3306", "SN44358", "2026-15-8 1:15 PM", False),
            ("HR Room", "ANVIZ EP 300", "192.168.1.115", "3306", "SN44399", "2026-15-8 1:15 PM", True),
        ]

        for dev in devices:
            card = DeviceCard(*dev)
            self.cards_layout.addWidget(card)

        scroll_area.setWidget(scroll_content)
        left_layout.addWidget(scroll_area)

        # --- RIGHT PANE: Device Form Sidebar ---
        right_pane = DeviceFormSidebar()

        # Add both panes to the split layout
        content_split_layout.addWidget(left_pane, 1) # Left pane expands to fill space
        content_split_layout.addWidget(right_pane)   # Right pane maintains fixed width

        # FIX 2: Pass `1` as the stretch factor to the layout so it takes all extra vertical space
        main_layout.addLayout(content_split_layout, 1)