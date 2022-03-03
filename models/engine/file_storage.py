#!/usr/bin/python3
"""file_storage module doc"""
import json


class FileStorage:
    """class FileStorage doc"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """method all doc"""
        return self.__objects

    def new(self, obj):
        """method new doc"""
        self.__objects[f'{type(obj).__name__}.{obj.id}'] = obj

    def save(self):
        """method save doc"""
        my_dict = {}
        with open(self.__file_path, 'w+') as f:
            for key, value in self.__objects.items():
                my_dict[key] = value.to_dict()
            json.dump(my_dict, f)

    def reload(self):
        """method reload doc"""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        try:
            with open(self.__file_path, 'r') as f:
                new_dict = json.load(f)
                for key, value in new_dict.items():
                    class_base = str(key).split(".")
                    self.__objects[key] = eval(class_base[0])(**value)
        except Exception:
            return
