#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models import storage_mode
from sqlalchemy import Column, String


class Amenity(BaseModel, Base):
    '''class amenity'''
    __tablename__ = 'amenities'
    if storage_mode == 'db':
        name = Column(String(128), nullable=False)
    else:
        name = ""
