#!/usr/bin/python3
"""this module defines a class to manage database storage """
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.base_model import Base
import os
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity

classes = {"Amenity": Amenity, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class DBStorage:
    """this class manage the storage"""
    __engine = None
    __session = None

    def __init__(self) -> None:
        """Instantiate a DBStorage object"""
        user = os.getenv('HBNB_MYSQL_USER')
        pwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')

        engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(user, pwd, host, db),
            pool_pre_ping=True)

        self.__engine = engine
        self.__metadata_obj = Base.metadata

        if (os.getenv('HBNB_TYPE_STORAGE') == 'test'):
            self.__metadata_obj.drop_all(bind=self.__engine, checkfirst=True)

    def all(self, cls=None):
        """Return a dictionary of model from database"""
        result_map = {}
        object = []

        if cls:
            objects = self.__session.query(cls).all()
            for object in objects:
                dictified = object.to_dict()
                result_map.update(
                    {dictified['__class__'] + '.' + object.id: object})
        else:
            for cls in classes:
                objects.append(self.__session.query(cls).all())

            for object_list in objects:
                for object in object_list:
                    dictified = object.to_dict()
                    result_map.update(
                        {dictified['__class__'] + '.' + object.id: object})

        return result_map

    def new(self, obj=None):
        """Add a new object to the current session"""
        if obj is None:
            return None
        self.__session.add(obj)

    def save(self):
        """Commit all session changes to the database"""
        self.__session.commit()

    def delete(self, obj=None):
        """deletes the passed object from database"""
        if obj is None:
            return None
        self.__session.query(type(obj)).filter(
                type(obj).id == obj.id).delete()

    def reload(self):
        """creat all tables"""
        self.__metadata_obj.create_all(bind=self.__engine)

        session_factory = sessionmaker(self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_factory)

    def close(self):
        """ close the current session"""
        self.__session.remove()
