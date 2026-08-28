from app.ui.components.activity import Activity

class DepartmentActivity(Activity):
    """**Department Page**"""
    def __init__(self, parent=None) -> None:
        """Initialize the Department Page Activity"""
        super().__init__(parent=parent, activity="Department")