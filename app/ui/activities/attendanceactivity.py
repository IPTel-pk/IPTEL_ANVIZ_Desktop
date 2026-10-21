from typing import Callable
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QComboBox,
    QHBoxLayout,
    QHeaderView,
    QLabel,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
    QSizePolicy,
    QScrollArea, # Added QScrollArea
)

from app.ui.components.activity import Activity
from app.ui.activities.deviceactivity import FlowLayout


class AttendanceActivity(Activity):
    """**Attendance Page**"""
    def __init__(self, navigate: Callable, parent=None) -> None:
        """Initialize the Attendance Page Activity"""
        super().__init__(parent=parent, activity="Attendance", navigate=navigate)

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
        # 2. TOP FILTER BAR (RESPONSIVE)
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

            # Label above
            lbl = QLabel(label_text)
            lbl.setStyleSheet("font-size: 12px; font-weight: 500; color: #000000; border: none; background: transparent;")
            layout.addWidget(lbl)

            # Compact Select Box
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

        # Add the 6 Filters from the screenshot
        top_bar.addWidget(create_filter("Date From", ["2026-8-19"]))
        top_bar.addWidget(create_filter("Date To", ["2026-8-20"]))
        top_bar.addWidget(create_filter("User", ["All Users", "John Doe", "Sarah Smith"]))
        top_bar.addWidget(create_filter("Department", ["All Departments", "Operational", "Accounts", "Sales", "IT"]))
        top_bar.addWidget(create_filter("Template", ["Monthly HR Export", "Daily Summary", "Custom"]))
        top_bar.addWidget(create_filter("Export", ["PDF", "Excel", "CSV"]))

        main_layout.addWidget(top_bar_widget)

        # ==========================================
        # 3. DATA TABLE (Attendance Summary)
        # ==========================================
        table = QTableWidget()
        table.setColumnCount(7)
        table.setHorizontalHeaderLabels(["Date", "Employee", "Department", "Check In", "Check Out", "Total Hours", "Status"])
        
        # Ensure table can shrink
        table.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        table.setMinimumHeight(100) 
        
        # Table Styling & Scrolling
        table.setShowGrid(False)
        table.setAlternatingRowColors(True)
        table.verticalHeader().setVisible(False)
        table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        
        # Enable Scrollbars
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

        # Configure columns
        header = table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Interactive)
        header.setStretchLastSection(True) 
        header.setDefaultAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        
        # Set default column widths
        table.setColumnWidth(0, 100) # Date
        table.setColumnWidth(1, 150) # Employee
        table.setColumnWidth(2, 130) # Department
        table.setColumnWidth(3, 100) # Check In
        table.setColumnWidth(4, 100) # Check Out
        table.setColumnWidth(5, 120) # Total Hours
        table.setColumnWidth(6, 100) # Status

        # Dummy Data
        data = [
            ("2026-8-19", "John Doe", "Operational", "9:00 AM", "5:00 PM", "8 hr", "Present"),
            ("2026-8-20", "John Doe", "Operationalajshkioeufhnwf", "9:00 AM", "1:00 PM", "4 hr", "Half Day"),
            ("2026-8-19", "Sarah Smith", "Accounts", "9:05 AM", "5:00 PM", "7 hr 55 min", "Present"),
            ("2026-8-20", "Sarah Smith", "Accounts", "10:00 AM", "5:00 PM", "6 hr", "Late"),
            ("2026-8-19", "Mike Johnson", "Sales", "9:00 AM", "5:00 PM", "8 hr", "Present"),
            ("2026-8-20", "Mike Johnson", "Sales", "9:10 AM", "5:00 PM", "7 hr 50 min", "Present"),
            ("2026-8-19", "Emily Brown", "IT", "9:00 AM", "5:00 PM", "8 hr", "Present"),
            ("2026-8-20", "Emily Brown", "IT", "9:00 AM", "4:45 PM", "7 hr 45 min", "Present"),
            ("2026-8-19", "Ahmad", "Operational", "9:00 AM", "5:00 PM", "8 hr", "Present"),
            ("2026-8-20", "Ahmad", "Operational", "-", "-", "-", "Leave"),
            ("2026-8-19", "Ali", "Operational", "9:00 AM", "5:00 PM", "8 hr", "Present"),
            ("2026-8-20", "Ali", "Operational", "9:00 AM", "5:00 PM", "8 hr", "Present"),
            ("2026-8-19", "Shoaib", "Operational", "-", "-", "-", "Absent"),
        ]

        table.setRowCount(len(data))
        for row, (date, emp, dept, check_in, check_out, total, status) in enumerate(data):
            table.setItem(row, 0, QTableWidgetItem(date))
            table.setItem(row, 1, QTableWidgetItem(emp))
            table.setItem(row, 2, QTableWidgetItem(dept))
            table.setItem(row, 3, QTableWidgetItem(check_in))
            table.setItem(row, 4, QTableWidgetItem(check_out))
            table.setItem(row, 5, QTableWidgetItem(total))
            table.setItem(row, 6, QTableWidgetItem(status))

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