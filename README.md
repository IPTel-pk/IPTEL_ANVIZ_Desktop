# IPTEL ANVIZ Desktop

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey)](https://github.com/IPTel-pk/IPTEL_ANVIZ_Desktop)
[![Version](https://img.shields.io/badge/version-0.0.1--alpha-orange)](https://github.com/IPTel-pk/IPTEL_ANVIZ_Desktop)
[![Python](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/)
[![PyQt6](https://img.shields.io/badge/PyQt6-6.0%2B-brightgreen)](https://www.riverbankcomputing.com/software/pyqt/)

**A modern, cross-platform attendance management solution designed for ANVIZ biometric devices.**

---

## 📖 Table of Contents

- [About the Project](#-about-the-project)
- [The Problem We Solve](#-the-problem-we-solve)
- [Features](#-features)
- [Technology Stack](#-technology-stack)
- [Timeline](#-timeline)
- [Getting Started](#-getting-started)
- [Installation](#-installation)
- [Usage](#-usage)
- [Contributing](#-contributing)
- [License](#-license)
- [Contact](#-contact)
- [Acknowledgments](#-acknowledgments)

---

## 📌 About the Project

**IPTEL ANVIZ Desktop** is a user-friendly attendance management desktop application developed by **IP Tel Services**—a Pakistani company specializing in biometric attendance solutions, primarily dealing with **ANVIZ** and **ZKTeco** machines.

This application is specifically designed for **ANVIZ biometric attendance machines**, offering a modern, intuitive interface that replaces the outdated, unmaintained software traditionally bundled with these devices.

### Why We Built This

ANVIZ machines are affordable, reliable, and widely used in schools, offices, and factories across Pakistan. However, the factory-provided software suffers from several critical issues:

- 🐌 **Outdated UI/UX** – Clunky, difficult to navigate interfaces
- 🖥️ **Windows-Only** – No support for Linux or macOS users
- 🚫 **No Active Development** – Software is no longer maintained or updated
- 🔒 **Closed Source** – No community contributions or improvements

We built this open-source solution to address these pain points and bring a better experience to ANVIZ users worldwide.

---

## 🎯 The Problem We Solve

| Problem | Our Solution |
| :--- | :--- |
| Proprietary, outdated software | Open-source, actively maintained |
| Windows-only compatibility | Cross-platform (Windows, Linux, macOS) |
| Complex, cluttered UI | Clean, minimal, user-friendly interface |
| No flexibility for customization | Open-source allows modifications |
| No community support | Active community and developer support |
| Manual data handling | Automated synchronization and reporting |
| No multi-organization support | Separate database files for each organization |

---

## ✨ Features

### Core Functionalities

- 📁 **Organization File Management** – Create and manage separate `.ipatt` database files for different organizations
- 📊 **Dashboard Overview** – Quick summary of users, logs, devices, and recent activities
- 🖥️ **Device Management** – Add, edit, and manage ANVIZ devices with IP/COM configuration
- 👤 **User Management** – Enroll, edit, delete, and bulk-import users from CSV/Excel/JSON
- 📝 **Report Page** – View and manage raw attendance logs with filtering
- 📄 **Attendance Page** – Generate and export formatted reports in PDF, Excel, and CSV
- 🏢 **Department Management** – Manage departments, shifts, weekly offs, and holiday calendars
- ⚠️ **Exception Handling** – Mark manual attendance, leaves, and modify logs
- ⚙️ **Customizable Settings** – Company details, date/time formats, and theme preferences

---

## 🛠️ Technology Stack

| Component | Technology |
| :--- | :--- |
| **Frontend Framework** | PyQt6 (Qt 6.x) |
| **Backend Language** | Python 3.9+ |
| **Database** | JSON-based `.ipatt` files |
| **Build Tools** | PyInstaller |
| **UI Designer** | Qt Designer |
| **Version Control** | Git / GitHub |
| **Documentation** | Markdown |

---

## 🗓️ Timeline

### Phase 1: Foundation (Completed)
- ✅ Project initialization and repository setup
- ✅ Core architecture design
- ✅ License selection (GPL v3)
- ✅ README and documentation setup

### Phase 2: MVP Development (In Progress)
- 🚧 Launcher Page – File management
- 🚧 Main Dashboard – Summary and overview
- 🚧 Device Management – IP/COM configuration
- 🚧 User Management – CRUD operations and import/export
- 🚧 Report Page – Log viewing and filtering
- 🚧 Attendance Page – Report generation and export

### Phase 3: Advanced Features
- ⏳ Department Management – Shifts, schedules, and calendars
- ⏳ Exception Management – Manual attendance and leave marking
- ⏳ Settings Page – Themes, formats, and company details
- ⏳ Device Synchronization – Download users and logs from ANVIZ devices

### Phase 4: Testing & Refinement (Q3 2026)
- ⏳ Cross-platform testing (Windows, Linux, macOS)
- ⏳ Performance optimization
- ⏳ Bug fixes and stability improvements
- ⏳ User acceptance testing (UAT)

### Phase 5: Beta Release (Q4 2026)
- ⏳ Public beta release
- ⏳ Community feedback collection
- ⏳ Documentation and user guides
- ⏳ Contribution guidelines refinement

### Phase 6: Future Roadmap (2027+)
- ⏳ Payroll integration
- ⏳ Cloud synchronization
- ⏳ Mobile companion app
- ⏳ Multi-language support
- ⏳ Advanced analytics and insights
- ⏳ Commercial paid version with additional features

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.9 or higher** – [Download Python](https://www.python.org/downloads/)
- **pip** – Python package manager (comes with Python)
- **Git** – For cloning the repository
- **Operating System** – Windows 10+, Linux (Ubuntu 20.04+), or macOS 11+

### Installation

```bash
# Clone the repository
git clone https://github.com/IPTel-pk/IPTEL_ANVIZ_Desktop.git

# Navigate to project directory
cd IPTEL_ANVIZ_Desktop

# Create a virtual environment (recommended)
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate

# Install required dependencies
pip install -r requirements.txt

# Run the application
python main.py
```

### Build from Source

```bash
pyinstaller --onedir --windowed --name "IPTEL_ANVIZ_Desktop" main.py
```

> **Note:** The built executable will be available in the `dist/` folder.

---

## 📖 Usage

### Creating a New Organization
1. Launch the application
2. Click **"Create New File"**
3. Name your organization file (e.g., `CompanyName.ipatt`)
4. Select a save location

### Adding a Device
1. Open your organization file
2. Go to **Device Page**
3. Click **"Add Device"**
4. Enter device details (Name, Model, IP)

### Managing Users
1. Go to **User Page**
2. Click **"Add User"** to enroll a new user
3. Use **"Import"** to bulk-add users from CSV/Excel/JSON
4. Use **"Upload to Device"** to sync users to ANVIZ machines

### Generating Reports
1. Go to **Attendance Page**
2. Select date range and filters
3. Click **"Generate Report"**
4. Preview or export to PDF/Excel/CSV

### Marking Exceptions
1. Go to **Exception Page**
2. Select a date
3. Use radio buttons to mark Present/Absent/Leave
4. Enter Time In/Time Out as needed
5. Save changes

---

## 🤝 Contributing

We welcome contributions from the community! Please read our [Contributing Guidelines](docs/CONTRIBUTING.md) before submitting any changes.

### Quick Contribution Steps

1. **Fork the repository** – Create your own copy
2. **Create a branch** – `git checkout -b feature/your-feature-name`
3. **Make your changes** – Write clean, well-documented code
4. **Test thoroughly** – Ensure your changes work on all platforms
5. **Commit your changes** – Write clear commit messages
6. **Push to your branch** – `git push origin feature/your-feature-name`
7. **Open a Pull Request** – Describe your changes and link any related issues

### Contribution Rules

- 📝 **All contributions must be well-documented** – Include comments and documentation
- 🧪 **Test your code** – Ensure it doesn't break existing functionality
- 🚫 **No unsolicited major changes** – Discuss large features via issues first
- 📄 **Sign the CLA** – Contributors agree to the Contributor License Agreement
- 🔍 **Code review required** – All PRs will be reviewed before merging

### Reporting Issues

If you find a bug or have a feature request, please:
1. Check if the issue already exists
2. Create a new issue with a clear title and description
3. Include steps to reproduce the bug
4. Attach screenshots or logs if applicable

---

## 📄 License

This project is licensed under the **GNU General Public License v3.0** – see the [LICENSE](LICENSE) file for details.

### Commercial Licensing

For commercial use or if you require a proprietary license, please contact us at:
📧 **moeez.raza.dev@gmail.com**

---

## 📞 Contact

**IP Tel Services**

- 🌐 Website: [moeezraza.netlify.app](https://moeezraza.netlify.app)
- 📧 Email: [moeez.raza.dev@gmail.com](mailto:moeez.raza.dev@gmail.com)
- 📞 Phone: +92 344 5880880

---

## 🙏 Acknowledgments

- **ANVIZ** – For manufacturing reliable and affordable biometric attendance machines
- **ZKTeco** – For their contribution to the biometric industry
- **Open Source Community** – For inspiration and support
- **IP Tel Services Team** – For their dedication to this project

---

## ⭐ Star Us!

If you find this project useful, please give us a ⭐ on GitHub! It helps us grow and improve the software.

---

## 🔗 Links

- [GitHub Repository](https://github.com/IPTel-pk/IPTEL_ANVIZ_Desktop)
- [Issue Tracker](https://github.com/IPTel-pk/IPTEL_ANVIZ_Desktop/issues)
- [Project Roadmap](docs/ROADMAP.md)
- [Contributing Guidelines](docs/CONTRIBUTING.md)
- [Technical Documentation](docs/TECHNICAL.md)

---

**Made with ❤️ by IP Tel Services Team – Pakistan**
