#!/usr/bin/python3
"""unittest state doc"""
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class test_amenity(unittest.TestCase):
    """test_amenity doc"""
    def test_docstring(self):
        """test for docstrings"""
        self.assertIsNotNone(Amenity.__doc__)

    def test_amenity(self):
        """test_amenity doc"""
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)
        self.assertIsInstance(amenity.name, str)
        self.assertEqual(str(amenity), "[{}] \
({}) {}".format(amenity.__class__.__name__, amenity.id, amenity.__dict__))
        amenity.save()
        self.assertNotEqual(amenity.created_at, amenity.updated_at)
        test_dict = amenity.to_dict()
        self.assertIsInstance(test_dict, dict)
        self.assertEqual(test_dict, amenity.to_dict())


if __name__ == '__main__':
    unittest.main()
