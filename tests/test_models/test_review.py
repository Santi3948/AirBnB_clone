#!/usr/bin/python3
"""unittest review doc"""
import unittest
from models.base_model import BaseModel
from models.review import Review
from models.place import Place
from models.user import User


class test_review(unittest.TestCase):
    """test_review doc"""
    def test_docstring(self):
        """test for docstrings"""
        self.assertIsNotNone(Review.__doc__)

    def test_review(self):
        """test_review doc"""
        review = Review()
        place = Place()
        user = User()
        review.place_id = place.id
        review.user_id = user.id
        self.assertIsInstance(review, Review)
        self.assertIsInstance(review.place_id, str)
        self.assertEqual(review.place_id, place.id)
        self.assertIsInstance(review.user_id, str)
        self.assertEqual(review.user_id, user.id)
        self.assertIsInstance(review.text, str)
        self.assertEqual(str(review), "[{}] ({}) \
{}".format(review.__class__.__name__, review.id, review.__dict__))
        review.save()
        self.assertNotEqual(review.created_at, review.updated_at)
        test_dict = review.to_dict()
        self.assertIsInstance(test_dict, dict)
        self.assertEqual(test_dict, review.to_dict())


if __name__ == '__main__':
    unittest.main()
