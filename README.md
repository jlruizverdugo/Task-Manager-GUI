🗂️ Task Manager GUI

A simple Python desktop application built with Tkinter and SQLite3 that allows you to register, consult, and manage pending tasks through an intuitive graphical interface.

🚀 Features

✅ Automatically creates a local database (tareas.db).
✅ Register new tasks with date, description, and responsible person.
✅ View all tasks or filter them by responsible person.
✅ Delete completed tasks.
✅ Export the database to a new .db file.
✅ User-friendly GUI with clear buttons and layout.

🧩 Technologies Used

Python 3.x

Tkinter — for the graphical interface

SQLite3 — for local database management

Shutil and OS — for file handling and system operations

🖥️ Installation & Execution
1. Clone the repository
git clone https://github.com/your-username/task-manager-gui.git
cd task-manager-gui

2. Install dependencies

No external libraries are required — just make sure you have Python 3 installed.

3. Run the application
python 26d1552f-aecd-4145-acdf-a155d412548f.py

🧠 How to Use

When you run the program, a window will appear with several action buttons:

Button	Description
Create Database	Creates the tareas.db file if it doesn’t exist.
Register Task	Prompts you to enter a new task (date, description, and responsible person).
Delete Completed Tasks	Deletes all tasks marked as completed.
View All Tasks	Displays every task currently stored in the database.
View Tasks by Responsible	Filters tasks by responsible person’s name.
Export Database	Creates a copy of the database under a new name.
📦 Project Structure
task-manager-gui/
│
├── 26d1552f-aecd-4145-acdf-a155d412548f.py   # Main program script
├── tareas.db                                  # Database file (auto-generated)
└── README.md

🛠️ Customization

You can change the database name by modifying this constant:

DB_NAME = 'tareas.db'


You can also adjust the window size, colors, and font styles by editing the Tkinter configuration section in the code.

📄 License

This project is distributed under the MIT License — feel free to use, modify, and share it.

Author

José Luis Ruiz Verdugo
