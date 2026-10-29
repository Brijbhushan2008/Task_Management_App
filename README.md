# Task_Management_App
A beginner-friendly Python console application that lets a user create a to-do list with authentication and file-based persistence.

---

## 🌟 What this app does

This app lets a user:
- Register a new account
- Log in with a saved account
- Add new tasks
- View existing tasks
- Delete tasks by number
- Update task text
- Keep tasks saved between sessions

It runs in the terminal and uses color output for readability.

---

## 📁 Project files

- `Task_management_app.py` — The main Python program.
- `user.txt` — Stores user credentials as `username:hashed_password` in the same app folder.
- `tasks_<username>.txt` — Stores each user's tasks separately in the same app folder.

> Note: This project is educational. Passwords are hashed with SHA-256, but it is still not suitable for real production use.

---

## 🚀 How the app starts

When the program runs, it performs these steps:
1. Imports `time`, `os`, `hashlib`, and `colorama`.
2. Initializes `colorama` so printed text appears in color.
3. Clears the terminal using a cross-platform helper.
4. Loads saved user accounts from `user.txt`.
5. Shows the login/sign-in menu.
6. After successful login, loads the current user's task file.
7. Opens the task manager menu.

---

## 🔧 Core functions explained

### `save_tasks(tasks, filename='tasks.txt')`

Saves the current task list to a file.

- Opens the given file in write mode.
- Writes each task on its own line.
- Replaces the file contents so the saved tasks always match the app state.

Example:
- Input: `['Buy milk', 'Complete homework']`
- Result: `tasks_<username>.txt` contains:
  - `Buy milk`
  - `Complete homework`

---

### `load_tasks(filename='tasks.txt')`

Loads tasks from a file and returns them as a list.

- Opens the task file if it exists.
- Reads every line and strips newline characters.
- Returns an empty list if the file is missing.

This is how the app remembers tasks between runs for each user.

---

### `hash_password(password)`

Creates a SHA-256 hash of a password.

- Converts the plain password into a secure hash.
- Stores only the hash to avoid saving raw passwords.

This improves security compared with plain text credentials.

---

### `save_user(username, password)`

Adds a new user account to `user.txt`.

- Receives a username and password.
- Hashes the password before saving.
- Appends a line like `alice:5e884898...` to the file.

---

### `load_users()`

Loads all stored user accounts.

- Reads `user.txt` line by line.
- Splits each line at `:` into username and password hash.
- Returns a dictionary like:
  - `{ 'alice': '5e884898...', 'bob': '2c1743a...' }`
- Returns `{}` if the file does not exist.

---

### `get_task_filename(username)`

Returns the task file name for a user.

- Uses the format `tasks_<username>.txt`.
- Ensures each user has their own task list file.

---

### `task_manager()`

The main task management interface.

#### What it does:
- Displays a colored task manager header
- Shows current tasks if any exist
- Provides options to add, view, delete, update, or exit
- Keeps running until the user chooses Exit

#### Menu behavior:

1. **Add task**
   - Prompts for new task text
   - Ignores empty input
   - Saves the task to the current user's task file

2. **View tasks**
   - Shows all tasks with numbers
   - Displays a friendly message if there are no tasks

3. **Delete task**
   - Shows numbered task list
   - Prompts for the task number to remove
   - Validates the input before deleting
   - Saves the updated task list

4. **Update task**
   - Shows numbered task list
   - Prompts for the task number to update
   - Replaces the selected task text
   - Saves the updated task list

5. **Exit**
   - Saves tasks again
   - Prints a goodbye message
   - Returns control to the main menu

---

### `sign_in()`

Handles account creation and login.

#### Menu options:
- `1` Sign-in — create a new account
- `2` Login — access the task manager
- `3` Exit — close the program

#### Sign-in flow:
- Prompts for username and password
- If the username already exists, asks the user to log in
- Otherwise saves the new user and returns to the login menu

#### Login flow:
- Prompts for username and password
- Hashes the password and compares it to the stored hash
- If valid, loads the current user's tasks and launches the task manager
- If invalid, prints an error and returns to the login menu

#### Exit flow:
- Prints `Goodbye!`
- Stops the program

---

## 📝 Usage instructions

Open a Windows terminal and run:

```powershell
python "Task_management_app.py"
```

Then follow the menu:
1. Select `1` to register a new account.
2. Select `2` to log in.
3. Use the task manager options after login.
4. Select `5` inside the task manager to exit.

---

## 🧠 Program entry point

The app uses a `main()` function and an `if __name__ == "__main__":` guard:

```python
def main():
    sign_in()

if __name__ == "__main__":
    main()
```

This ensures the login flow runs only when the file is executed directly. If the file is imported, the functions are loaded without starting the app.

---

## ✅ Why this project is useful

- Demonstrates user authentication and file storage.
- Shows how to hash passwords safely.
- Teaches menu-driven console application design.
- Helps beginners practice Python I/O and control flow.

---

## 🎯 Summary

This app is a beginner-level task manager with authentication. It uses hashed passwords, separate task files for each user, and a clean console interface.

It also uses a Python `main()` entry point and an `if __name__ == "__main__":` guard so it works correctly when run directly or imported.

