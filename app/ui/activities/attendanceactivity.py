from typing import Callable
from PySide6.QtWidgets import (
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
    QSizePolicy,
)
from app.ui.components.activity import Activity
from app.ui.components.flowlayout import FlowLayout
from app.ui.components.selectfield import SelectField
from app.ui.components.paginationfooter import PaginationFooter
from app.ui.components.standardtable import StandardTable
from data.attendance import data

class AttendanceActivity(Activity):
    """**Attendance Page**"""
    def __init__(self, navigate: Callable, parent=None) -> None:
        """Initialize the Attendance Page Activity"""
        super().__init__(
            parent=parent, activity="Attendance", navigate=navigate
        )
        # 1. Create the main layout directly on self.content so the type is explicit for PySide6/Pylance
        main_layout = QVBoxLayout(self.content)
        main_layout.setContentsMargins(0, 30, 0, 0)
        main_layout.setSpacing(30)

        # 2. TOOL BAR
        tool_bar_widget = QWidget()
        tool_bar_widget.setStyleSheet("background: transparent;")
        tool_bar_widget.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed
        )
        tool_bar = FlowLayout(
            tool_bar_widget,
            margin=0,
            h_spacing=15,
            v_spacing=15
        )
        tool_bar.addWidget(SelectField(
            "Date From", ["2026-8-19"]
        ))
        tool_bar.addWidget(SelectField(
            "Date To", ["2026-8-20"]
        ))
        tool_bar.addWidget(SelectField(
            "User", ["All Users", "John Doe", "Sarah Smith"]
        ))
        tool_bar.addWidget(SelectField(
            "Department", [
                "All Departments", "Operational", "Accounts", "Sales", "IT"
            ]
        ))
        tool_bar.addWidget(SelectField(
            "Template", ["Monthly HR Export", "Daily Summary", "Custom"]
        ))
        tool_bar.addWidget(SelectField(
            "Export", ["PDF", "Excel", "CSV"]
        ))
        main_layout.addWidget(tool_bar_widget)

        # 3. DATA TABLE
        table = StandardTable([
            "Date", "Employee", "Department", "Check In",
            "Check Out", "Total Hours", "Status"
        ])
        table.setMinimumHeight(5)

        # Set specific column widths
        table.setColumnWidth(0, 100) # Date
        table.setColumnWidth(1, 150) # Employee
        table.setColumnWidth(2, 130) # Department
        table.setColumnWidth(3, 100) # Check In
        table.setColumnWidth(4, 100) # Check Out
        table.setColumnWidth(5, 120) # Total Hours
        table.setColumnWidth(6, 100) # Status

        table.setRowCount(len(data))
        for row, (
            date, emp, dept, check_in, check_out, total, status
        ) in enumerate(data):
            table.setItem(row, 0, QTableWidgetItem(date))
            table.setItem(row, 1, QTableWidgetItem(emp))
            table.setItem(row, 2, QTableWidgetItem(dept))
            table.setItem(row, 3, QTableWidgetItem(check_in))
            table.setItem(row, 4, QTableWidgetItem(check_out))
            table.setItem(row, 5, QTableWidgetItem(total))
            table.setItem(row, 6, QTableWidgetItem(status))
        main_layout.addWidget(table)

        # 4. PAGINATION FOOTER
        footer = PaginationFooter("Showing 1-20 of 100")
        main_layout.addWidget(footer)
