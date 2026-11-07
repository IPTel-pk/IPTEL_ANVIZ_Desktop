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
    """
    ### NoSpaceProxyModel
    This custom model filters dropdown entries while ignoring spaces and comparing them in lowercase.
    """

    def __init__(self, parent=None):
        """
        Initialize the filter proxy model.

        This method stores the normalized text used during item matching for searchable dropdowns.
        """
        super().__init__(parent)
        self._filter_text = ""

        # 1. Store the normalized search text for filtering

    def setFilterText(self, text: str):
        """
        Store the normalized filter text used for searching.
        """
        # 1. Remove spaces and lowercase the typed query
        self._filter_text = "".join(text.split()).lower()
        self.invalidateFilter()

    def filterAcceptsRow(self, source_row, source_parent):
        """
        Accept rows whose text matches the normalized search query.
        """
        # 1. Skip filtering when the query is empty
        if not self._filter_text:
            return True

        index = self.sourceModel().index(source_row, 0, source_parent)
        item_text = self.sourceModel().data(
            index, Qt.ItemDataRole.DisplayRole
        )
        if not item_text:
            return False

        # 2. Normalize the option text before comparing it
        clean_item = "".join(item_text.split()).lower()
        return self._filter_text in clean_item

class SearchableComboBox(QComboBox):
    """
    ### SearchableComboBox
    This widget allows typing into a dropdown and filters the options as the user searches.
    """

    def __init__(self, items: list, parent=None):
        """
        Initialize the searchable dropdown.

        This method sets up the editable combobox, proxy model, and focus behavior used for type-to-filter selection.
        """
        super().__init__(parent)
        self.addItems(items)
        self.setEditable(True)
        self.setInsertPolicy(QComboBox.InsertPolicy.NoInsert)

        # 1. Set up the custom proxy model to filter items without spaces
        self.proxy_model = NoSpaceProxyModel(self)
        self.proxy_model.setSourceModel(self.model())

        # 2. Set up the completer used for popup suggestions
        completer = QCompleter(self.proxy_model, self)
        completer.setCompletionMode(QCompleter.CompletionMode.PopupCompletion)
        completer.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        self.setCompleter(completer)

        # 3. Connect typing in the line edit to the filter logic
        line_edit = self.lineEdit()
        if line_edit is not None:
            line_edit.textEdited.connect(self.proxy_model.setFilterText)
            line_edit.installEventFilter(self)

        # 4. Show all options when the user clicks or focuses the field
        line_edit = self.lineEdit()
        if line_edit is not None:
            line_edit.installEventFilter(self)

    def eventFilter(self, obj, event):
        """
        Reset the filter and show the full list when the field receives focus or a click.
        """
        if obj == self.lineEdit():
            if event.type() in (
                QEvent.Type.MouseButtonPress, QEvent.Type.FocusIn
            ):
                # 1. Clear the filter so all options appear again
                self.proxy_model.setFilterText("")
                self.showPopup()
        return super().eventFilter(obj, event)

class SelectField(QWidget):
    """
    ### SelectField
    This widget creates a labeled dropdown field used throughout the app for selecting values from a list.
    """

    def __init__(
        self, text: str, items: list, default_value: str = "",
        min_width: int = 130, parent=None
    ):
        """
        Initialize the select field widget.

        This method creates the label and searchable combobox used for list-based selections in forms.
        """
        super().__init__(parent)

        # 1. Create the vertical layout for the label and dropdown
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(4)

        # 2. Add the field label on top of the control
        self.label = QLabel(text)
        self.label.setStyleSheet("""
            font-size: 12px; font-weight: bold;
            border: none; background: transparent;
        """)
        layout.addWidget(self.label)

        # 3. Create the searchable combo box for the list of choices
        self.combo_box = SearchableComboBox(items)
        self.combo_box.setFixedHeight(32)
        self.combo_box.setMinimumWidth(min_width)

        # 4. Apply a default placeholder text if provided
        line_edit = self.combo_box.lineEdit()
        if line_edit is not None:
            if default_value:
                line_edit.setPlaceholderText(default_value)
            elif items:
                line_edit.setPlaceholderText(items[0])

        # 5. Style the combo box to match the app theme
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
        """
        Return the currently selected dropdown value.
        """
        return self.combo_box.currentText()
