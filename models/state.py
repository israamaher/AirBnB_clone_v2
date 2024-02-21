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

            for _, v in all_cities.items():
                if v.state_id == self.id:
                    cities_list.append(v)

            return cities_list
