#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from models import HBNB_TYPE_STORAGE
from sqlalchemy import Column, String, ForeignKey, Float, Integer
from sqlalchemy.orm import relationship
from models.review import Review

if HBNB_TYPE_STORAGE == 'db':
    place_amenity = Table('place_amenity', Base.metadata,
                    place_id = Column(String(60),
                        ForeignKey('places.id'), primary_key=True,
                        nullable=False)
                    amenity_id = Column(String(60),
                        ForeignKey('amenities.id'), primary_key=True,
                        nullable=False))

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'

    if HBNB_TYPE_STORAGE == 'db':
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship('Review', backref='place', cascade='all, delete')
        amenities = relationship('Amenity', secondary=place_amenity, viewonly=False, backref='place_amenity')
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            from models import storage
            """returns the list of Review instances with
            place_id equals to the current Place.id"""
            reviewList = []

            all_obj = storage.all(Review)

            for obj in all_obj:
                if self.id == obj.place_id:
                    reviewList.append[obj]
            return reviewList

         @property
        def amenities(self):
            """getter attribute amenities that returns the list of Amenity
            instances based on the attribute amenity_ids that contains all
            Amenity.id linked to the Place"""
            from models import storage
            from models.amenity import Amenity
            amenities = []
            for amenity in storage.all(Amenity).values():
                if amenity.id in self.amenity_ids:
                    amenities.append(amenity)
            return amenities

        @amenities.setter
        def amenities(self, obj):
            """setter attribute amenities that handles append method for adding"""
            from models.amenity import Amenity
            if type(obj) == type(Amenity):
                self.amenity_ids.append(obj.id)
