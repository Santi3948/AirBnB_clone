#!/usr/bin/python3
"""unittest file storage doc"""
import unittest
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class FileStorage(unittest.TestCase):
    """test_file_storage doc"""
    def test_docstring(self):
        """test for docstrings"""
        self.assertIsNotNone(FileStorage.__doc__)

    def test_file_storage(self):
        """test_file_storage doc"""
        bm = BaseModel()
        self.assertIsInstance(storage.all(), dict)
        self.assertIsInstance(storage.new(bm), type(None))
        self.assertIsInstance(storage.save(), type(None))
        self.assertIsInstance(storage.reload(), type(None))


if __name__ == '__main__':
    unittest.main()
