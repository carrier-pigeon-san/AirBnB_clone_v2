#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)
    cities = relationship("City", backref='state',
                          cascade='all, delete-orphan')

    @property
    def cities(self):
        from models import storage as fs
        from models.city import City

        cty_objs = fs.all(City)
        state_cities = []
        for value in cty_objs.values():
            if value.get('state_id') == self.id:
                state_cities.append(value)
        return state_cities
