from PySide6.QtWidgets import QMainWindow, QWidget, QMenuBar
from PySide6.QtGui import QIcon
from app.ui.components.menubar import MenuBar
from app.ui.activities.launcheractivity import LauncherActivity
from app.ui.activities.mainactivity import MainActivity
from app.ui.activities.deviceactivity import DeviceActivity
from app.ui.activities.usersactivity import UsersActivity
from app.ui.activities.departmentactivity import DepartmentActivity
from app.ui.activities.reportactivity import ReportActivity
from app.ui.activities.attendanceactivity import AttendanceActivity
from app.ui.activities.exceptionactivity import ExceptionActivity
from app.ui.activities.settingsactivity import SettingsActivity

class MainWindow(QMainWindow):
    """**App Main Window**"""
    def __init__(self) -> None:
        """Initialize the main window of the appliation"""
        super().__init__()
        self.setWindowTitle("IPTEL ANVIZ")
        self.setGeometry(0, 0, 800, 600)
        self.setWindowIcon(QIcon("assets/icon.png"))
        self.setContentsMargins(0,0,0,0)
        menubar = self.menuBar()
        if menubar is None:
            menubar = QMenuBar(self)
            self.setMenuBar(menubar)
        MenuBar(menubar, self)
        self._activity_widget = LauncherActivity(self)
        self.setCentralWidget(self._activity_widget)
    
    def _swap_activity(self, widget: QWidget) -> None:
        """Used for changing the pages or activities of the app."""
        if self._activity_widget is not None:
            self._activity_widget.setParent(None)
            self._activity_widget.deleteLater()

        self._activity_widget = widget
    
    def navigate(self, target: str) -> None:
        """Navigation target requested from an activity's sidebar."""
        
        if target == "main":
            self._swap_activity(MainActivity(self, ))
        elif target == "device":
            self._swap_activity(DeviceActivity())
        elif target == "users":
            self._swap_activity(UsersActivity())
        elif target == "department":
            self._swap_activity(DepartmentActivity())
        elif target == "report":
            self._swap_activity(ReportActivity())
        elif target == "attendance":
            self._swap_activity(AttendanceActivity())
        elif target == "exception":
            self._swap_activity(ExceptionActivity())
        elif target == "settings":
            self._swap_activity(SettingsActivity())
        else:
            self._swap_activity(LauncherActivity())
