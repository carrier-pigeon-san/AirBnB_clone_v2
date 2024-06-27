#!/usr/bin/python3
"""This module contains the class Amenity that handles amenity objects
that will be attributed to objects of Place class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """This class """
    from models.place import place_amenity
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary=place_amenity)
