from PySide6.QtWidgets import (
    QLabel,
    QVBoxLayout,
    QWidget,
    QComboBox,
    QCompleter,
)
from PySide6.QtCore import Qt, QEvent, QSortFilterProxyModel
from app.settings import SECONDARY_COLOR

class NoSpaceProxyModel(QSortFilterProxyModel):
    """Custom proxy model to filter items based on space-removed, lowercase matching."""
    def __init__(self, parent=None):
        super().__init__(parent)
        self._filter_text = ""

    def setFilterText(self, text: str):
        # Remove all spaces and convert to lowercase
        self._filter_text = "".join(text.split()).lower()
        self.invalidateFilter()

    def filterAcceptsRow(self, source_row, source_parent):
        if not self._filter_text:
            return True

        index = self.sourceModel().index(source_row, 0, source_parent)
        item_text = self.sourceModel().data(
            index, Qt.ItemDataRole.DisplayRole
        )
        if not item_text:
            return False

        # Remove spaces from the item and lowercase it
        clean_item = "".join(item_text.split()).lower()

        # Match using the 'in' operator
        return self._filter_text in clean_item

class SearchableComboBox(QComboBox):
    """A QComboBox that allows typing, custom filtering, and shows all options on click."""
    def __init__(self, items: list, parent=None):
        super().__init__(parent)
        self.addItems(items)
        self.setEditable(True)
        self.setInsertPolicy(QComboBox.InsertPolicy.NoInsert)

        # 1. Setup custom proxy model
        self.proxy_model = NoSpaceProxyModel(self)
        self.proxy_model.setSourceModel(self.model())

        # 2. Setup completer
        completer = QCompleter(self.proxy_model, self)
        completer.setCompletionMode(QCompleter.CompletionMode.PopupCompletion)
        completer.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        self.setCompleter(completer)

        # 3. Connect typing to update the filter
        line_edit = self.lineEdit()
        if line_edit is not None:
            line_edit.textEdited.connect(self.proxy_model.setFilterText)
            line_edit.installEventFilter(self)

        # 4. Show all options on click / focus
        line_edit = self.lineEdit()
        if line_edit is not None:
            line_edit.installEventFilter(self)

    def eventFilter(self, obj, event):
        if obj == self.lineEdit():
            if event.type() in (
                QEvent.Type.MouseButtonPress, QEvent.Type.FocusIn
            ):
                # Clear the filter so all options show when clicked/focused
                self.proxy_model.setFilterText("")
                self.showPopup()
        return super().eventFilter(obj, event)

class SelectField(QWidget):
    """Reusable custom dropdown field with a label on top."""
    def __init__(
        self, text: str, items: list, default_value: str = "",
        min_width: int = 130, parent=None
    ):
        super().__init__(parent)
        
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(4)

        self.label = QLabel(text)
        self.label.setStyleSheet("""
            font-size: 12px; font-weight: bold;
            border: none; background: transparent;
        """)
        layout.addWidget(self.label)
        
        self.combo_box = SearchableComboBox(items)
        self.combo_box.setFixedHeight(32)
        self.combo_box.setMinimumWidth(min_width)
        
        # Handle default value (shown when not focused and empty)
        line_edit = self.combo_box.lineEdit()
        if line_edit is not None:
            if default_value:
                line_edit.setPlaceholderText(default_value)
            elif items:
                line_edit.setPlaceholderText(items[0])
        
        self.combo_box.setStyleSheet(f"""
            QComboBox {{
                border: 1px solid {SECONDARY_COLOR};
                padding: 0 30px 0 8px;
                font-size: 12px;
                background-color: #ffffff;
                color: #000000;
            }}
            QComboBox::drop-down {{
                border: none;
                width: 24px;
                background: transparent;
            }}
            QComboBox::down-arrow {{
                image: url(assets/arrow.png);
                width: 12px;
                height: 12px;
            }}
        """)
        layout.addWidget(self.combo_box)

    def current_text(self) -> str:
        return self.combo_box.currentText()
