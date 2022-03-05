#!/usr/bin/python3
"""unittest state doc"""
import unittest
from models.base_model import BaseModel
from models.state import State
from models.city import City


class test_state(unittest.TestCase):
    """test_city doc"""
    def test_docstring(self):
        """test for docstrings"""
        self.assertIsNotNone(State.__doc__)

    def test_city(self):
        """test_city doc"""
        state = State()
        city = City()
        city.state_id = state.id
        self.assertIsInstance(city, City)
        self.assertEqual(state.id, city.state_id)
        self.assertIsInstance(city.name, str)
        self.assertEqual(str(city), "[{}] ({}) \
<{}>".format(city.__class__.__name__, city.id, city.__dict__))
        city.save()
        self.assertNotEqual(city.created_at, city.updated_at)
        test_dict = city.to_dict()
        self.assertIsInstance(test_dict, dict)
        self.assertEqual(test_dict, city.to_dict())


if __name__ == '__main__':
    unittest.main()
