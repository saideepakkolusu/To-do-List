import os
import json
from datetime import datetime
from typing import List, Dict
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# --- Constants ---
TASKS_FILE = "todo_tasks.json"
BACKUP_DIR = "backups"

# Ensure backup directory exists
os.makedirs(BACKUP_DIR, exist_ok=True)


class Task:
    def __init__(self, description: str, priority: str = "Medium", due_date: str = ""):
        self.description = description
        self.completed = False
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.priority = priority.capitalize()
        self.due_date = due_date

    def to_dict(self) -> Dict:
        return {
            "description": self.description,
            "completed": self.completed,
            "created_at": self.created_at,
            "priority": self.priority,
            "due_date": self.due_date,
        }

    @staticmethod
    def from_dict(data: Dict):
        task = Task(data["description"], data.get("priority", "Medium"), data.get("due_date", ""))
        task.completed = data.get("completed", False)
        task.created_at = data.get("created_at", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        return task


class ToDoList:
    def __init__(self):
        self.tasks: List[Task] = self.load_tasks()

    def load_tasks(self) -> List[Task]:
        if os.path.exists(TASKS_FILE):
            with open(TASKS_FILE, "r") as f:
                try:
                    data = json.load(f)
                    return [Task.from_dict(task) for task in data]
                except json.JSONDecodeError:
                    print(Fore.RED + "Failed to load tasks. Starting fresh.")
        return []

    def save_tasks(self):
        # Backup before saving
        backup_path = os.path.join(BACKUP_DIR, f"todo_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json")
        with open(backup_path, "w") as backup_file:
            json.dump([task.to_dict() for task in self.tasks], backup_file, indent=4)

        with open(TASKS_FILE, "w") as f:
            json.dump([task.to_dict() for task in self.tasks], f, indent=4)

    def display_tasks(self):
        if not self.tasks:
            print(Fore.YELLOW + "\nNo tasks in the list yet!\n")
            return

        print(Fore.CYAN + "\n--- Your To-Do List ---")
        for idx, task in enumerate(self.tasks, 1):
            status = Fore.GREEN + "✓" if task.completed else Fore.RED + " "
            due = f" | Due: {task.due_date}" if task.due_date else ""
            print(f"{idx}. [{status}{Style.RESET_ALL}] {task.description} | Priority: {task.priority}{due}")
        print(Fore.CYAN + "-----------------------\n")
        print(Fore.MAGENTA + f"✔ {sum(t.completed for t in self.tasks)} of {len(self.tasks)} tasks completed\n")

    def add_task(self, description: str, priority: str, due_date: str):
        new_task = Task(description, priority, due_date)
        self.tasks.append(new_task)
        self.save_tasks()
        print(Fore.GREEN + f"Task '{description}' added.")

    def complete_task(self, task_number: int):
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1].completed = True
            self.save_tasks()
            print(Fore.GREEN + f"Task {task_number} marked as complete.")
        else:
            print(Fore.RED + "Invalid task number.")

    def delete_task(self, task_number: int):
        if 0 < task_number <= len(self.tasks):
            deleted = self.tasks.pop(task_number - 1)
            self.save_tasks()
            print(Fore.GREEN + f"Task '{deleted.description}' deleted.")
        else:
            print(Fore.RED + "Invalid task number.")

    def export_to_csv(self, filename="todo_export.csv"):
        import csv
        with open(filename, "w", newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Description", "Completed", "Created At", "Priority", "Due Date"])
            for task in self.tasks:
                writer.writerow([
                    task.description,
                    "Yes" if task.completed else "No",
                    task.created_at,
                    task.priority,
                    task.due_date
                ])
        print(Fore.GREEN + f"Tasks exported to {filename}")


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    todo = ToDoList()

    while True:
        clear_screen()
        todo.display_tasks()

        print("Options:")
        print("1. Add a new task")
        print("2. Mark task as complete")
        print("3. Delete a task")
        print("4. Export tasks to CSV")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            desc = input("Enter task description: ").strip()
            priority = input("Enter priority (Low / Medium / High): ").strip().capitalize()
            if priority not in ["Low", "Medium", "High"]:
                print(Fore.YELLOW + "Invalid priority. Defaulting to 'Medium'.")
                priority = "Medium"
            due_date = input("Enter due date (YYYY-MM-DD) or leave empty: ").strip()
            todo.add_task(desc, priority, due_date)
            input("Press Enter to continue...")
        elif choice == '2':
            try:
                num = int(input("Enter task number to complete: "))
                todo.complete_task(num)
                input("Press Enter to continue...")
            except ValueError:
                print(Fore.RED + "Invalid input. Please enter a number.")
                input("Press Enter to continue...")
        elif choice == '3':
            try:
                num = int(input("Enter task number to delete: "))
                confirm = input(f"Are you sure you want to delete task {num}? (y/n): ").lower()
                if confirm == 'y':
                    todo.delete_task(num)
                else:
                    print("Deletion cancelled.")
                input("Press Enter to continue...")
            except ValueError:
                print(Fore.RED + "Invalid input. Please enter a number.")
                input("Press Enter to continue...")
        elif choice == '4':
            todo.export_to_csv()
            input("Press Enter to continue...")
        elif choice == '5':
            print("Exiting To-Do List. Goodbye!")
            break
        else:
            print(Fore.RED + "Invalid choice. Please try again.")
            input("Press Enter to continue...")


if __name__ == "__main__":
    main()
