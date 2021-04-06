import db
from sqlalchemy.sql import func
from sqlalchemy import  Column, Integer, String, ForeignKey, Date, delete, update
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(60), nullable=False)
    last_name = Column(String(60), nullable=False)
    email = Column(String(60), nullable=False)
    password_hash = Column(String(60), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
        
class Task(db.Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    title = Column(String(60), nullable=False)
    description = Column(String(255), nullable = False)
    date = Column(Date, default=func.now())
    state_id = Column(Integer, ForeignKey('states.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    
    user = relationship('User', primaryjoin='Task.user_id == User.id', back_populates = 'tasks') 
    state = relationship('State', primaryjoin='Task.state_id == State.id', back_populates ='tasks')     

class State(db.Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(60))
    description = Column(String(60))
    tasks = relationship('Task', back_populates='state')

def create_state_table():
    state_table = db.session.query(State).all()
    if len(state_table) == 0:
        db.session.add_all([
            State(name="Pending", description="This task is pending"),
            State(name="On-going", description="Task in process"),
            State(name="Done", description="This task is finished")
            ])
        db.session.commit()    

User.tasks = relationship("Task", order_by = Task.id, back_populates = "user")
db.Base.metadata.create_all(db.engine)
create_state_table()

