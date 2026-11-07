# Technical Documentation - IPTEL ANVIZ Desktop

## 📌 Project Overview
**IPTEL ANVIZ Desktop** is a cross-platform attendance management application designed for ANVIZ biometric devices. It serves as a modern, open-source replacement for the outdated ANVIZ CrossChex software, providing a cleaner UI, better performance, and cross-platform support (Windows, Linux, macOS).

The application is built using **Python 3.9+** and **PyQt6**, utilizing a local JSON-based file system to store organizational data.

---

## 📖 Table of Contents
1. [Project Architecture](#project-architecture)
2. [File Structure](#file-structure)
3. [Core Directories & Files](#core-directories--files)
4. [Data Model (`.ipatt` Files)](#data-model-ipatt-files)
5. [UI Architecture](#ui-architecture)
6. [Reusable Components](#reusable-components)
7. [Contact](#contact)

---

## 🏗️ Project Architecture

The application follows a modular architecture:
- **UI Layer:** Built with PyQt6, divided into Windows and Activities.
- **State Management:** Handled by the Main Window, which swaps Activities (pages) dynamically without reloading the whole application.
- **Data Layer:** Uses local `.ipatt` files (JSON format) to store organization data, ensuring portability and easy backups.
- **Hardware Layer:** Communicates with ANVIZ devices via network (IP) or serial (COM) connections.

---

## 📁 File Structure

```text
IPTEL_ANVIZ_Desktop/
│
├── main.py                 # Application entry point
├── run.bat / run.sh        # Environment setup and launch scripts
├── README.md               # Project overview and setup guide
├── LICENSE.md              # GPL v3 License
├── requirements.txt        # Production dependencies
├── requirements-dev.txt    # Development dependencies
│
├── app/                    # Main application package
│   ├── __init__.py         # App initialization and QApplication setup
│   ├── settings.py         # Global constants (Colors, App Version, etc.)
│   │
│   ├── ui/                 # All UI-related code
│   │   ├── activities/     # Individual pages (Launcher, Dashboard, etc.)
│   │   ├── components/     # Reusable custom widgets
│   │   └── windows/        # Main window shell
│   │
├── assets/                 # Static files (Images, Icons, Logos)
├── data/                   # Mock/Testing data for development
└── docs/                   # Documentation
    ├── CONTRIBUTING.md     # Guidelines for contributors
    └── TECHNICAL.md        # This file
```

---

## 📂 Core Directories & Files

### Root Directory
- **`main.py`**: The entry point of the application. It initializes the `QApplication`, loads the main window, and starts the event loop.
- **`run.bat` / `run.sh`**: Scripts to activate the virtual environment and launch the app in development mode (`.bat` for Windows, `.sh` for UNIX/Linux).
- **`requirements.txt`**: Lists the required Python packages (e.g., `PySide6`).

### `app/`
The core application package.
- **`__init__.py`**: Handles the initialization of the main application class.
- **`settings.py`**: Centralized configuration. Contains constant strings for colors (e.g., `ACCENT_COLOR`), version numbers, and default settings used across the app.

### `app/ui/`
Contains all User Interface code.
- **`windows/`**: Contains the application shell. 
  - `mainwindow.py`: The main box that holds the sidebar, header, and the dynamic content area where activities are loaded.
- **`activities/`**: Contains the 9 separate pages of the application (Launcher, Main, Device, User, Report, Attendance, Department, Exception, Settings). Each activity is a standalone `QWidget` that is swapped into the main window.
- **`components/`**: Contains custom, reusable UI widgets (explained in the Reusable Components section below).

### `assets/`
Contains all static resources, including application icons, logos, and placeholder images used in the UI.

### `data/`
Contains mock/temporary data (e.g., dictionaries mimicking database responses) used for testing the UI during development before the database is fully connected.

---

## 🖥️ UI Architecture

The UI is built using PyQt6 and follows a dynamic swapping model:
1. **MainWindow** acts as the container.
2. **Sidebar** (Aside) and **Header** remain static.
3. When a user clicks a sidebar button, the `MainWindow` clears the current content area and injects a new **Activity** (page).

### The 9 Activities:
1. **Launcher:** File creation, opening, and recent files list.
2. **Main (Dashboard):** Summary stats and recent activity feed.
3. **Device:** Device IP/COM configuration and hardware actions.
4. **User:** Employee/Student enrollment and management.
5. **Report:** Raw attendance logs and filtering.
6. **Attendance:** Formatted report generation and export (PDF/CSV).
7. **Department:** Shift timings, working days, and holiday calendars.
8. **Exception:** Manual attendance overrides and leave management.
9. **Settings:** Company details, themes, and time formats.

---

Here is the improved **Reusable Components** section. Instead of a flat list, I have grouped the files logically by their function. This makes it much easier for a new developer to find what they need without getting overwhelmed by 23 separate bullet points.

---

## 🧩 Reusable Components

To ensure a consistent look and feel, the `app/ui/components/` folder contains all the custom, reusable widgets used throughout the application. They are grouped below by their primary function:

### 1. Layouts & Base Classes
- **`flowlayout.py`**: A custom layout that mimics CSS `flex-wrap`. It automatically wraps child widgets (like cards) to the next line when the window is resized, making the UI fully responsive.
- **`activity.py`**: The base class for all 9 pages (Activities). It handles the standard page structure, header setup, and navigation logic.
- **`header.py`**: The top header bar used across all pages. It includes the page title and a search bar with a cancel button.

### 2. Navigation & Menus
- **`aside.py`**: The main sidebar container that holds the navigation buttons.
- **`asidebutton.py`**: The custom buttons used inside the sidebar. It includes logic for active states (left border highlight) and icon spacing.
- **`menubar.py`**: The top application menu (File, Edit, Device, Data, View, Help) containing all the window-level shortcuts and actions.

### 3. Form Fields & Inputs
- **`inputfield.py`**: A standardized text input with a label on top. It supports password mode (`hidden`) and disabled states.
- **`selectfield.py`**: A customized, searchable dropdown (`QComboBox`). It allows users to filter options by typing while ignoring spaces and case sensitivity.
- **`workingdayswidget.py`**: A custom widget containing circular toggle buttons (M, T, W, T, F, S, S) used in the Department form to select working days.

### 4. Buttons
- **`primarybutton.py`**: The standard submit/save button (e.g., "Save User", "Save Device") with an accent color and hover state.
- **`toolbarbutton.py`**: Standardized buttons used in the top toolbars (e.g., "Add", "Edit", "Delete", "Download") with icons and a white background.
- **`largebutton.py`**: Large action cards used specifically on the Launcher page for "Create New File" and "Open Existing File".
- **`fileitemaction.py`**: A tiny widget containing the folder and trash icons used in the Recent Files table rows.

### 5. Data Display (Cards & Tables)
- **`standardtable.py`**: A pre-styled `QTableWidget` with alternating row colors, no grid lines, custom headers, and disabled row selection. It automatically handles horizontal scrolling and stretches to fill available space.
- **`statbox.py`**: The small summary boxes used on the Dashboard (e.g., "156 Users", "3 Devices").
- **`devicecard.py`**: The card used on the Device page to display device stats (IP, Port, Status). It is clickable, toggles a checkbox, and highlights with `ACCENT_COLOR` when selected.
- **`usercard.py`**: The card used on the User page to display a user's name, department, and avatar.
- **`departmentcard.py`**: The card used on the Department page to display start/end times and working days.
- **`activityitem.py`**: A single row in the Dashboard's "Recent Activities" list. It dynamically loads different icons and colors based on the status code (Ok, Add, Edit, Delete, Info).

### 6. Sidebars & Footers
- **`deviceformsidebar.py`**: The right-side panel for adding/editing devices. Contains inputs for IP, Port, Model, etc.
- **`userformsidebar.py`**: The right-side panel for adding/editing users. Contains inputs for ID, Name, Department, Password, etc.
- **`departmentformsidebar.py`**: The right-side panel for adding/editing departments. Contains the time inputs and the `WorkingDaysWidget`.
- **`paginationfooter.py`**: A reusable footer for tables containing the "Showing X-Y of Z" label and the left/right navigation arrows.

---
## 📞 Contact
For technical inquiries, please contact:

- 🌐 Website: [moeezraza.netlify.app](https://moeezraza.netlify.app)
- 📧 Email: [moeez.raza.dev@gmail.com](mailto:moeez.raza.dev@gmail.com)
- 📞 Phone: [+92 310 3439448](https://wa.me/923103439448)
