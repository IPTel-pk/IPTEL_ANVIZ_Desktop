from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QTableWidget,
    QHeaderView,
    QSizePolicy,
)
from app.settings import SECONDARY_COLOR, HIGHLIGHT_COLOR

class StandardTable(QTableWidget):
    """
    ### StandardTable
    This widget provides the app-wide table style used for attendance, reports, and other summary screens.
    """

    def __init__(self, columns: list[str], parent=None):
        """
        Initialize the standardized data table.

        This method sets the columns, locking behavior, and styling used consistently across all report tables.
        """
        super().__init__(parent)

        # 1. Set up the table columns and headers
        self.setColumnCount(len(columns))
        self.setHorizontalHeaderLabels(columns)

        self.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding
        )
        self.setMinimumHeight(5)

        # 2. Prevent editing and selection for read-only display tables
        self.setSelectionMode(QTableWidget.SelectionMode.NoSelection)
        self.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)

        # 3. Apply the standard visual styling
        self.setShowGrid(False)
        self.setAlternatingRowColors(True)
        self.verticalHeader().setVisible(False)

        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.setHorizontalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAsNeeded
        )
        self.setStyleSheet(f"""
            QTableWidget {{
                background-color: #ffffff;
                alternate-background-color: {HIGHLIGHT_COLOR};
                border: none;
                outline: none;
            }}
            QTableWidget::item {{
                border-bottom: 1px solid #e0e0e0;
                padding: 8px;
                font-size: 12px;
                color: #000000;
            }}
            QHeaderView::section {{
                background-color: #ffffff;
                color: #000000;
                font-weight: bold;
                font-size: 12px;
                border: none;
                border-bottom: 2px solid {SECONDARY_COLOR};
                padding: 8px;
                text-align: left;
            }}
        """)

        # 4. Configure the header resizing and alignment options
        header = self.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Interactive)
        header.setStretchLastSection(True)
        header.setDefaultAlignment(
            Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter
        )
