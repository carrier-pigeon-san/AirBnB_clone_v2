#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone"""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker, scoped_session
from models.base_model import Base


class DBStorage:
    """This class manages storage of hbnb models in a MySQL database"""

    __engine = None
    __session = None

    def __init__(self):
        """DBStorage class instance constructor"""
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}:3306/{}'.format(
                getenv('HBNB_MYSQL_USER'),
                getenv('HBNB_MYSQL_PWD'),
                getenv('HBNB_MYSQL_HOST'),
                getenv('HBNB_MYSQL_DB')
            ),
            pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        * Query on the current database session (self.__session) all objects
          depending of the class name (argument cls)
        * If cls=None, query all types of objects (User, State, City, Amenity,
          Place and Review)
        * This method returns a dictionary: (key = <class-name>.<object-id>
          and value = object)
        """
        from models.user import User
        from models.state import State
        from models.city import City
        from models.place import Place
        from models.amenity import Amenity
        from models.review import Review

        models = {
            'State': State, 'City': City
        }
        obj_list = {}
        if cls:
            query = self.__session.query(cls).all()
            for obj in query:
                obj_list.update(
                    {'.'.join([obj.__class__.__name__, obj.id]): obj})
        else:
            for value in models.values():
                query = self.__session.query(value).all()
                for obj in query:
                    obj_list.update(
                        {'.'.join([obj.__class__.__name__, obj.id]): obj})
        return obj_list

    def new(self, obj):
        """Add the object to the current database session (self.__session)
        """
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Delete from the current database session obj if not None
        """
        from models.base_model import Base
        from models.state import State
        from models.city import City

        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)
