#!/usr/bin/python3
"""unittest user doc"""
import unittest
from models.base_model import BaseModel
from models.user import User


class test_user(unittest.TestCase):
    """test_user doc"""
    def test_docstring(self):
        """test for docstrings"""
        self.assertIsNotNone(User.__doc__)

    def test_user(self):
        """test_user doc"""
        user = User()
        self.assertIsInstance(user, User)
        self.assertIsInstance(user.email, str)
        self.assertIsInstance(user.password, str)
        self.assertIsInstance(user.first_name, str)
        self.assertIsInstance(user.last_name, str)
        self.assertEqual(str(user), "[{}] \
({}) <{}>".format(user.__class__.__name__, user.id, user.__dict__))
        user.save()
        self.assertNotEqual(user.created_at, user.updated_at)
        test_dict = user.to_dict()
        self.assertIsInstance(test_dict, dict)
        self.assertEqual(test_dict, user.to_dict())


if __name__ == '__main__':
    unittest.main()
