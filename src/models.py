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
    name = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    favorites = relationship("favorites")

class Favorites(Base):
    __tablename__ = "favorites"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    people_id = Column(Integer)
    planets_id = Column(Integer)
    vehicles_id = Column(Integer)
    user = relationship("user")  
    people = relationship("people")
    vehicles = relationship("vehicles")
    planets = relationship("planets")

class People(Base):
    __tablename__ = "people"
    id = Column(Integer, primary_key=True)
    people_id = Column(Integer, ForeignKey("favorites.people_id"))
    name = Column(String(150), nullable=False)
    gender = Column(String(150), nullable=False)
    hair_color = Column(String(150), nullable=False)
    eye_color = Column(String(150), nullable=False)
    favorites = relationship("favorites")

class Vehicles(Base):
    __tablename__ = "vehicles"
    id = Column(Integer, primary_key=True)
    vehicles_id = Column(Integer, ForeignKey("favorites.vehicles_id") )
    name = Column(String(250))
    manufacture = Column(String(250))
    model = Column(String(250))
    favorites = relationship("favorites")

class Planets(Base):
    __tablename__ = "planets"
    id = Column(Integer, primary_key=True)
    plantes_id = Column(Integer, ForeignKey("favorites.planets_id"))
    name = Column(String(250))
    Population = Column(String(250))
    Terrain = Column(String(250))
    favorites = relationship("favorites")

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')