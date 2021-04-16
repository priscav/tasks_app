import db
from prompt_toolkit import prompt
from models import Task, User, State


def create_user():
    name = input("Name: ")
    last_name = input("Last_name: ")
    email_ = input("Email: ")
    password_user = prompt("Password: ", is_password=True)
    user = db.session.query(User).filter_by(email=email_).first()
    if user is None:
        new_user = User(name=name, last_name=last_name, email=email_)
        new_user.set_password(password_user)
        db.session.add(new_user)
        db.session.commit()
        print("\nUser created!\n")
    else:
        print("\nThis user already exists\n")


def login():
    email_ = input("Email: ")
    user = db.session.query(User).filter_by(email=email_).first()
    if user is not None:
        password_user = prompt("Password: ", is_password=True)
        if user.check_password(password_user):
            print("\nYou are logged-in\n")
            return user.id
        else:
            print("\nPassword is incorrect\n")
    else:
        print("\nThis user does not exist\n")
