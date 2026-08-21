import sys
from app import App

def main() -> int:
    """**Entry Point**"""
    app = App()
    return app.run()

if __name__ == "__main__":
    sys.exit(main())
