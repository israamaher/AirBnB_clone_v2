#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os
from models import storage_mode


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    if storage_mode == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state",
                              cascade='all, delete, delete-orphan')

    else:
        name = ''

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)

    if storage_mode != "db":
        @property
        def cities(self):
            '''
            Return a list of cities with state_id
            equal to the current State.id
            '''
            from models import storage
            from models.city import City

            all_cities = storage.all(City)
            cities_list = []

            for city in all_cities.items():
                if city.state_id == self.id:
                    cities_list.append(city)

            return cities_list
