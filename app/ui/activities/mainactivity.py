from app.ui.components.activity import Activity

class MainActivity(Activity):
    """**Main Page**"""
    def __init__(self, parent=None) -> None:
        """Initialize the Main Page Activity"""
        super().__init__(parent=parent, activity="Main")
