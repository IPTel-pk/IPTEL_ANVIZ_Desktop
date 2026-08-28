from typing import Callable
from app.ui.components.activity import Activity

class LauncherActivity(Activity):
    """**Launcher Page**"""
    def __init__(self, navigate:Callable, parent=None) -> None:
        """Initialize the Launcher Page Activity"""
        super().__init__(parent=parent, activity="Launcher", navigate=navigate)
