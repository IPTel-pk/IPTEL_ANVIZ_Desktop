from typing import Callable
from PySide6.QtWidgets import (
    QSizePolicy,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
)
from app.ui.components.activity import Activity
from app.ui.components.flowlayout import FlowLayout
from app.ui.components.toolbarbutton import ToolbarButton
from app.ui.components.selectfield import SelectField
from app.ui.components.standardtable import StandardTable
from app.ui.components.paginationfooter import PaginationFooter
from data.report import data

class ReportActivity(Activity):
    """**Report Page**"""
    def __init__(self, navigate: Callable, parent=None) -> None:
        """Initialize the Report Page Activity"""
        super().__init__(parent=parent, activity="Report", navigate=navigate)

        # 1. Safely get or create the main layout directly on self.content this removes the need for an outer QScrollArea
        main_layout = self.content.layout()
        if main_layout is None:
            main_layout = QVBoxLayout(self.content)
        main_layout.setContentsMargins(0, 30, 0, 0)
        main_layout.setSpacing(20)

        # 2. TOP FILTER BAR & ACTION BUTTONS
        tool_bar_widget = QWidget()
        tool_bar_widget.setStyleSheet("background: transparent;")
        tool_bar_widget.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed
        )
        tool_bar = FlowLayout(
            tool_bar_widget, margin=0, h_spacing=15, v_spacing=15
        )
        # Add Filters using SelectField
        tool_bar.addWidget(SelectField(
            "Date From", ["2026-8-19"]
        ))
        tool_bar.addWidget(SelectField(
            "Date To", ["2026-8-19"]
        ))
        tool_bar.addWidget(SelectField(
            "User", ["All Users", "John Doe", "Sarah Smith"]
        ))
        tool_bar.addWidget(SelectField(
            "Department", ["All Departments", "Operational", "Sales", "IT"]
        ))
        # Add Action Buttons directly
        tool_bar.addWidget(ToolbarButton(
            "Exceptions", "assets/edit.png"
        ))
        tool_bar.addWidget(ToolbarButton(
            "Attendance", "assets/attendance-black.png"
        ))
        main_layout.addWidget(tool_bar_widget)

        # 3. DATA TABLE (Raw Logs)
        table = StandardTable([
            "Date", "Time", "User ID", "User Name", "Department", "Status"
        ])
        table.setMinimumHeight(5)

        # Set column widths
        table.setColumnWidth(0, 120) 
        table.setColumnWidth(1, 100) 
        table.setColumnWidth(2, 100) 
        table.setColumnWidth(3, 150) 
        table.setColumnWidth(4, 150) 
        table.setColumnWidth(5, 120)

        table.setRowCount(len(data))
        for row, (date, time, uid, name, dept, status) in enumerate(data):
            table.setItem(row, 0, QTableWidgetItem(date))
            table.setItem(row, 1, QTableWidgetItem(time))
            table.setItem(row, 2, QTableWidgetItem(uid))
            table.setItem(row, 3, QTableWidgetItem(name))
            table.setItem(row, 4, QTableWidgetItem(dept))
            table.setItem(row, 5, QTableWidgetItem(status))
        main_layout.addWidget(table)

        # 4. PAGINATION FOOTER
        footer = PaginationFooter("Showing 1-20 of 100")
        main_layout.addWidget(footer)
