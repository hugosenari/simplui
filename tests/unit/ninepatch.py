'''
Created on Sep 12, 2015

@author: hugosenari
'''
import unittest
from simplui.ninepatch import PixelData

class Fake(PixelData):
    def __init__(self, data, has_alpha=True, width=1):
        self.data = data
        self.has_alpha = has_alpha
        self.width = width


class TestPixelData(unittest.TestCase):

    def test_is_alpha_and_black(self):
        target = Fake(b'\x00\x00\x00\xFF')
        actual = PixelData.is_black(target, 0, 0)
        self.assertTrue(actual, "Must be black")

    def test_is_alpha_and_not_black(self):
        target = Fake(b'\x00\x00\x00\xF0')
        actual = PixelData.is_black(target, 0, 0)
        self.assertFalse(actual, "Must not be black")

    def test_is_not_alpha_but_black(self):
        target = Fake(b'\x00\x00\x00\xFF', False)
        actual = PixelData.is_black(target, 0, 0)
        self.assertTrue(actual, "Must be black")

    def test_is_not_alpha_and_not_black(self):
        target = Fake(b'\x00\x0F\x00\xFF', False)
        actual = PixelData.is_black(target, 0, 0)
        self.assertFalse(actual, "Must not be black")


if __name__ == "__main__":
    unittest.main()