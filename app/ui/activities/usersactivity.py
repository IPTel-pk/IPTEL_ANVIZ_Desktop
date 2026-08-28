from app.ui.components.activity import Activity

class UsersActivity(Activity):
    """**Users Page**"""
    def __init__(self, parent=None) -> None:
        """Initialize the Users Page Activity"""
        super().__init__(parent=parent, activity="Users")
