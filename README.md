# 📝 Advanced CLI To-Do List Manager

A feature-rich **Command-Line To-Do List Application** built in Python using object-oriented principles, persistent file storage, colored terminal UI, task priorities, due dates, backups, and more.

---

## 🚀 Features

- ✅ Add, view, and delete tasks with descriptions
- ⭐ Assign **priorities**: Low, Medium, High
- 📅 Add **due dates** to tasks
- 🎯 Mark tasks as complete
- 💾 **Persistent storage** using JSON
- 🕒 **Auto-backups** created with timestamps
- 📈 Progress indicator: *X of Y tasks completed*
- 🎨 **Colored terminal output** using `colorama`
- 📤 Export tasks to `.csv` for external use
- 🧼 Clear and simple user interface
- 🧪 Input validation and error handling

---

## 📂 Folder Structure

📁 your-repo/
├── todo_list_ultimate.py # Main Python script
├── todo_tasks.json # Auto-generated task data file
├── backups/ # Contains timestamped JSON backups
└── README.md # Project description

yaml
Copy
Edit

---

## 🛠️ Requirements

- Python 3.7+
- [`colorama`](https://pypi.org/project/colorama/)

### Install dependencies:
```bash
pip install colorama
💡 How to Use
▶️ Run the Program
bash
Copy
Edit
python todo_list_ultimate.py
📋 Menu Options
Add a new task
Enter description, priority, and due date.

Mark task as complete
Enter the task number to mark as done.

Delete a task
Permanently deletes a task (with confirmation).

Export tasks to CSV
Saves your task list in todo_export.csv.

Exit
Safely exits the app.

🧠 Example Output
bash
Copy
Edit
--- Your To-Do List ---
1. [✓] Buy groceries | Priority: High | Due: 2025-08-01
2. [ ] Finish project report | Priority: Medium | Due: 2025-08-02
-----------------------

✔ 1 of 2 tasks completed
💾 Backups
Every time you update your list, a JSON backup is automatically created in the backups/ folder with the filename format:

pgsql
Copy
Edit
todo_backup_YYYYMMDD_HHMMSS.json
📤 Export to CSV
Use the menu to export all tasks to todo_export.csv, which includes:

Description

Completion status

Created timestamp

Priority

Due date

🔧 Future Improvements (Optional)
GUI version (Tkinter or PyQt)

Web version (Flask + SQLite)

Notifications or reminders

Task tags and search functionality

Undo/redo functionality

📄 License
This project is licensed under the MIT License.

👨‍💻 Author
Sai Deepak Kolusu
📍 Hyderabad, India
📧 saideepakkolusu39@gmail.com
🔗 LinkedIn

yaml
Copy
Edit
