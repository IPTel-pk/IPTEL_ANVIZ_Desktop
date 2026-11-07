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
    """
    ### MainWindow
    This is the root desktop window for the application and it manages the visible activity screen and app menu.
    """

    def __init__(self) -> None:
        """
        Initialize the application window.

        This method configures the window title, size, icon, menu bar, and the initial launcher screen.
        """
        super().__init__()

        # 1. Set the base window properties such as title, size, and icon
        self.setWindowTitle("IPTEL ANVIZ")
        self.setGeometry(0, 0, 800, 600)
        self.setWindowIcon(QIcon("assets/icon.png"))
        self.setContentsMargins(0, 0, 0, 0)

        # 2. Create or attach the menu bar for the application
        menubar = self.menuBar()
        if menubar is None:
            menubar = QMenuBar(self)
            self.setMenuBar(menubar)
        MenuBar(menubar, self)

        # 3. Set the first screen that opens when the app starts
        self._activity_widget = LauncherActivity(
            parent=self, navigate=self.navigate
        )
        self.setCentralWidget(self._activity_widget)

    def _swap_activity(self, widget: QWidget) -> None:
        """
        Replace the current screen with a new activity widget.

        This method cleans up the old activity and sets the requested widget as the new central content.
        """
        # 1. Remove the previous central widget before replacing it
        if self._activity_widget is not None:
            self._activity_widget.setParent(None)
            self._activity_widget.deleteLater()

        # 2. Store and display the new activity widget
        self._activity_widget = widget
        self.setCentralWidget(self._activity_widget)

    def navigate(self, target: str) -> None:
        """
        Navigate between the application's activity screens.

        This method receives the target page name and swaps in the matching widget for that screen.
        """
        # 1. Route to the main dashboard screen
        if target == "Main":
            self._swap_activity(MainActivity(
                parent=self, navigate=self.navigate
            ))

        # 2. Route to the device management screen
        elif target == "Device":
            self._swap_activity(DeviceActivity(
                parent=self, navigate=self.navigate
            ))

        # 3. Route to the users management screen
        elif target == "Users":
            self._swap_activity(UsersActivity(
                parent=self, navigate=self.navigate
            ))

        # 4. Route to the department screen
        elif target == "Department":
            self._swap_activity(DepartmentActivity(
                parent=self, navigate=self.navigate
            ))

        # 5. Route to the report screen
        elif target == "Report":
            self._swap_activity(ReportActivity(
                parent=self, navigate=self.navigate
            ))

        # 6. Route to the attendance screen
        elif target == "Attendance":
            self._swap_activity(AttendanceActivity(
                parent=self, navigate=self.navigate
            ))

        # 7. Route to the exception screen
        elif target == "Exception":
            self._swap_activity(ExceptionActivity(
                parent=self, navigate=self.navigate
            ))

        # 8. Route to the settings screen
        elif target == "Settings":
            self._swap_activity(SettingsActivity(
                parent=self, navigate=self.navigate
            ))

        # 9. Fall back to the launcher when no known page matches
        else:
            self._swap_activity(LauncherActivity(
                parent=self, navigate=self.navigate
            ))
