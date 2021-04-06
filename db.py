from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine =  create_engine('sqlite:///database.db')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()