from app.ui.components.activity import Activity

class DeviceActivity(Activity):
    """**Device Page**"""
    def __init__(self, parent=None) -> None:
        """Initialize the Device Page Activity"""
        super().__init__(parent=parent, activity="Device")
