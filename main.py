from models import Task, User, State
import auth
import tasks
MENU_PROMT = """ -- Tasks app --
1) Sign up
2) Sign in
3) Search by user
4)All task
5)Exit
\n"""
MENU_USER = """ -- Tasks app --
1)Tasks list
2)Create new task
3)Change state
4)Edit task
5)Delete task
6)Search task by title
7)Exit
\n"""

user_login = None
def main():
    global user_login
    runnning = True
    while runnning:
        if user_login is None:
            user_input = input(MENU_PROMT)
            if user_input == "1":
                auth.create_user()
            elif user_input == "2":
                user_login = auth.login()
            elif user_input == "3":
                tasks.search_by_user()
            elif user_input == "4":
                tasks.all_tasks()
            elif user_input == "5":
                runnning = False
            else:
                print("Invalid command")
        else:
            user_input = input(MENU_USER)
            if user_input == "1":
                tasks.all_tasks_user(user_login)
            elif user_input == "2":
                tasks.create_task(user_login)
            elif user_input == "3":
                tasks.update_state(user_login)
            elif user_input == "4":
                tasks.edit_task(user_login)
            elif user_input == "5":
                tasks.delete_task(user_login)
            elif user_input == "6":
                tasks.search_task_by_title(user_login)
            elif user_input == "7":
                user_login = None
            else:
                print("Invalid command\n")


main()
