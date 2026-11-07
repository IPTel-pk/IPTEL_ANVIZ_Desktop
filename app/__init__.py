from PySide6.QtWidgets import QApplication
from app.ui.windows.mainwindow import MainWindow

class App:
    """
    ### App
    This class starts the Qt application and creates the main desktop window used by the entire project.
    """

    def __init__(self) -> None:
        """
        Initialize the application shell.

        This method creates the QApplication instance and the primary window that hosts the UI.
        """
        # 1. Create the Qt application instance
        self.app = QApplication([])

        # 2. Initialize the main application window
        self.mainwindow = MainWindow()

    def run(self) -> int:
        """
        Launch the application and start the event loop.

        This method displays the main window and returns the Qt exit code when the app closes.
        """
        # 3. Show the main window and begin the GUI event loop
        self.mainwindow.show()
        return self.app.exec()
