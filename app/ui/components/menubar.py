from PySide6.QtWidgets import QMainWindow, QMenu, QMenuBar
from PySide6.QtGui import QAction

class MenuBar:
    def __init__(self, menubar: QMenuBar, parent_window: QMainWindow):
        menus = [
            # FILE MENU
            {"name": "File", "status": "File Menu", "options": [
                {"name": "New File", "shortcut": "Ctrl+N", "status": "Create a new .ipatt file", "callback": lambda: print("New File")},
                {"name": "Open File", "shortcut": "Ctrl+O", "status": "Open an existing .ipatt file", "callback": lambda: print("Open File")},
                {"name": "Save", "shortcut": "Ctrl+S", "status": "Save current changes", "callback": lambda: print("Save")},
                {"name": "-"},
                {"name": "Close File", "shortcut": "Ctrl+W", "status": "Close current file", "callback": lambda: print("Close File")},
                {"name": "Exit", "shortcut": "Ctrl+Q", "status": "Exit to desktop", "callback": parent_window.close}
            ]},

            # EDIT MENU (Quick Add Actions)
            {"name": "Edit", "status": "Edit Menu", "options": [
                {"name": "Add User", "status": "Enroll a new user", "callback": lambda: print("Add User")},
                {"name": "Add Device", "status": "Register a new device", "callback": lambda: print("Add Device")},
                {"name": "Add Department", "status": "Create a new department", "callback": lambda: print("Add Department")},
                {"name": "-"},
                {"name": "Mark Exception / Leave", "status": "Open Exception page", "callback": lambda: print("Exception")},
            ]},

            # DEVICE MENU (Hardware Actions)
            {"name": "Device", "status": "Device Operations", "options": [
                {"name": "Test Connection", "status": "Ping the selected device", "callback": lambda: print("Ping")},
                {"name": "Sync Time", "status": "Sync PC time to device", "callback": lambda: print("Sync Time")},
                {"name": "-"},
                {"name": "Download Logs", "shortcut": "F5", "status": "Download attendance logs from device", "callback": lambda: print("Download Logs")},
                {"name": "Download Users", "status": "Download user list from device", "callback": lambda: print("Download Users")},
                {"name": "Upload Users", "shortcut": "F6", "status": "Upload users to device", "callback": lambda: print("Upload Users")},
            ]},

            # DATA MENU (Import / Export)
            {"name": "Data", "status": "Data Import and Export", "options": [
                {"name": "Import Users (CSV/Excel)", "status": "Bulk import users", "callback": lambda: print("Import Users")},
                {"name": "Export Users", "status": "Export user list", "callback": lambda: print("Export Users")},
                {"name": "-"},
                {"name": "Export Report as PDF", "status": "Export current report to PDF", "callback": lambda: print("Export PDF")},
                {"name": "Export Report as Excel", "status": "Export current report to Excel", "callback": lambda: print("Export Excel")},
                {"name": "Export Report as CSV", "status": "Export current report to CSV", "callback": lambda: print("Export CSV")},
            ]},

            # VIEW MENU (Navigation & Themes)
            {"name": "View", "status": "View Options", "options": [
                {"name": "Dashboard", "status": "Go to Main Dashboard", "callback": lambda: print("Navigate: Main")},
                {"name": "Attendance Reports", "status": "Go to Attendance Page", "callback": lambda: print("Navigate: Attendance")},
                {"name": "Raw Logs", "status": "Go to Report Page", "callback": lambda: print("Navigate: Report")},
                {"name": "-"},
                {"name": "Settings", "shortcut": "Ctrl+,", "status": "Open Settings Page", "callback": lambda: print("Navigate: Settings")},
                {"name": "-"},
                {"name": "Toggle Theme", "status": "Switch between Light and Dark mode", "callback": lambda: print("Toggle Theme")},
            ]},

            # HELP MENU
            {"name": "Help", "status": "Help and Info", "options": [
                {"name": "Documentation", "shortcut": "F1", "status": "Open user manual", "callback": lambda: print("Docs")},
                {"name": "Check for Updates", "status": "Check for newer versions", "callback": lambda: print("Update")},
                {"name": "License", "status": "View software license (GPL v3)", "callback": lambda: print("License")},
                {"name": "FAQs", "status": "Frequently Asked Questions", "callback": lambda: print("FAQs")},
                {"name": "-"},
                {"name": "About IPTEL ANVIZ", "status": "About this software", "callback": lambda: print("About")},
                {"name": "Contact Us", "status": "Get in touch with IP Tel Services", "callback": lambda: print("Contact")}
            ]}
        ]

        for menu in menus:
            new_menu: QMenu = menubar.addMenu('&' + menu["name"])
            if "status" in menu:
                new_menu.setStatusTip(menu["status"])
            if "options" in menu:
                for option in menu["options"]:
                    if option["name"] == '-':
                        new_menu.addSeparator()
                    else:
                        action = QAction(option["name"], parent_window)
                        if "shortcut" in option:
                            action.setShortcut(option["shortcut"])
                        if "status" in option:
                            action.setStatusTip(option["status"])
                        if "callback" in option:
                            action.triggered.connect(option["callback"])
                        new_menu.addAction(action)
