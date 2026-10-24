from typing import Callable
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QTableWidget,
    QTableWidgetItem,
    QHeaderView,
)
from app.ui.components.activity import Activity
from app.ui.components.largebutton import LargeButton
from app.ui.components.fileitemaction import FileItemActions
from data.launcher import files_data

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