#!/usr/bin/env python3

from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker  # Updated import for SQLAlchemy 2.0

Base = declarative_base()  # No more deprecation warning

class Dog(Base):
    __tablename__ = 'dogs'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    breed = Column(String, nullable=False)

# Create the database engine
engine = create_engine('sqlite:///dogs.db')

# Create a session factory
Session = sessionmaker(bind=engine)
session = Session()
