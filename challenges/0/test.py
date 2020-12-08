import unittest
from .index import Challenge


class TestStringMethods(unittest.TestCase):

    def test_small_1(self):
        f = open("./challenges/0/smallinput.txt", "r")
        chal = Challenge(f.read())
        self.assertEqual(chal.star1(), 'Fill in with small input!')

    def test_small_2(self):
        f = open("./challenges/0/smallinput.txt", "r")
        chal = Challenge(f.read())
        self.assertEqual(chal.star2(), 'Fill in with small input!')


if __name__ == '__main__':
    unittest.main()
