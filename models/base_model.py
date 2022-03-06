#!/usr/bin/python3
"""Model Base module doc"""

from datetime import datetime
from uuid import uuid4
from models import storage


class BaseModel():
    """class BaseModel doc"""

    def __init__(self, *args, **kwargs):
        """constructor method doc"""
        if len(kwargs) > 0:
            for key in kwargs:
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        setattr(self, key, datetime.strptime(kwargs[key], '%Y\
-%m-%dT%H:%M:%S.%f'))
                    else:
                        setattr(self, key, kwargs[key])
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """str doc"""
        return "[{}] ({}) \
<{}>".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """save doc"""
        storage.save()
        self.updated_at = datetime.now()

    def to_dict(self):
        """to dict doc"""
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = self.__class__.__name__
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        return my_dict
