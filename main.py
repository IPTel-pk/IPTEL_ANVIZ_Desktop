import sys
from app import App

# 1. Application entry point
# This function creates the application instance and starts the event loop.
def main() -> int:
    """
    ### Main Entry Point
    This function initializes the app object and launches the desktop window.
    """
    # 2. Create the top-level app wrapper and run the GUI
    app = App()
    return app.run()

# 3. Run the application when the script is executed directly
if __name__ == "__main__":
    sys.exit(main())
