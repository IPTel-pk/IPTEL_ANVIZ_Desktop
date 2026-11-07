from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit
from app.settings import (
    ACCENT_COLOR,
    SECONDARY_COLOR,
    HIGHLIGHT_COLOR,
    GRAY_TEXT_COLOR
)

class InputField(QWidget):
    """
    ### InputField
    This widget creates a reusable labeled text field for forms across the application.
    """

    def __init__(
        self, text: str, placeholder: str = "", hidden: bool = False,
        disable: bool = False, parent=None
    ):
        """
        Initialize the input field widget.

        This method creates the label, text box, and styling for editable or read-only form inputs.
        """
        super().__init__(parent)

        # 1. Create the main vertical layout for the input field
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(4)

        # 2. Add the field label above the text field
        self.label = QLabel(text)
        self.label.setStyleSheet("""
            font-size: 12px; font-weight: bold;
            border: none; background: transparent;
        """)
        if text:
            layout.addWidget(self.label)
        else:
            self.label.setVisible(False)
            layout.setSpacing(0)

        # 3. Create the actual QLineEdit element
        self.line_edit = QLineEdit()
        self.line_edit.setPlaceholderText(placeholder)
        self.line_edit.setFixedHeight(28)

        # 4. Apply password mode if requested
        if hidden:
            self.line_edit.setEchoMode(QLineEdit.EchoMode.Password)

        # 5. Apply read-only styling when disabled is selected
        if disable:
            self.line_edit.setDisabled(True)
            self.line_edit.setStyleSheet(f"""
                QLineEdit {{
                    border: 1px solid {SECONDARY_COLOR};
                    padding: 0 8px;
                    font-size: 12px;
                    background-color: {HIGHLIGHT_COLOR};
                    color: {GRAY_TEXT_COLOR};
                }}
            """)
        else:
            self.line_edit.setStyleSheet(f"""
                QLineEdit {{
                    border: 1px solid {SECONDARY_COLOR};
                    padding: 0 8px;
                    font-size: 12px;
                    background-color: #ffffff;
                    color: #000000;
                }}
                QLineEdit:focus {{
                    border: 1px solid {ACCENT_COLOR};
                }}
            """)
        layout.addWidget(self.line_edit)

    def text(self) -> str:
        """
        Return the current text value from the field.
        """
        return self.line_edit.text()

    def set_text(self, text: str) -> None:
        """
        Set the displayed text of the field.
        """
        self.line_edit.setText(text)
