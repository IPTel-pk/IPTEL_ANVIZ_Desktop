from typing import Callable
from app.ui.components.activity import Activity

class ReportActivity(Activity):
    """**Report Page**"""
    def __init__(self, navigate:Callable, parent=None) -> None:
        """Initialize the Report Page Activity"""
        super().__init__(parent=parent, activity="Report", navigate=navigate)
