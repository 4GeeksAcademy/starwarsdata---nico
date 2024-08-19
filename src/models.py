import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id_user = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False, unique =True)
    password = Column(String(250), nullable=False)
    date = Column(DateTime, nullable=False)

    favorites = relationship('favorites', back_populates='user')

class Character(Base):
    __tablename__ = 'character'
    id_character = Column(Integer, primary_key=True)
    name = Column(String(250))
    description = Column(String(250))

    favorites = relationship('Favorites', back_populates='character')

class Planet(Base):
    __tablename__ = 'Planet'
    id_character = Column(Integer, primary_key=True)
    name = Column(String(250))
    description = Column(String(250))

    favorites = relationship('Favorites', back_populates='planet')


class Favorite(Base):
    __tablename__ = 'favorite'
    id_favorite = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id_user'), nullable=False)
    character_id = Column(Integer, ForeignKey('character.id_character'), nullable=True)
    planet_id = Column(Integer, ForeignKey('planet.id_planet'), nullable=True)

    user = relationship('User', back_populates = 'favorites')
    character = relationship('Character', back_populates = 'favorites')
    planet = relationship('Planet', back_populates = 'favorites')   

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
