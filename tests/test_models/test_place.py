#!/usr/bin/python3
"""unittest state doc"""
import unittest
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.user import User
from models.amenity import Amenity
from models.place import Place


class test_place(unittest.TestCase):
    """test_city doc"""
    def test_docstring(self):
        """test for docstrings"""
        self.assertIsNotNone(Place.__doc__)

    def test_place(self):
        """test_place doc"""
        user = User()
        city = City()
        place = Place()
        place.city_id = city.id
        place.user_id = user.id
        self.assertIsInstance(place, Place)
        self.assertEqual(city.id, place.city_id)
        self.assertEqual(user.id, place.user_id)
        self.assertIsInstance(place.city_id, str)
        self.assertIsInstance(place.user_id, str)
        self.assertIsInstance(place.name, str)
        self.assertIsInstance(place.description, str)
        self.assertIsInstance(place.number_rooms, int)
        self.assertIsInstance(place.number_bathrooms, int)
        self.assertIsInstance(place.max_guest, int)
        self.assertIsInstance(place.price_by_night, int)
        self.assertIsInstance(place.latitude, float)
        self.assertIsInstance(place.longitude, float)
        amenity_0 = Amenity()
        amenity_1 = Amenity()
        place.amenity_ids = [amenity_0.id, amenity_1.id]
        self.assertEqual(type(place.amenity_ids), list)
        self.assertEqual(str(place), "[{}] ({}) \
<{}>".format(place.__class__.__name__, place.id, place.__dict__))
        place.save()
        self.assertNotEqual(place.created_at, place.updated_at)
        test_dict = place.to_dict()
        self.assertIsInstance(test_dict, dict)
        self.assertEqual(test_dict, place.to_dict())


if __name__ == '__main__':
    unittest.main()
