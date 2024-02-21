#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship
import os
import models
from models import storage


if models.storage_mode == 'db':
    place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60),
                                 ForeignKey('places.id'),
                                 primary_key=True,
                                 nullable=False),
                          Column('amenity_id', String(60),
                                 ForeignKey('amenities.id'),
                                 primary_key=True,
                                 nullable=False)
                          )


class Place(BaseModel, Base):
    """ A place to stay """
    if models.storage_mode == "db":
        __tablename__ = "places"
        city_id = Column(
            'city_id', String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(
            'user_id', String(60), ForeignKey('users.id'), nullable=False)
        name = Column("name", String(128), nullable=False)
        description = Column("description", String(1024))
        number_rooms = Column(
            "number_rooms", Integer(), nullable=False, default=0)
        number_bathrooms = Column(
            "number_bathrooms", Integer(), nullable=False, default=0)
        max_guest = Column("max_guest", Integer(), nullable=False, default=0)
        price_by_night = Column(
            "price_by_night", Integer(), nullable=False, default=0)
        latitude = Column("latitude", Float())
        longitude = Column("longitude", Float())
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
            ''' get a list all reviews'''
            all_reviews = storage.all(models.Review)
            list_reviews = []
            for i in all_reviews.values():
                if i.place_id == self.id:
                    list_reviews.append(i)
            return list_reviews

        @property
        def amenities(self):
            ''' get list amenity'''
            all_amenities = storage.all(models.Amenity)
            list_amen = []
            for a in all_amenities.values():
                if a.id in self.amenity_ids:
                    list_amen.append(a)
            return list_amen

        @amenities.setter
        def amenities(self, obj):
            ''' add id to attr '''
            if obj is not None:
                if isinstance(obj, models.Amenity):
                    if obj.id not in self.amenity_ids:
                        self.amenity_ids.append(obj.id)
