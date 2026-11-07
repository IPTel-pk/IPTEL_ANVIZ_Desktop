from typing import Callable
from PySide6.QtCore import Qt, QEvent
from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
    QTableWidget,
    QTableWidgetItem,
    QHeaderView,
)
from app.ui.components.activity import Activity
from app.ui.components.largebutton import LargeButton
from app.ui.components.fileitemaction import FileItemActions
from app.settings import SECONDARY_COLOR
from data.launcher import files_data

class LauncherActivity(Activity):
    """
    ### Launcher Activity
    This widget builds the launcher screen for opening or creating files and displays a recent files table with quick actions for each item.
    """

    def __init__(self, navigate: Callable, parent=None) -> None:
        """
        Initialize the launcher page.

        This method creates the action buttons at the top and sets up the recent files table with file metadata and action controls.
        """
        super().__init__(
            parent=parent, activity="Launcher", navigate=navigate
        )

        # 1. Main Layout
        # This sets up the vertical layout used for the launcher page and reserves space for the top action buttons and recent files panel.
        main_layout = QVBoxLayout(self.content)
        main_layout.setContentsMargins(0, 30, 0, 0)
        main_layout.setSpacing(30)

        # 1. Top Buttons
        top_buttons_layout = QHBoxLayout()
        top_buttons_layout.setSpacing(30)

        create_btn = LargeButton(
            "Create New File", "(.ipatt)", "assets/add.png"
        )
        open_btn = LargeButton(
            "Open Existing File", "Browse Files", "assets/folder.png"
        )

        top_buttons_layout.addWidget(create_btn)
        top_buttons_layout.addWidget(open_btn)
        main_layout.addLayout(top_buttons_layout)

        # 2. Recent Files table
        recent_files_box = QWidget()
        recent_files_box.setObjectName("recentFilesBox")
        recent_files_box.setStyleSheet(f"""
            QWidget#recentFilesBox {{
                background-color: #ffffff;
                border: 1px solid {SECONDARY_COLOR};
            }}
        """)

        recent_files_layout = QVBoxLayout(recent_files_box)
        recent_files_layout.setContentsMargins(0, 0, 0, 0)
        recent_files_layout.setSpacing(0)

        # 2.1. Header Label
        header_label = QLabel("Recent Files")
        header_label.setFixedHeight(40)
        header_label.setStyleSheet(f"""
            font-size: 16px;
            font-weight: bold;
            padding-left: 15px;
            border-bottom: 1px solid {SECONDARY_COLOR};
            background-color: transparent;
        """)
        recent_files_layout.addWidget(header_label)

        # 2.2 Table Setup
        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(
            ["File Name", "Path", "Actions"]
        )
        # Make table expand fully
        self.table.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding
        )
        self.table.setMinimumHeight(50) # Allows window to shrink

        # Table Styling
        self.table.setShowGrid(False)
        self.table.setAlternatingRowColors(True)
        self.table.verticalHeader().setVisible(False)
        self.table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.table.setSelectionMode(QTableWidget.SelectionMode.NoSelection)
        self.table.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.table.setStyleSheet("""
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
        """)

        # Column Resizing
        header = self.table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Interactive)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.Fixed)
        self.table.setColumnWidth(2, 100)
        header.setDefaultAlignment(
            Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter
        )
        self.table.setRowCount(len(files_data))
        for row, (name, path) in enumerate(files_data):
            # Name
            name_item = QTableWidgetItem(name)
            name_item.setToolTip(name)
            self.table.setItem(row, 0, name_item)

            # Path
            path_item = QTableWidgetItem(path)
            path_item.setToolTip(path)
            path_item.setForeground(Qt.GlobalColor.gray)
            self.table.setItem(row, 1, path_item)

            # Actions
            actions_widget = FileItemActions(
                button_size=20, button_spacing=15
            )
            self.table.setCellWidget(row, 2, actions_widget)

        # Click and Cursor Logic
        self.table.setMouseTracking(True)
        self.table.cellEntered.connect(self._on_cell_hover)
        self.table.cellClicked.connect(self._on_cell_clicked)
        self.table.cellDoubleClicked.connect(self._on_cell_double_clicked)
        self.table.viewport().installEventFilter(self)

        recent_files_layout.addWidget(self.table)
        main_layout.addWidget(recent_files_box, 1)

    def _on_cell_hover(self, row: int, column: int) -> None:
        """
        Update the cursor when the mouse moves over a table cell.

        File name and path cells show a pointer cursor, while action cells keep the default arrow appearance.
        """
        if column in (0, 1):
            self.table.viewport().setCursor(
                Qt.CursorShape.PointingHandCursor
            )
        else:
            self.table.viewport().setCursor(Qt.CursorShape.ArrowCursor)

    def _on_cell_clicked(self, row: int, column: int) -> None:
        """
        Handle a single click in the recent files table.

        Clicking a file name or path prints the selected file for the current interaction behavior.
        """
        if column in (0, 1):
            item = self.table.item(row, 0)
            if item is None:
                return
            file_name = item.text()
            print(f"Clicked: {file_name}")

    def _on_cell_double_clicked(self, row: int, column: int) -> None:
        """
        Handle a double-click on a file entry.

        This method is used to trigger the open action for a selected recent file.
        """
        if column in (0, 1):
            item = self.table.item(row, 0)
            if item is None:
                return
            file_name = item.text()
            print(f"Double-clicked: {file_name}")

    def eventFilter(self, source, event) -> bool:
        """
        Reset the cursor when the mouse leaves the table viewport.

        This keeps pointer behavior consistent for interactive cells and allows the cursor to return to its default state.
        """
        if (source == self.table.viewport() and
            event.type() == QEvent.Type.Leave):
            self.table.viewport().setCursor(Qt.CursorShape.ArrowCursor)
        return super().eventFilter(source, event)
