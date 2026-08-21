from PyQt6.QtWidgets import QMainWindow, QWidget
from PyQt6.QtGui import QIcon

class MainWindow(QMainWindow):
    """**App Main Window**"""
    def __init__(self) -> None:
        """Initialize the main window of the appliation"""
        super().__init__()
        self.setWindowTitle("IPTEL ANVIZ")
        self.setGeometry(0, 0, 1440, 1024)
        self.setWindowIcon(QIcon("assets/icon.png"))
        self.setContentsMargins(0,0,0,0)
    
    def _swap_activity(self, widget: QWidget) -> None:
        """Used for changing the pages or activities of the app."""
        if self._activity_widget is not None:
            self._activity_widget.setParent(None)
            self._activity_widget.deleteLater()

        self._activity_widget = widget
        self.setCentralWidget(self._activity_widget)
    
    # def _on_navigate(self, target: str) -> None:
    #     """Navigation target requested from an activity's sidebar."""
        
    #     if target == "device":
    #         self._swap_activity(DeviceActivity(on_navigate=self._on_navigate))
    #     elif target == "users":
    #         self._swap_activity(UsersActivity(on_navigate=self._on_navigate))
    #     elif target == "report":
    #         self._swap_activity(ReportActivity(on_navigate=self._on_navigate))
    #     else:
    #         # Unknown target; fail safe to DeviceActivity while file is open.
    #         self._swap_activity(DeviceActivity(on_navigate=self._on_navigate))
