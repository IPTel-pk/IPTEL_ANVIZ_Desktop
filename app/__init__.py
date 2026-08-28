from PySide6.QtWidgets import QApplication
from app.ui.windows.mainwindow import MainWindow

class App:
    """**App Class**"""
    
    def __init__(self) -> None:
        """Initialize the application, including main window"""
        self.app = QApplication([])
        self.mainwindow = MainWindow()
    
    def run(self) -> int:
        """Executes the application"""
        self.mainwindow.show()
        return self.app.exec()
