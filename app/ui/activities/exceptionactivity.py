from typing import Callable
from PySide6.QtWidgets import (
    QAbstractScrollArea,
    QHBoxLayout,
    QRadioButton,
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
from app.ui.components.inputfield import InputField
from data.execption import data

class ExceptionActivity(Activity):
    """
    ### Exception Activity
    This widget creates the exception review screen where attendance records can be validated, adjusted, and saved with user, department, and status filters.
    """

    def __init__(self, navigate: Callable, parent=None) -> None:
        """
        Initialize the exception page activity.

        This method builds the filter toolbar, exception table, radio status controls, text input cells, and the final pagination section.
        """
        super().__init__(
            parent=parent, activity="Exception", navigate=navigate
        )

        # 1. Main Layout
        # This creates or reuses the main content layout that holds the tool bar, table, and pagination footer for the exception screen.
        main_layout = self.content.layout()
        if main_layout is None:
            main_layout = QVBoxLayout(self.content)
        
        main_layout.setContentsMargins(0, 30, 0, 0)
        main_layout.setSpacing(20)

        # 1. Tool Bar
        tool_bar_widget = QWidget()
        tool_bar_widget.setStyleSheet("background: transparent;")
        tool_bar_widget.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed
        )
        tool_bar = FlowLayout(
            tool_bar_widget, margin=0, h_spacing=15, v_spacing=15
        )
        tool_bar.addWidget(SelectField(
            "Date", ["2026-8-19"]
        ))
        tool_bar.addWidget(SelectField(
            "User", ["All Users", "John Doe", "Sarah Smith"]
        ))
        tool_bar.addWidget(SelectField(
            "Department", [
                "All Departments", "Operational", "Accounts", "Sales", "IT"
            ]
        ))
        tool_bar.addWidget(ToolbarButton(
            "Save", "assets/add.png"
        ))
        tool_bar.addWidget(ToolbarButton(
            "Attendance", "assets/attendance-black.png"
        ))
        main_layout.addWidget(tool_bar_widget)

        # 2. DATA TABLE
        table = StandardTable([
            "User ID", "User Name", "Department",
            "Status", "Check in", "Check out"
        ])

        # Ignore contents when calculating size hint
        table.setSizeAdjustPolicy(
            QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored
        )
        table.setMinimumHeight(50)
        table.verticalHeader().setDefaultSectionSize(52)
        table.setColumnWidth(0, 80)
        table.setColumnWidth(1, 150)
        table.setColumnWidth(2, 120)
        table.setColumnWidth(3, 250)
        table.setColumnWidth(4, 120)
        table.setColumnWidth(5, 120)

        def create_radio_widget() -> QWidget:
            """
            **Radio Buttons**

            Radio widget remains as a helper since there's no reusable RadioField component yet
            """
            w = QWidget()
            w.setStyleSheet("background: transparent;")
            layout = QHBoxLayout(w)
            layout.setContentsMargins(0, 0, 0, 0)
            layout.setSpacing(15)
            for text in ["Present", "Absent", "Leave"]:
                rb = QRadioButton(text)
                rb.setStyleSheet("font-size: 11px; color: #000000;")
                layout.addWidget(rb)
            return w

        table.setRowCount(len(data))
        for row, (uid, name, dept) in enumerate(data):
            table.setItem(row, 0, QTableWidgetItem(uid))
            table.setItem(row, 1, QTableWidgetItem(name))
            table.setItem(row, 2, QTableWidgetItem(dept))
            table.setCellWidget(row, 3, create_radio_widget())
            
            # Replaced create_input_widget with the InputField component passed empty string "" for the label to keep it compact in the table cell
            table.setCellWidget(row, 4, InputField(text="", placeholder=""))
            table.setCellWidget(row, 5, InputField(text="", placeholder=""))
        main_layout.addWidget(table)

        # 3. PAGINATION FOOTER
        footer = PaginationFooter("Showing 1-20 of 100")
        main_layout.addWidget(footer)
