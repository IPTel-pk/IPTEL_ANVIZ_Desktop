# Technical Documentation - IPTEL ANVIZ Desktop

## 📌 Project
Attendance management software for ANVIZ biometric devices.

## WorkFlow and UI/UX
This topic includes the designing of the work flow of the application, including pages and activities in the applications

**Launcher Page:**

- This windows shows when no file is open.
- List all the recent opened files (including name with path and last open date).
- If there is no recent file show large buttons of creating a new file, Opening an existing file and settings
- Opening an existing file which is not in the recent list.
- Creating a new file `.ipatt`.
- (Note: A small helper text reminds users that backing up is as simple as copying these files to an external drive).

**Main Page:**

- This is the screen that appears immediately after a file is opened.
- Display the opened file’s full name and path prominently in the top header/status bar.
- Dashboard page with the summary of the whole file (like, total users, logs, devices, departments and recent activities).

**Device Page:**

- List all devices including Device Name, Model, IP Address (or COM Port for serial connections), and Serial Number.
- Add a new device entry (manually enter IP/COM, model, and a friendly name).
- Edit or delete an existing device entry.
- Test/Ping or connect a device.
- View the last seen.
- Download users data and attendance logs

**User Page:**

- List all enrolled users (including ID, Name, Department, Enroll Date, device where they are enroll and attendance method like fingerprint, RFID or face).
- Download all the user from device.
- Add, edit, or delete a user manually.
- Bulk-import users from a CSV/Excel or JSON file.
- Sync or upload all the users to device(s).
- Exporting all the users in CSV, Excel, JSON or PDF file.

**Report Page:**

- Initialy display all the current date logs.
- Filter logs by date range and user via simple dropdowns.
- Download attendance logs from device.
- Delete individual logs or clear logs for a specific date range.

**Attendance Page:**

- Generate reports from attendance logs.
- Choose output formats.
- Export to PDF, Excel, or CSV.
- Preview the report on-screen before exporting.
- Save custom report configurations as named templates (e.g., "Monthly HR Export").

**Department Page:**

- List all the departments (including name, start time, off time and initials of the working days)
- Assign specific shifts or timetable to departments.
- Set weekly off-days and manage a holiday calendar.
- Define salary calculation rules of each department.

**Exception Page:**

- Mark manual attendance.
- Mark Employee leave.
- Modifying the attendance log

**Settings Page:**

- Set default company details (Name, Address) to appear on report.
- Choose default date/time format (12hr / 24hr) and the start of the work week.
- Toggle between Light and Dark UI themes.

### Summary
- Launcher Page
- Main Page
- Device Page
- User Page
- Report Page
- Attendance Page
- Department Page
- Exception Page
- Settings Page

## Time Line
- 2026-08-20 - UI/UX and System Design

## 📞 Contact
moeez.raza.dev@gmail.com

**Updated:** 2026-08-20