from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QMouseEvent
from PySide6.QtWidgets import (
    QCheckBox,
    QHBoxLayout,
    QLabel,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)
from app.settings import ACCENT_COLOR, SECONDARY_COLOR, GRAY_TEXT_COLOR

class UserCard(QWidget):
    """
    ### UserCard
    This widget represents a selectable user item with a profile image, name, department, and checkbox-based selection state.
    """

    def __init__(self, name: str, department: str, parent=None):
        """
        Initialize the user card widget.

        This method constructs the user row layout, profile icon, labels, and checkbox used for selection.
        """
        super().__init__(parent)
        self.setFixedHeight(70)
        self.setMinimumWidth(250)
        self.setMaximumWidth(350)
        self.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed
        )
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setCursor(Qt.CursorShape.PointingHandCursor)

        # 1. Create the main horizontal layout for the user row
        layout = QHBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(5)

        # 2. Add the selection checkbox on the left of the card
        self.checkbox = QCheckBox()
        self.checkbox.setStyleSheet("border: none; background: transparent;")
        self.checkbox.stateChanged.connect(self._update_card_style)
        layout.addWidget(
            self.checkbox,
            alignment=Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft
        )

        # 3. Add the user avatar image
        icon_label = QLabel()
        pixmap = QPixmap("assets/user.png")
        if not pixmap.isNull():
            icon_label.setPixmap(pixmap.scaled(
                50, 50,
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            ))
        icon_label.setFixedSize(50, 50)
        icon_label.setStyleSheet("border: none; background: transparent;")
        layout.addWidget(icon_label)

        # 4. Add the name and department text block
        text_layout = QVBoxLayout()
        text_layout.setSpacing(2)
        text_layout.setAlignment(Qt.AlignmentFlag.AlignVCenter)

        name_label = QLabel(name)
        name_label.setStyleSheet("""
            font-size: 16px; font-weight: bold; color: #000000;
            border: none; background: transparent;
        """)
        name_label.setTextInteractionFlags(
            Qt.TextInteractionFlag.TextSelectableByMouse
        )
        dept_label = QLabel(department)
        dept_label.setStyleSheet(f"""
            font-size: 13px; color: {GRAY_TEXT_COLOR};
            border: none; background: transparent;
        """)
        dept_label.setTextInteractionFlags(
            Qt.TextInteractionFlag.TextSelectableByMouse
        )

        text_layout.addWidget(name_label)
        text_layout.addWidget(dept_label)
        layout.addLayout(text_layout)

        # 5. Push the content to the left edge of the card
        layout.addStretch()

        # 6. Apply the initial border style based on the checkbox state
        self._update_card_style()

    def _update_card_style(self) -> None:
        """
        Update the card border color to reflect the selection state.

        When checked, the card uses the accent border color; otherwise it stays on the default secondary border.
        """
        if self.checkbox.isChecked():
            border_color = ACCENT_COLOR
        else:
            border_color = SECONDARY_COLOR
        self.setStyleSheet(f"""
            UserCard {{
                background-color: #ffffff;
                border: 1px solid {border_color};
            }}
        """)

    def mousePressEvent(self, event: QMouseEvent) -> None:
        """
        Toggle the selection state when the card is clicked.

        This allows users to select a card without needing to click on the tiny checkbox itself.
        """
        if event.button() == Qt.MouseButton.LeftButton:
            child = self.childAt(event.pos())

            if child != self.checkbox:
                self.checkbox.setChecked(not self.checkbox.isChecked())

        super().mousePressEvent(event)
