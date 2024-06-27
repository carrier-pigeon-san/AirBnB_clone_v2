#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Table, Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship

metadata = Base.metadata

place_amenity = Table(
    'place_amenity',
    metadata,
    Column('place_id', String(60), ForeignKey('places.id'), primary_key=True,
           nullable=False),
    Column('amenity_id', String(60), ForeignKey('amenities.id'),
           primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    reviews = relationship("Review", backref='place',
                           cascade='all, delete-orphan')
    amenities = relationship("place_amenity", secondary=place_amenity,
                             viewonly=False)
    amenity_ids = []

    @property
    def reviews(self):
        from models import storage as fs
        from models.review import Review

        review_objs = fs.all(Review)
        place_reviews = []
        for value in review_objs.values():
            if value.place_id == self.id:
                place_reviews.append(value)
        return place_reviews

    @property
    def amenities(self):
        from models import storage as fs
        from models.amenity import Amenity

        amenity_objs = fs.all(Amenity)
        place_amenities = []
        for value in amenity_objs.values():
            if value.id in self.amenity_ids:
                place_amenities.append(value)
        return place_amenities

    @amenities.setter
    def amenities(self, value):
        from amenity import Amenity

        if isinstance(value, Amenity):
            self.amenity_ids.append(value.id)
