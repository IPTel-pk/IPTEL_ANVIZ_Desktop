from typing import Callable

from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QPushButton,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
    QTableWidget,
    QTableWidgetItem,
    QHeaderView,
)

from app.ui.components.activity import Activity


class LargeButton(QPushButton):
    """Custom button for the top section with icon, title, and subtitle."""

    def __init__(self, title: str, subtitle: str, icon_path: str, parent=None):
        super().__init__(parent)
        self.setFixedHeight(130)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)

        self.setStyleSheet(
            """
            QPushButton {
                background-color: #ffffff;
                border: 1px solid #d9d9d9;
            }
            QPushButton:hover {
                background-color: #f9f9f9;
            }
            """
        )

        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.setSpacing(2)

        icon_label = QLabel()
        pixmap = QPixmap(icon_path)
        if not pixmap.isNull():
            pixmap = pixmap.scaled(
                50,
                50,
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation,
            )
            icon_label.setPixmap(pixmap)
        icon_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        icon_label.setStyleSheet("border: none; background: transparent;")
        layout.addWidget(icon_label)

        title_label = QLabel(title)
        title_label.setStyleSheet(
            "font-size: 18px; font-weight: 500; border: none; background: transparent; color: #000000;"
        )
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title_label)

        sub_label = QLabel(subtitle)
        sub_label.setStyleSheet(
            "font-size: 10px; color: #878787; border: none; background: transparent;"
        )
        sub_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(sub_label)


class FileItemActions(QWidget):
    """Widget containing action buttons (folder & trash) for the table rows."""
    def __init__(self, button_size: int = 24, button_spacing: int = 10, parent=None):
        super().__init__(parent)
        self.setStyleSheet("border: none; background: transparent;")

        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(button_spacing)
        layout.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)

        # Folder Button
        self.btn1 = QPushButton()
        self.btn1.setIcon(QIcon("assets/folder.png"))
        self.btn1.setStyleSheet("border: none; background: transparent;")
        self.btn1.setFixedSize(button_size, button_size)
        self.btn1.setIconSize(QSize(button_size, button_size))
        layout.addWidget(self.btn1)

        # Trash Button
        self.btn2 = QPushButton()
        self.btn2.setIcon(QIcon("assets/trash.png"))
        self.btn2.setStyleSheet("border: none; background: transparent;")
        self.btn2.setFixedSize(button_size, button_size)
        self.btn2.setIconSize(QSize(button_size, button_size))
        layout.addWidget(self.btn2)


class LauncherActivity(Activity):
    """Launcher Page"""

    def __init__(self, navigate: Callable, parent=None) -> None:
        super().__init__(parent=parent, activity="Launcher", navigate=navigate)

        main_layout = QVBoxLayout(self.content)
        main_layout.setContentsMargins(0, 30, 0, 0)
        main_layout.setSpacing(30)

        # ==========================================
        # 1. TOP BUTTONS
        # ==========================================
        top_buttons_layout = QHBoxLayout()
        top_buttons_layout.setSpacing(30)

        create_btn = LargeButton("Create New File", "(.ipatt)", "assets/add.png")
        open_btn = LargeButton("Open Existing File", "Browse Files", "assets/folder.png")

        top_buttons_layout.addWidget(create_btn)
        top_buttons_layout.addWidget(open_btn)

        main_layout.addLayout(top_buttons_layout)

        # ==========================================
        # 2. RECENT FILES TABLE
        # ==========================================
        recent_files_box = QWidget()
        recent_files_box.setObjectName("recentFilesBox")
        recent_files_box.setStyleSheet("""
            QWidget#recentFilesBox {
                background-color: #ffffff;
                border: 1px solid #d9d9d9;
            }
        """)

        recent_files_layout = QVBoxLayout(recent_files_box)
        recent_files_layout.setContentsMargins(0, 0, 0, 0)
        recent_files_layout.setSpacing(0)

        # Header Label
        header_label = QLabel("Recent Files")
        header_label.setFixedHeight(40)
        header_label.setStyleSheet("""
            font-size: 16px;
            font-weight: bold;
            padding-left: 15px;
            border-bottom: 1px solid #d9d9d9;
            background-color: transparent;
        """)
        recent_files_layout.addWidget(header_label)

        # Table Setup
        table = QTableWidget()
        table.setColumnCount(3)
        table.setHorizontalHeaderLabels(["File Name", "Path", "Actions"])
        
        # Table Styling
        table.setShowGrid(False)
        table.setAlternatingRowColors(True)
        table.verticalHeader().setVisible(False)
        table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        table.setSelectionMode(QTableWidget.SelectionMode.SingleSelection)
        table.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        
        table.setStyleSheet("""
            QTableWidget {
                background-color: #ffffff;
                alternate-background-color: #f9f9f9;
                border: none;
                outline: none;
            }
            QTableWidget::item {
                border-bottom: 1px solid #f0f0f0;
                padding: 5px;
                font-size: 13px;
                color: #000000;
            }
            QTableWidget::item:selected {
                background-color: #e8f0fe;
                color: #000000;
            }
            QHeaderView::section {
                background-color: #ffffff;
                color: #878787;
                font-weight: bold;
                font-size: 12px;
                border: none;
                border-bottom: 1px solid #d9d9d9;
                padding: 5px 10px;
                text-align: left;
            }
        """)

        # Column Resizing
        header = table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents) # File Name
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)          # Path (takes available space)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.Fixed)            # Actions
        table.setColumnWidth(2, 100)                                            # Width for action buttons
        header.setDefaultAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)

        # Dummy Data
        files_data = [
            ("Company-2026.ipatt", "C:/users/name/Desktop/"),
            ("Company-2025.ipatt", "D:/Backups/"),
            ("Very_long_file_name_overflowing.ipatt", "/mnt/username/d/Local Disk/backup_folder/with_very_large/folder_path/overflowing/"),
            ("Company-2024.ipatt", "/home/name/Documents/"),
            ("Company-2023.ipatt", "C:/users/name/Desktop/"),
            ("Company-2022.ipatt", "C:/users/name/Desktop/"),
        ]

        table.setRowCount(len(files_data))
        for row, (name, path) in enumerate(files_data):
            # Name
            name_item = QTableWidgetItem(name)
            name_item.setToolTip(name)
            table.setItem(row, 0, name_item)

            # Path
            path_item = QTableWidgetItem(path)
            path_item.setToolTip(path)
            # Optional: path text can be greyed out
            path_item.setForeground(Qt.GlobalColor.gray)
            table.setItem(row, 1, path_item)

            # Actions
            actions_widget = FileItemActions(button_size=20, button_spacing=15)
            table.setCellWidget(row, 2, actions_widget)

        recent_files_layout.addWidget(table)

        # Add the box to the main layout
        main_layout.addWidget(recent_files_box)
        main_layout.addStretch()