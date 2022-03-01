#!/usr/bin/python3
"""Model Base module doc"""
from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel():
    """class BaseModel doc"""

    def __init__(self, *args, **kwargs):
        """constructor method doc"""
        if len(kwargs) > 0:
            for key in kwargs:
                if key != "__class__":
                    setattr(self, key, kwargs[key])
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now().isoformat("#", "microseconds")
            self.updated_at = datetime.now().isoformat("#", "microseconds")
            storage.new(self)

    def __str__(self):
        """str doc"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """save doc"""
        storage.save()
        self.updated_at = datetime.now()

    def to_dict(self):
        """to dict doc"""
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = self.__class__.__name__
        my_dict["created_at"] = str(my_dict["created_at"])
        my_dict["updated_at"] = str(my_dict["updated_at"])
        return my_dict
