'''
Created on Sep 11, 2015

@author: hugosenari
'''
import unittest
from simplui.theme import BaseTheme

class TestTheme(unittest.TestCase):

    def test_if_seting_with_empty_dict(self):
        target = BaseTheme({}, "IMAGE")
        assert 'image' in target
        assert target["image"] == "IMAGE"

if __name__ == "__main__":
    unittest.main()