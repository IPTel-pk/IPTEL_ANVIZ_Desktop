from typing import Callable
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (
    QComboBox,
    QHBoxLayout,
    QHeaderView,
    QLabel,
    QLineEdit,
    QPushButton,
    QRadioButton,
    QSizePolicy,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
    QScrollArea, # Imported QScrollArea
)
from app.ui.components.activity import Activity
from app.ui.components.flowlayout import FlowLayout
from data.execption import data

class ExceptionActivity(Activity):
    """**Exception Page**"""
    def __init__(self, navigate: Callable, parent=None) -> None:
        """Initialize the Exception Page Activity"""
        super().__init__(parent=parent, activity="Exception", navigate=navigate)

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
        # 2. TOP FILTER BAR & ACTION BUTTONS
        # ==========================================
        top_bar_widget = QWidget()
        top_bar_widget.setStyleSheet("background: transparent;")
        top_bar_widget.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        
        top_bar = FlowLayout(top_bar_widget, margin=0, h_spacing=15, v_spacing=15)

        # Helper for dropdowns
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
            combo.setMinimumWidth(140)
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

        # Add Filters
        top_bar.addWidget(create_filter("Date", ["2026-8-19"]))
        top_bar.addWidget(create_filter("User", ["All Users", "John Doe", "Sarah Smith"]))
        top_bar.addWidget(create_filter("Department", ["All Departments", "Operational", "Accounts", "Sales", "IT"]))

        # Helper for action buttons
        def create_action_btn(text: str) -> QWidget:
            container = QWidget()
            container.setStyleSheet("background: transparent;")
            layout = QVBoxLayout(container)
            layout.setContentsMargins(0, 0, 0, 0)
            layout.setSpacing(4)
            
            # Spacer to push button down and align with comboboxes
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

        # Add Action Buttons
        top_bar.addWidget(create_action_btn("Save"))
        top_bar.addWidget(create_action_btn("Attendance"))

        main_layout.addWidget(top_bar_widget)

        # ==========================================
        # 3. DATA TABLE (Exception Management)
        # ==========================================
        table = QTableWidget()
        table.setColumnCount(6)
        table.setHorizontalHeaderLabels(["User ID", "User Name", "Department", "Status", "Check in", "Check out"])
        
        table.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        table.setMinimumHeight(100) # FIX: Allows window to shrink
        
        table.setShowGrid(False)
        table.setAlternatingRowColors(True)
        table.verticalHeader().setVisible(False)
        table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        
        # Kept the row height exactly as you requested
        table.verticalHeader().setDefaultSectionSize(45)
        
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
        
        # Set column widths
        table.setColumnWidth(0, 80)  # User ID
        table.setColumnWidth(1, 150) # User Name
        table.setColumnWidth(2, 120) # Department
        table.setColumnWidth(3, 250) # Status (Needs space for radios)
        table.setColumnWidth(4, 120) # Check in
        table.setColumnWidth(5, 120) # Check out

        # --- Cell Widget Helpers ---
        def create_radio_widget() -> QWidget:
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

        def create_input_widget() -> QWidget:
            w = QWidget()
            w.setStyleSheet("background: transparent;")
            layout = QHBoxLayout(w)
            layout.setContentsMargins(5, 5, 5, 5)
            
            le = QLineEdit()
            le.setFixedHeight(28)
            le.setStyleSheet("""
                QLineEdit {
                    border: 1px solid #d9d9d9;
                    background-color: #ffffff;
                    font-size: 12px;
                    padding: 0 4px;
                }
            """)
            layout.addWidget(le)
            return w

        table.setRowCount(len(data))
        for row, (uid, name, dept) in enumerate(data):
            # Standard text columns
            table.setItem(row, 0, QTableWidgetItem(uid))
            table.setItem(row, 1, QTableWidgetItem(name))
            table.setItem(row, 2, QTableWidgetItem(dept))
            
            # Custom cell widgets
            table.setCellWidget(row, 3, create_radio_widget())
            table.setCellWidget(row, 4, create_input_widget())
            table.setCellWidget(row, 5, create_input_widget())

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

        # Set the content in the scroll area and add to the main content layout
        main_scroll.setWidget(scroll_content)
        content_layout = QVBoxLayout(self.content)
        content_layout.setContentsMargins(0, 0, 0, 0)
        content_layout.addWidget(main_scroll)