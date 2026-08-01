

import json
import os

DATA_FILE = "tasks.json"



# STORAGE + PERSISTENCE

def load_tasks():
    """Read saved tasks from disk, if any exist."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []


def save_tasks(tasks):
    """Write the current task list to disk."""
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=2)


# PROCESS (the logic that changes the data)

def add_task(tasks):
    """Ask the user for a task and append it to the list."""
    task_name = input("Enter a new task: ").strip()

    if task_name == "":
        print("⚠️  Task cannot be empty. Nothing was added.\n")
        return

    task = {"task": task_name, "done": False}
    tasks.append(task)          # <-- the core skill: list.append()
    save_tasks(tasks)
    print(f"✅ Added: '{task_name}'\n")


def complete_task(tasks):
    """Mark a task as done by its number."""
    view_tasks(tasks)
    if not tasks:
        return

    choice = input("Enter the task number to mark as done: ").strip()
    if not choice.isdigit() or not (1 <= int(choice) <= len(tasks)):
        print("⚠️  Invalid task number.\n")
        return

    index = int(choice) - 1
    tasks[index]["done"] = True
    save_tasks(tasks)
    print(f"🎉 Marked '{tasks[index]['task']}' as done!\n")


def delete_task(tasks):
    """Remove a task by its number."""
    view_tasks(tasks)
    if not tasks:
        return

    choice = input("Enter the task number to delete: ").strip()
    if not choice.isdigit() or not (1 <= int(choice) <= len(tasks)):
        print("⚠️  Invalid task number.\n")
        return

    index = int(choice) - 1
    removed = tasks.pop(index)
    save_tasks(tasks)
    print(f"🗑️  Removed: '{removed['task']}'\n")


 
# DISPLAY (the read-only view of the data)

def view_tasks(tasks):
    """Print every task with its index and status."""
    print("\n----- YOUR TO-DO LIST -----")
    if not tasks:
        print("No tasks yet. Add one from the menu!")
    else:
        # enumerate() gives (index, value) together -- the
        # "professional" way shown in the slides, instead of
        # manually looping with range(len(tasks)).
        for i, task in enumerate(tasks, start=1):
            status = "✔" if task["done"] else " "
            print(f"[{status}] {i}. {task['task']}")
    print("----------------------------\n")


# MENU / VIEW LAYER
def show_menu():
    print("===== DecodeLabs To-Do List =====")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark a task as done")
    print("4. Delete a task")
    print("5. Exit")


def main():
    tasks = load_tasks()   # my_tasks = [] on first run, or loaded from disk

    while True:
        show_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye! Your tasks are saved in tasks.json 👋")
            break
        else:
            print("⚠️  Please choose a number between 1 and 5.\n")


# The "gatekeeper" pattern from the slides -- this block only
# runs when the file is executed directly, not when imported.
if __name__ == "__main__":
    main()
