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
        self._activity_widget = LauncherActivity(parent=self, navigate=self.navigate)
        self.setCentralWidget(self._activity_widget)
    
    def _swap_activity(self, widget: QWidget) -> None:
        """Used for changing the pages or activities of the app."""
        if self._activity_widget is not None:
            self._activity_widget.setParent(None)
            self._activity_widget.deleteLater()

        self._activity_widget = widget
        self.setCentralWidget(self._activity_widget)
    
    def navigate(self, target: str) -> None:
        """Navigation target requested from an activity's sidebar."""
        
        if target == "Main":
            self._swap_activity(MainActivity(parent=self, navigate=self.navigate))
        elif target == "Device":
            self._swap_activity(DeviceActivity(parent=self, navigate=self.navigate))
        elif target == "Users":
            self._swap_activity(UsersActivity(parent=self, navigate=self.navigate))
        elif target == "Department":
            self._swap_activity(DepartmentActivity(parent=self, navigate=self.navigate))
        elif target == "Report":
            self._swap_activity(ReportActivity(parent=self, navigate=self.navigate))
        elif target == "Attendance":
            self._swap_activity(AttendanceActivity(parent=self, navigate=self.navigate))
        elif target == "Exception":
            self._swap_activity(ExceptionActivity(parent=self, navigate=self.navigate))
        elif target == "Settings":
            self._swap_activity(SettingsActivity(parent=self, navigate=self.navigate))
        else:
            self._swap_activity(LauncherActivity(parent=self, navigate=self.navigate))
