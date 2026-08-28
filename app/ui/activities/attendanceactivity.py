from app.ui.components.activity import Activity

class AttendanceActivity(Activity):
    """**Attendance Page**"""
    def __init__(self, parent=None) -> None:
        """Initialize the Attendance Page Activity"""
        super().__init__(parent=parent, activity="Attendance")
