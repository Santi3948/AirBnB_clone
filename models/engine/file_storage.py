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
        return __objects

    def new(self, obj):
        """method new doc"""
        self.__objects[obj.__class__.__name__.id] = obj

    def save(self):
        """method save doc"""
        self.__file_path = __objects.__dict__
