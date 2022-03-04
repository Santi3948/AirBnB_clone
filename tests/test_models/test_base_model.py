#!/usr/bin/python3
"""unittest base model doc"""
import unittest
from datetime import datetime
from models.base_model import BaseModel


class test_base_model(unittest.TestCase):
    """test_base doc"""
    def test_docstring(self):
        """test for docstrings"""
        self.assertIsNotNone(BaseModel.__doc__)

    def test_base(self):
        """test_base doc"""
        bm = BaseModel()
        self.assertEqual(isinstance(bm, BaseModel), True)
        self.assertEqual(isinstance(bm.id, str), True)
        self.assertEqual(type(bm.created_at), datetime)
        self.assertIsInstance(bm.updated_at, datetime)
        self.assertEqual(str(bm), f"[{bm.__class__.__name__}] \
({bm.id}) {bm.__dict__}")
        bm.save()
        self.assertNotEqual(bm.created_at, bm.updated_at)
        test_dict = bm.to_dict()
        self.assertEqual(type(test_dict), dict)
        self.assertEqual(test_dict, bm.to_dict())
        self.assertEqual(type(test_dict["created_at"]), str)
        self.assertEqual(type(test_dict["updated_at"]), str)


if __name__ == '__main__':
    unittest.main()
