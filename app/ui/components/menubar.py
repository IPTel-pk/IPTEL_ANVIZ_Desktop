from PySide6.QtWidgets import QMainWindow, QMenu, QMenuBar
from PySide6.QtGui import QAction

class MenuBar:
  def __init__(self, menubar:QMenuBar, parent_window:QMainWindow):
    menus = [
      {"name": "File", "status": "File Menu", "options": [
        {"name": "New File", "shortcut": "Ctrl+N", "status": "Create new file", "callback": lambda: print("")},
        {"name": "Open File", "shortcut": "Ctrl+O", "status": "Open existing file", "callback": lambda: print("")},
        {"name": "-"},
        {"name": "Close File", "status": "Close current file", "callback": lambda: print("")},
        {"name": "Exit", "shortcut": "Ctrl+Q", "status": "Exit to desktop", "callback": lambda: print("")}
      ]},
      {"name": "Edit", "status": "Edit Menu", "options": [
        {"name": "New Device", "status": "Create new device", "callback": lambda: print("")},
        {"name": "Edit Device", "status": "Modify device", "callback": lambda: print("")},
        {"name": "-"},
        {"name": "New User", "status": "Create new user", "callback": lambda: print("")},
        {"name": "Edit User", "status": "Modify user", "callback": lambda: print("")},
      ]},
      {"name": "Help", "status": "Help and Info", "options": [
        {"name": "Documentation", "callback": lambda: print("")},
        {"name": "License", "callback": lambda: print("")},
        {"name": "FAQs", "callback": lambda: print("")},
        {"name": "Contact us", "callback": lambda: print("")}
      ]}
    ]
    for menu in menus:
      new_menu:QMenu = menubar.addMenu('&' + menu["name"])
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
