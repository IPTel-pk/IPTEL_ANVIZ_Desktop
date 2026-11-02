from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit
from app.settings import (
    ACCENT_COLOR,
    SECONDARY_COLOR,
    HIGHLIGHT_COLOR,
    GRAY_TEXT_COLOR
)

class InputField(QWidget):
    """Reusable custom input field with a label on top."""
    def __init__(
        self, text: str, placeholder: str = "", hidden: bool = False,
        disable: bool = False, parent=None
    ):
        super().__init__(parent)

        # Main layout for this widget
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(4)

        # Label
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

        # Input Field
        self.line_edit = QLineEdit()
        self.line_edit.setPlaceholderText(placeholder)
        self.line_edit.setFixedHeight(28)

        # Handle 'hidden' parameter (for passwords)
        if hidden:
            self.line_edit.setEchoMode(QLineEdit.EchoMode.Password)

        # Handle 'disable' parameter
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

    # Convenience methods to get/set values
    def text(self) -> str:
        return self.line_edit.text()

    def set_text(self, text: str) -> None:
        self.line_edit.setText(text)
