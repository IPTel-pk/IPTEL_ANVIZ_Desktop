from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (
    QHBoxLayout,
    QPushButton,
    QWidget,
)

class FileItemActions(QWidget):
    """
    ### FileItemActions
    This widget provides quick action buttons for each file row, including open-folder and delete actions.
    """

    def __init__(
        self, button_size: int = 24, button_spacing: int = 10, parent=None
    ):
        """
        Initialize the file action widget.

        This method creates the row action buttons and aligns them to the right side of each file entry.
        """
        super().__init__(parent)
        self.setStyleSheet("border: none; background: transparent;")

        # 1. Create the horizontal layout for the action buttons
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(button_spacing)
        layout.setAlignment(
            Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter
        )

        # 2. Add the folder action button
        self.btn1 = QPushButton()
        self.btn1.setIcon(QIcon("assets/folder.png"))
        self.btn1.setCursor(Qt.CursorShape.PointingHandCursor)
        self.btn1.setStyleSheet("border: none; background: transparent;")
        self.btn1.setFixedSize(button_size, button_size)
        self.btn1.setIconSize(QSize(button_size, button_size))
        layout.addWidget(self.btn1)

        # 3. Add the delete action button
        self.btn2 = QPushButton()
        self.btn2.setIcon(QIcon("assets/trash.png"))
        self.btn2.setCursor(Qt.CursorShape.PointingHandCursor)
        self.btn2.setStyleSheet("border: none; background: transparent;")
        self.btn2.setFixedSize(button_size, button_size)
        self.btn2.setIconSize(QSize(button_size, button_size))
        layout.addWidget(self.btn2)
