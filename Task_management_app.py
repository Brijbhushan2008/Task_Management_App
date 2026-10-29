import time 
import os  
import hashlib
from colorama import Fore , Style , init , Back
init(autoreset=True)

def clear_screen():
    """Clear the terminal screen in a cross-platform way."""
    os.system('cls' if os.name == 'nt' else 'clear')

clear_screen()

#------------------------------File Handling------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
USER_FILE = os.path.join(BASE_DIR, "user.txt")
TASK_FILE_TEMPLATE = os.path.join(BASE_DIR, "tasks_{}.txt")

def get_task_filename(username):
    """Return the task filename for a specific user."""
    return TASK_FILE_TEMPLATE.format(username)


def hash_password(password):
    """Return the SHA-256 hash of the password."""
    return hashlib.sha256(password.encode('utf-8')).hexdigest()


def save_tasks(tasks, filename='tasks.txt'):
    """Save the list of tasks to the selected filename."""
    with open(filename, 'w', encoding='utf-8') as f:
        for task in tasks:
            f.write(task + '\n')


def load_tasks(filename='tasks.txt'):
    """Load tasks from a file and return them as a list."""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        return []


def save_user(username, password):
    hashed_password = hash_password(password)
    with open(USER_FILE, 'a', encoding='utf-8') as f:
        f.write(f"{username}:{hashed_password}\n")


