# Project_Time_Login
Project_Time_Login


Time Login Application
Overview
This is a simple Python application built with Tkinter that provides a user authentication system. Users can log in with a username and password, and successful login attempts are logged to a CSV file with a timestamp.
Features

User authentication with login and password.
Logs successful login attempts to a file (Logs.csv) with the username, password, and timestamp.
Displays success or error messages using Tkinter's messagebox.
Basic GUI for entering login credentials.

Prerequisites

Python 3.x
Tkinter (usually included with Python standard library)
No additional libraries are required.

Installation

Clone or download the project files.
Ensure Python is installed on your system.
Place the main script (e.g., time_login.py) in your desired directory.

Usage

Run the main script:python time_login.py


The application window will open, prompting for a username and password.
Enter one of the predefined credentials:
Username: user1, Password: password@123
Username: user2, Password: pasd901


Click the "Login" button.
On successful login, a success message is shown, and the login details are appended to Project Time Login/Logs.csv.
On failed login, an error message is displayed.

File Structure

time_login.py: Main script containing the application logic.
Project Time Login/Logs.csv: Output file where login logs are stored (created automatically on first login).
README.md: This file.

Notes

The application stores passwords in plain text in the CSV file, which is not secure for production use. This is intended for educational purposes only.
Ensure the directory Project Time Login exists in the same location as the script, or modify the file path in the log_utilisateur method.
The application uses hardcoded users (user1 and user2). In a real-world scenario, consider using a secure database for user management.

Limitations

No user registration feature.
Passwords are displayed in plain text in the log file (not secure).
No input validation for empty fields.

Future Improvements

Add user registration functionality.
Encrypt passwords before logging or use a secure database.
Add input validation to prevent empty submissions.
Improve the GUI with better styling and responsiveness.

License
This project is for educational purposes and is not licensed for commercial use.
