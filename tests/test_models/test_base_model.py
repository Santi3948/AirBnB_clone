#!/usr/bin/python3
"""unittest base model doc"""
import unittest
from models.base_model import BaseModel


class test_base(unittest.TestCase):
    """test_base doc"""
    def test_base(self):
        """test_base doc"""
        # code test here!

    def test_str(self):
        """test_str doc"""
        bm = BaseModel()
        self.assertEqual(bm.__str__, f'[{self.__class__.__name__}] \
({self.id}) {self.__dict__}')

if __name__ == '__main__':
    unittest.main()
