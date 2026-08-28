from app.ui.components.activity import Activity

class SettingsActivity(Activity):
    """**Settings Page**"""
    def __init__(self, parent=None) -> None:
        """Initialize the Settings Page Activity"""
        super().__init__(parent=parent, activity="Settings")