def load_users():
    users = {}
    try:
        with open(USER_FILE, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(":")
                if len(parts) != 2:
                    continue
                username, password_hash = parts
                users[username] = password_hash
    except FileNotFoundError:
        pass
    return users

#-------------------------------Main Program-----------------------------------------

tasks = []
current_user = None

def task_manager():
    global tasks

    print(f"{Fore.YELLOW+Style.BRIGHT}\n>-======-[TASK MANAGER]-======-<\n")

    if not tasks:
        print(f'{Fore.RED+Style.BRIGHT}>--You have no previous tasks--<')
    else:
        time.sleep(1)
        print(f'{Fore.GREEN+Style.BRIGHT}Your previous tasks are:')
        for i, task in enumerate(tasks, start=1):
            print(f'{i}.{task}')

    time.sleep(1)

    print(f"\n1.[ADD]\n2.[VIEW]\n3.[DELETE]\n4.[UPDATE]\n{Style.BRIGHT}5.[EXIT]")

    while True:
        operation = input("What do you want to do(just type num): ").strip()

        if operation == "1":       #ADD
            new_task = input("\nEnter task you want to add: ").strip()
            if not new_task:
                print(f"{Fore.LIGHTCYAN_EX+Style.DIM}>--Nothing is added--<\n")
            else:
                tasks.append(new_task)
                save_tasks(tasks, get_task_filename(current_user))
                print(f"{Fore.LIGHTMAGENTA_EX+Style.DIM}\n>- [{new_task}] -< has been successfully added...\n")
                time.sleep(1)

        elif operation == "2":     #VIEW
            if not tasks:
                print(f"{Fore.LIGHTCYAN_EX+Style.DIM}>--You haven't added anything yet--<\n")
            else:
                print(f'\n{Fore.LIGHTGREEN_EX}Your tasks are:')
                for i, task in enumerate(tasks, start=1):
                    print(f'{i}.{task}')
                print('\n')
                time.sleep(1)

        elif operation == "3":     #DELETE
            if not tasks:
                print(f"{Fore.LIGHTCYAN_EX+Style.DIM}>--There is nothing to delete--<\n")
            else:
                print(f'\n{Fore.LIGHTGREEN_EX}Your tasks are:')
                for i, task in enumerate(tasks, start=1):
                    print(f'{i}.{task}')
                del_task = input("Enter task number you want to delete:").strip()
                if del_task.isdigit():
                    del_task = int(del_task)
                    if 1 <= del_task <= len(tasks):
                        old_val1 = tasks.pop(del_task - 1)
                        save_tasks(tasks, get_task_filename(current_user))
                        print(f"{Fore.LIGHTMAGENTA_EX+Style.DIM}\n>- [{old_val1}] -< has been deleted successfully..\n")
                        time.sleep(1)
                    else:
                        print(f"{Fore.LIGHTRED_EX+Style.DIM}!!Invalid task number!!\n")
                else:
                    print(f"{Fore.LIGHTCYAN_EX+Style.DIM}>--Please enter a valid number--<\n")

        elif operation == "4":       #UPDATE
            if not tasks:
                print(f"{Fore.LIGHTCYAN_EX+Style.DIM}>--You don't have any task yet--<\n")
            else:  
                print(f'\n{Fore.LIGHTGREEN_EX}Your tasks are:')
                for i, task in enumerate(tasks, start=1):
                    print(f'{i}.{task}') 
                update_val = input("Which one you want to update:").strip()
                if update_val.isdigit():
                    update_index = int(update_val)
                    if 1 <= update_index <= len(tasks):
                        ch_val = input("Enter what you want to update it with:").strip()
                        old_val2 = tasks[update_index - 1]
                        tasks[update_index - 1] = ch_val
                        save_tasks(tasks, get_task_filename(current_user))
                        print(f"{Fore.LIGHTMAGENTA_EX+Style.DIM}\n>- [{old_val2}] -< has been changed to >- [{ch_val}] -<\n")
                        time.sleep(1)
                    else:
                        print(f"{Fore.LIGHTRED_EX+Style.DIM}!!Invalid task number!!\n")
                else:
                    print(f"{Fore.LIGHTCYAN_EX+Style.DIM}>--Please enter a valid number--<\n")

        elif operation == "5":        #EXIT
            save_tasks(tasks, get_task_filename(current_user))
            print(f"{Fore.MAGENTA+Style.BRIGHT}\n>---Thanks for using the APP. Have a nice day😊---<\n\nDeveloped by :-  BRIJBHUSHAN SHARMA")
            time.sleep(1)
            break
        else:
            print(f"{Fore.LIGHTRED_EX+Style.DIM}!! Invalid input !!\n") 

#----------------------------------Authentication---------------------------------------

def sign_in():
    global current_user, tasks
    users = load_users()
    print(f'{Fore.YELLOW+Style.BRIGHT}Welcome to task manager\n')
    while True:
        choice = input('1.[SIGN-IN]\n2.[LOGIN]\n3.[EXIT]\nEnter choice:').strip()

        if choice == "1":                      #Sign-in
            username = input("\nEnter new username:").strip()
            password = input("Enter new password:").strip()
            if username in users:
                print(f'{Fore.LIGHTCYAN_EX+Style.DIM}\n[ Username already exists! Try logging in instead ]\n')
            else:
                save_user(username, password)
                users[username] = hash_password(password)
                print(f'{Fore.MAGENTA+Style.BRIGHT}\n[ Sign-in successful! Please login now. ]\n')
                time.sleep(1)

        elif choice == "2":                     #Login
            username = input('\nEnter username:').strip()
            password = input('Enter password:').strip()
            password_hash = hash_password(password)
            if username in users and users[username] == password_hash:
                current_user = username
                tasks = load_tasks(get_task_filename(username))
                print(f'{Fore.MAGENTA+Style.BRIGHT}\n[ Login successful ]\n')
                time.sleep(1)
                print(f'{Fore.CYAN+Style.BRIGHT}\nLOADING....')
                time.sleep(3)
                clear_screen()
                task_manager()
                break
            else:
                print(f'{Fore.LIGHTRED_EX+Style.DIM}\nWrong username or password!\n')

        elif choice == "3":                      #Exit
            print(f'{Fore.GREEN+Style.BRIGHT}\nGoodbye!\n')
            time.sleep(1)
            break
        else:
            print(f'{Fore.LIGHTRED_EX+Style.DIM}\nINVALID CHOICE!\n')

#-----------------------------------------------------------------------------------------

def main():
    sign_in()


if __name__ == "__main__":
    main()
