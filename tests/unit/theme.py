'''
Created on Sep 11, 2015

@author: hugosenari
'''
import unittest
from simplui.theme import BaseTheme

class MyImage(object):
    def get_region(self, *args):
        pass

class TestTheme(unittest.TestCase):

    def test_assert_set_image(self):
        target = BaseTheme({"image": "NOT IMAGE"}, "IMAGE")
        assert 'image' in target
        assert target["image"] == "IMAGE"

    def test_assert_set_field(self):
        target = BaseTheme({"eggs": "spam"}, None)
        assert 'eggs' in target
        assert target["eggs"] == "spam"

    def test_assert_set_dict(self):
        target = BaseTheme({"eggs": {"spam": "bacon"}}, None)
        assert 'eggs' in target
        assert 'spam' in target["eggs"]
        assert target["eggs"]["spam"] == "bacon"
        
    def _test_assert_set_ninepatch(self):
        target = BaseTheme(
            {"eggs": {"image_spam": [27, 25, 43, 25]}},
            MyImage()
        )
        assert 'eggs' in target
        assert 'image_spam' in target["eggs"]
        assert target["eggs"]["spam"] == "bacon"

if __name__ == "__main__":
    unittest.main()