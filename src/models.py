import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    First_name = Column(String(250), nullable=False)
    Last_name = Column(String(250), nullable=False)
    Email = Column(String(120), nullable=False)
    Last_name = Column(String(250), nullable=False)
    Password = Column(String(40), nullable=False)

class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    planet_name = Column(String(250), nullable=False)
    planet_description = Column(String(250), nullable=False)
   
class Character(Base):
    __tablename__ = 'Character'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    character_name = Column(String(250), nullable=False)
    character_description = Column(String(250), nullable=False)

class Favorites(Base):
    __tablename__ = 'Favorites'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    planets_id = Column(Integer, ForeignKey('planets.id'))
    Planets = relationship(Planets)
    character_id = Column(Integer, ForeignKey('character.id'))
    character = relationship(Character)
    

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')