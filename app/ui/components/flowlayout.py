from PySide6.QtCore import Qt, QSize, QRect, QPoint
from PySide6.QtWidgets import QLayout

class FlowLayout(QLayout):
    """
    ### FlowLayout
    This custom layout wraps widgets in rows and moves them to the next line when space is not available, similar to a responsive wrap layout.
    """

    def __init__(self, parent=None, margin=0, h_spacing=20, v_spacing=20):
        """
        Initialize the flexible flow layout.

        This method stores the spacing values and the item list needed to position widgets in flowing rows.
        """
        super().__init__(parent)
        self.item_list = []
        self.h_spacing = h_spacing
        self.v_spacing = v_spacing
        self.setContentsMargins(margin, margin, margin, margin)

    def addItem(self, item):
        """
        Add a widget item to the layout.

        This stores the item so it can be positioned and laid out during the next geometry update.
        """
        self.item_list.append(item)

    def count(self):
        """
        Return the total number of layout items.
        """
        return len(self.item_list)

    def itemAt(self, index):
        """
        Return the item at the provided index if it exists.
        """
        if 0 <= index < len(self.item_list):
            return self.item_list[index]
        return None

    def takeAt(self, index):
        """
        Remove and return the item at the given index.
        """
        if 0 <= index < len(self.item_list):
            return self.item_list.pop(index)
        return None

    def expandingDirections(self):
        """
        Indicate the layout expansion direction.
        """
        return Qt.Orientation.Vertical

    def hasHeightForWidth(self):
        """
        Indicate that this layout can adapt its height to its width.
        """
        return True

    def heightForWidth(self, width):
        """
        Calculate the height needed for the given width.
        """
        return self.doLayout(QRect(0, 0, width, 0), True)

    def setGeometry(self, rect):
        """
        Apply the computed geometry for all items in the layout.
        """
        super().setGeometry(rect)
        self.doLayout(rect, False)

    def sizeHint(self):
        """
        Return the preferred size hint for the layout.
        """
        return self.minimumSize()

    def minimumSize(self):
        """
        Calculate the minimum size required to fit all items.
        """
        size = QSize()
        for item in self.item_list:
            size = size.expandedTo(item.minimumSize())
        margins = self.contentsMargins()
        size += QSize(margins.left() + margins.right(), margins.top() + margins.bottom())
        return size

    def doLayout(self, rect, test_only):
        """
        Position each item in rows based on the available width and spacing values.
        """
        x = rect.x()
        y = rect.y()
        line_height = 0

        for item in self.item_list:
            widget = item.widget()
            space_x = self.h_spacing
            space_y = self.v_spacing

            item_size = item.sizeHint()
            next_x = x + item_size.width() + space_x
            if next_x - space_x > rect.right() and line_height > 0:
                x = rect.x()
                y = y + line_height + space_y
                next_x = x + item_size.width() + space_x
                line_height = 0

            if not test_only:
                item.setGeometry(QRect(QPoint(x, y), item_size))

            x = next_x
            line_height = max(line_height, item_size.height())

        return y + line_height - rect.y()
