#!/usr/bin/python3
"""unittest state doc"""
import unittest
from models.base_model import BaseModel
from models.state import State


class test_state(unittest.TestCase):
    """test_state doc"""
    def test_docstring(self):
        """test for docstrings"""
        self.assertIsNotNone(State.__doc__)

    def test_state(self):
        """test_state doc"""
        state = State()
        self.assertIsInstance(state, State)
        self.assertIsInstance(state.name, str)
        self.assertEqual(str(state), "[{}] ({}) \
<{}>".format(state.__class__.__name__, state.id, state.__dict__))
        state.save()
        self.assertNotEqual(state.created_at, state.updated_at)
        test_dict = state.to_dict()
        self.assertIsInstance(test_dict, dict)
        self.assertEqual(test_dict, state.to_dict())


if __name__ == '__main__':
    unittest.main()
