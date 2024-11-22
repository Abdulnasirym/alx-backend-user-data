#!/usr/bin/python3
""" A module that create a user model """

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, create_engine

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)


engine = create_engine('sqlite:///test.db')
Base.metadata.create_all(engine)
