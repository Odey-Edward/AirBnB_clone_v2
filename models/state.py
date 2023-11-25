#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models import HBNB_TYPE_STORAGE


class State(BaseModel, Base):
    """ State class """

    __tablename__ = 'states'

    if HBNB_TYPE_STORAGE == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state', cascade='all, delete')
    else:
        name = ""

        @property
        def cities(self):
            """ returns the list of City instances with state_id
            equals to the current State.id"""
            from models import storage
            cityObj = storage.all(City)

            matchedCity = []

            for key in cityObj:
                if cityObj[key].state_id == self.id:
                    matchedCity.append(cityObj[key])

            return (matchedCity)
