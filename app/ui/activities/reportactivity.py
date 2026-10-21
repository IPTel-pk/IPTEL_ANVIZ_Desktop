from typing import Callable
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (
    QComboBox,
    QHBoxLayout,
    QHeaderView,
    QLabel,
    QPushButton,
    QSizePolicy,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
    QScrollArea, # Added QScrollArea
)

from app.ui.components.activity import Activity
from app.ui.activities.deviceactivity import FlowLayout


class ReportActivity(Activity):
    """**Report Page**"""
    def __init__(self, navigate: Callable, parent=None) -> None:
        """Initialize the Report Page Activity"""
        super().__init__(parent=parent, activity="Report", navigate=navigate)

        # 1. Main Scroll Area (Allows window to shrink vertically)
        main_scroll = QScrollArea()
        main_scroll.setWidgetResizable(True)
        main_scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        main_scroll.setStyleSheet("QScrollArea { border: none; background: transparent; }")

        scroll_content = QWidget()
        scroll_content.setStyleSheet("background: transparent;")
        
        main_layout = QVBoxLayout(scroll_content)
        main_layout.setContentsMargins(0, 30, 0, 0)
        main_layout.setSpacing(20)

        # ==========================================
        # 2. TOP FILTER BAR & ACTION BUTTONS (RESPONSIVE)
        # ==========================================
        top_bar_widget = QWidget()
        top_bar_widget.setStyleSheet("background: transparent;")
        top_bar_widget.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        
        top_bar = FlowLayout(top_bar_widget, margin=0, h_spacing=15, v_spacing=15)

        # Helper function to create the compact filter boxes
        def create_filter(label_text: str, items: list) -> QWidget:
            widget = QWidget()
            widget.setStyleSheet("background: transparent;")
            layout = QVBoxLayout(widget)
            layout.setContentsMargins(0, 0, 0, 0)
            layout.setSpacing(4)

            lbl = QLabel(label_text)
            lbl.setStyleSheet("font-size: 12px; font-weight: 500; color: #000000; border: none; background: transparent;")
            layout.addWidget(lbl)

            combo = QComboBox()
            combo.addItems(items)
            combo.setFixedHeight(32)
            combo.setMinimumWidth(130)
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
            layout.addWidget(combo)
            return widget

        top_bar.addWidget(create_filter("Date From", ["2026-8-19"]))
        top_bar.addWidget(create_filter("Date To", ["2026-8-19"]))
        top_bar.addWidget(create_filter("User", ["All Users", "John Doe", "Sarah Smith"]))
        top_bar.addWidget(create_filter("Department", ["All Departments", "Operational", "Sales", "IT"]))

        # Helper function for action buttons
        def create_action_btn(text: str) -> QWidget:
            container = QWidget()
            container.setStyleSheet("background: transparent;")
            layout = QVBoxLayout(container)
            layout.setContentsMargins(0, 0, 0, 0)
            layout.setSpacing(4)
            
            spacer = QLabel(" ")
            spacer.setStyleSheet("font-size: 12px; background: transparent;")
            layout.addWidget(spacer)

            btn = QPushButton(text)
            btn.setIcon(QIcon("assets/icon.jpg"))
            btn.setIconSize(btn.iconSize().scaled(16, 16, Qt.AspectRatioMode.KeepAspectRatio))
            btn.setFixedHeight(32)
            btn.setStyleSheet("""
                QPushButton {
                    background-color: #ffffff;
                    color: #000000;
                    border: 1px solid #d9d9d9;
                    padding: 0 15px;
                    font-size: 12px;
                    font-weight: 500;
                }
                QPushButton:hover {
                    background-color: #f9f9f9;
                }
            """)
            layout.addWidget(btn)
            return container

        top_bar.addWidget(create_action_btn("Exceptions"))
        top_bar.addWidget(create_action_btn("Attendance"))

        main_layout.addWidget(top_bar_widget)

        # ==========================================
        # 3. DATA TABLE (Raw Logs)
        # ==========================================
        table = QTableWidget()
        table.setColumnCount(6)
        table.setHorizontalHeaderLabels(["Date", "Time", "User ID", "User Name", "Department", "Status"])
        
        # Ensure table can shrink
        table.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        table.setMinimumHeight(100) 

        # Table Styling & Scrolling
        table.setShowGrid(False)
        table.setAlternatingRowColors(True)
        table.verticalHeader().setVisible(False)
        table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        
        table.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        table.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        
        table.setStyleSheet("""
            QTableWidget {
                background-color: #ffffff;
                alternate-background-color: #f2f2f2;
                border: none;
                outline: none;
            }
            QTableWidget::item {
                border-bottom: 1px solid #e0e0e0;
                padding: 8px;
                font-size: 12px;
                color: #000000;
            }
            QTableWidget::item:selected {
                background-color: #e8f0fe;
                color: #000000;
            }
            QHeaderView::section {
                background-color: #ffffff;
                color: #000000;
                font-weight: bold;
                font-size: 12px;
                border: none;
                border-bottom: 2px solid #d9d9d9;
                padding: 8px;
                text-align: left;
            }
        """)

        header = table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Interactive)
        header.setStretchLastSection(True)
        header.setDefaultAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        
        table.setColumnWidth(0, 120) 
        table.setColumnWidth(1, 100) 
        table.setColumnWidth(2, 100) 
        table.setColumnWidth(3, 150) 
        table.setColumnWidth(4, 150) 
        table.setColumnWidth(5, 120) 

        data = [
            ("2026-8-19", "9:00 AM", "0001", "John Doe", "Operational", "Check in"),
            ("2026-8-19", "5:00 PM", "0001", "John Doe", "Operational", "Check out"),
            ("2026-8-19", "9:00 AM", "0002", "Sarah Smith", "Accounts", "Check in"),
            ("2026-8-19", "5:00 PM", "0002", "Sarah Smith", "Accounts", "Check out"),
            ("2026-8-19", "9:00 AM", "0003", "Mike Johnson", "Sales", "Check in"),
            ("2026-8-19", "5:00 PM", "0003", "Mike Johnson", "Sales", "Check out"),
            ("2026-8-19", "9:00 AM", "0004", "Emily Brown", "IT", "Check in"),
            ("2026-8-19", "5:00 PM", "0004", "Emily Brown", "IT", "Check out"),
            ("2026-8-19", "9:00 AM", "0005", "Ahmad", "Operational", "Check in"),
            ("2026-8-19", "5:00 PM", "0005", "Ahmad", "Operational", "Check out"),
            ("2026-8-19", "9:00 AM", "0006", "Ali", "Operational", "Check in"),
            ("2026-8-19", "5:00 PM", "0006", "Ali", "Operational", "Check out"),
            ("2026-8-19", "9:00 AM", "0007", "Shoaib", "Operational", "Check in"),
        ]

        table.setRowCount(len(data))
        for row, (date, time, uid, name, dept, status) in enumerate(data):
            table.setItem(row, 0, QTableWidgetItem(date))
            table.setItem(row, 1, QTableWidgetItem(time))
            table.setItem(row, 2, QTableWidgetItem(uid))
            table.setItem(row, 3, QTableWidgetItem(name))
            table.setItem(row, 4, QTableWidgetItem(dept))
            table.setItem(row, 5, QTableWidgetItem(status))

        main_layout.addWidget(table, 1)

        # ==========================================
        # 4. PAGINATION FOOTER
        # ==========================================
        footer_layout = QHBoxLayout()
        footer_layout.setContentsMargins(0, 10, 0, 0)
        
        showing_lbl = QLabel("Showing 1-20 of 100")
        showing_lbl.setStyleSheet("font-size: 12px; color: #878787; border: none; background: transparent;")
        footer_layout.addWidget(showing_lbl)
        
        footer_layout.addStretch()
        
        btn_style = """
            QPushButton {
                background-color: #ffffff;
                color: #000000;
                border: 1px solid #d9d9d9;
                font-size: 14px;
                font-weight: bold;
                padding-bottom: 2px;
            }
            QPushButton:hover {
                background-color: #f9f9f9;
            }
        """
        
        left_btn = QPushButton("←")
        left_btn.setFixedSize(32, 32)
        left_btn.setStyleSheet(btn_style)
        footer_layout.addWidget(left_btn)
        
        right_btn = QPushButton("→")
        right_btn.setFixedSize(32, 32)
        right_btn.setStyleSheet(btn_style)
        footer_layout.addWidget(right_btn)

        main_layout.addLayout(footer_layout)

        # Set the content in the scroll area
        main_scroll.setWidget(scroll_content)
        content_layout = QVBoxLayout(self.content)
        content_layout.setContentsMargins(0, 0, 0, 0)
        content_layout.addWidget(main_scroll)