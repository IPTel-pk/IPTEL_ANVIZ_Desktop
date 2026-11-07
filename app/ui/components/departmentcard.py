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
from app.settings import ACCENT_COLOR, SECONDARY_COLOR

class DepartmentCard(QWidget):
    """
    ### DepartmentCard
    This widget displays a department summary card with a checkbox, icon, and basic schedule information for selection and editing.
    """

    def __init__(
        self, name: str, start_time: str, off_time: str,
        working_days: str, parent=None
    ):
        """
        Initialize the department card.

        This method builds the card layout, adds the department name and working schedule, and hooks the checkbox to the card style update.
        """
        super().__init__(parent)
        self.setMinimumWidth(250)
        self.setMaximumWidth(300)
        self.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed
        )
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setCursor(Qt.CursorShape.PointingHandCursor)

        # 1. Create the main vertical layout for the card
        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(5)

        # 2. Build the header row with the checkbox and department name
        top_row = QHBoxLayout()
        top_row.setSpacing(5)

        self.checkbox = QCheckBox()
        self.checkbox.setStyleSheet("border: none; background: transparent;")

        # 3. Connect the checkbox to the style update method
        self.checkbox.stateChanged.connect(self._update_card_style)
        top_row.addWidget(self.checkbox)

        name_label = QLabel(name)
        name_label.setStyleSheet("""
            font-size: 14px; font-weight: bold; color: #000000;
            border: none; background: transparent;
        """)
        name_label.setTextInteractionFlags(
            Qt.TextInteractionFlag.TextSelectableByMouse
        )
        top_row.addWidget(name_label)
        top_row.addStretch()
        layout.addLayout(top_row)

        # 4. Build the bottom area with the icon and schedule details
        bottom_row = QHBoxLayout()
        bottom_row.setSpacing(10)

        # 5. Add the department icon placeholder
        icon_label = QLabel()
        pixmap = QPixmap("assets/group.png")
        if not pixmap.isNull():
            icon_label.setPixmap(pixmap.scaled(
                45, 45, 
                Qt.AspectRatioMode.KeepAspectRatio, 
                Qt.TransformationMode.SmoothTransformation
            ))
        icon_label.setFixedSize(45, 45)
        icon_label.setStyleSheet("border: none; background: transparent;")
        bottom_row.addWidget(icon_label)

        # 6. Add the internal detail labels for start time, off time, and working days
        details_layout = QVBoxLayout()
        details_layout.setSpacing(2)
        details_layout.setAlignment(Qt.AlignmentFlag.AlignVCenter)

        start_lbl = QLabel(f"Start: {start_time}")
        start_lbl.setStyleSheet("""
            font-size: 12px; color: #000000; border: none;
            background: transparent;
        """)
        start_lbl.setTextInteractionFlags(
            Qt.TextInteractionFlag.TextSelectableByMouse
        )
        off_lbl = QLabel(f"Off: {off_time}")
        off_lbl.setStyleSheet(
            """
            font-size: 12px; color: #000000; border: none;
            background: transparent;
        """)
        off_lbl.setTextInteractionFlags(
            Qt.TextInteractionFlag.TextSelectableByMouse
        )
        days_lbl = QLabel(f"Working Days: {working_days}")
        days_lbl.setStyleSheet("""
            font-size: 12px; color: #000000; border: none;
            background: transparent;
        """)
        days_lbl.setTextInteractionFlags(
            Qt.TextInteractionFlag.TextSelectableByMouse
        )
        details_layout.addWidget(start_lbl)
        details_layout.addWidget(off_lbl)
        details_layout.addWidget(days_lbl)

        bottom_row.addLayout(details_layout)
        bottom_row.addStretch()

        layout.addLayout(bottom_row)
        self._update_card_style()

    def _update_card_style(self) -> None:
        """
        Update the card border based on whether the department is selected.

        A checked card uses the accent color to stand out, while an unchecked card keeps the normal secondary border.
        """
        if self.checkbox.isChecked():
            border_color = ACCENT_COLOR
        else: border_color = SECONDARY_COLOR
        self.setStyleSheet(f"""
            DepartmentCard {{
                background-color: #ffffff;
                border: 1px solid {border_color};
            }}
        """)

    def mousePressEvent(self, event: QMouseEvent) -> None:
        """
        Toggle the checkbox when the card itself is clicked.

        This keeps the widget easy to select without requiring the user to click the tiny checkbox icon directly.
        """
        if event.button() == Qt.MouseButton.LeftButton:
            # Check if the user clicked directly on the checkbox
            child = self.childAt(event.pos())

            # If clicked on the card but NOT on the checkbox itself, toggle it manually
            if child != self.checkbox:
                self.checkbox.setChecked(not self.checkbox.isChecked())
        super().mousePressEvent(event)
