import db
from models import Task, User, State


def search_by_user():
    user_name = (input("User name: "))
    user = db.session.query(User).filter_by(name=user_name).first()
    if user is None:
        print("\nInvalid user\n")
    else:
        if len(user.tasks) > 0:
            for task in user.tasks:
                print(f"Title: {task.title}, description: {task.description}, state: {task.state.name}, date: {task.date}\n")
        else:
            print("\nThis user does not have tasks assigned\n")


def all_tasks():
    tasks = db.session.query(Task).all()
    if len(tasks) > 0:
        for task in tasks:
            print(f"id : {task.id}, title: {task.title}, description: {task.description}, author: {task.user.name}, state: {task.state.name}, date: {task.date}\n")
            
    else:
        print("\nNo tasks found\n")


def all_tasks_user(user_login):
    tasks = db.session.query(Task).filter_by(user_id=user_login).all()
    if len(tasks) > 0:
        for task in tasks:
            print(f"id : {task.id}, title: {task.title}, description: {task.description}, state: {task.state.name}, date: {task.date}\n")
    else:
        print("\nYou don't have any tasks\n")
    return tasks


def create_task(user_login):
    title_user = input("Title: ")
    task = db.session.query(Task).filter_by(title=title_user, user_id=user_login).first()
    if task is None:
        description = input("Description: ")
        new_task = Task(title=title_user, description=description, user_id=user_login, state_id=1)
        db.session.add(new_task)
        db.session.commit()
        print("\nYour task has been created successfully!\n")
    else:
        print("\nThis task has already been  created\n")


def update_state(user_login):
    tasks = all_tasks_user(user_login)
    UPDATE_TASK = """\n
    Task Pending: select 1
    Task On-going: select 2
    Task Finished: select 3
    \n"""
    if len(tasks)> 0:
        id_task = input("Task id: ")
        task = db.session.query(Task).filter_by(id=id_task, user_id=user_login).first()
        if task is None:
            print("\nThis task does not exists\n")
        else:
            selection_update = input(UPDATE_TASK)
            db.session.query(Task).filter_by(id=id_task).update({Task.state_id: int(selection_update)})
            db.session.commit()
            print("\nTitle task has been updated\n")


def edit_task(user_login):
    tasks = all_tasks_user(user_login)
    if len(tasks)>0:
        title_task_id = int(input("Task id: "))
        task = db.session.query(Task).filter_by(id=title_task_id, user_id=user_login).first()
        if task is not None:
            title_or_description = input("Edit title or description (T/D)?: ")
            if title_or_description.lower() == "t":
                new_title = input("New title: ")
                db.session.query(Task).filter_by(title=task.title, user_id=user_login).update({Task.title: new_title})
                db.session.commit()
                print(f"\nThe title has been changed to: {new_title}\n")

            if title_or_description.lower() == "d":
                new_description = input("New description: ")
                db.session.query(Task).filter_by(description=task.description,user_id=user_login).update({Task.description: new_description})
                db.session.commit()
                print(f"\nThe description has been changed  to:  {new_description}\n")


def delete_task(user_login):
    tasks = all_tasks_user(user_login)

    if len(tasks) > 0:
        task_id = int(input("Task id: "))
        db.session.query(Task).filter_by(id=task_id, user_id=user_login).delete()
        db.session.commit()
        print("\nTask deleted\n")


def search_task_by_title(user_login):
    task_title = input("Title task: ")
    task = db.session.query(Task).filter_by(title=task_title, user_id=user_login).first()
    if task is None:
        print("\nWrong title or the task does not exist\n")
    else:
        print(f"title: {task.title}, description: {task.description}, state: {task.state.name}, date: {task.date}\n")
