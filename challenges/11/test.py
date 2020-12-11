import unittest
from .index import Challenge
import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

smallinput = open(os.path.join(__location__, 'smallinput.txt')).read()
input = open(os.path.join(__location__, 'input.txt')).read()

class TestStringMethods(unittest.TestCase):

    def test_small_1(self):
        chal = Challenge(smallinput)
        self.assertEqual(chal.star1(), 37)

    def test_small_2(self):
        chal = Challenge(smallinput)
        self.assertEqual(chal.star2(), 26)


    def test_1(self):
        chal = Challenge(input)
        self.assertEqual(chal.star1(), 2412)

    def test_2(self):
        chal = Challenge(input)
        self.assertEqual(chal.star2(), 2176)


if __name__ == '__main__':
    unittest.main()
