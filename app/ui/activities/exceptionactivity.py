from typing import Callable
from app.ui.components.activity import Activity

class ExceptionActivity(Activity):
    """**Exception Page**"""
    def __init__(self, navigate:Callable, parent=None) -> None:
        """Initialize the Exception Page Activity"""
        super().__init__(parent=parent, activity="Exception", navigate=navigate)
