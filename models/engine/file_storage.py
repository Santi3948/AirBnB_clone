#!/usr/bin/python3
"""file_storage module doc"""
import json
from os import path


class FileStorage:
    """class FileStorage doc"""
    __file_path = __file__
    __objects = {}

    def all(self):
        """method all doc"""
        return self.__objects

    def new(self, obj):
        """method new doc"""
        self.__objects[f"{type(obj).__name__}.{obj.id}"] = obj.to_dict()

    def save(self):
        """method save doc"""
        try:
            with open (self.__file_path, 'w+') as f:
                f.write(js.dump(self.__objects, f))
        except Exception:
            return

    def reload(self):
        """ethod reload doc"""
       try:
            with open (self.__file_path) as f:
                self.__objects = js.loads(f)
				return self.__objects
        except Exception:
            return 
