import unittest
from .index import Challenge


class TestStringMethods(unittest.TestCase):

    def test_small_1(self):
        f = open("./challenges/8/smallinput.txt", "r")
        chal = Challenge(f.read())
        self.assertEqual(chal.star1(), 5)

    def test_small_2(self):
        f = open("./challenges/8/smallinput.txt", "r")
        chal = Challenge(f.read())
        self.assertEqual(chal.star2(), 8)

    def test_1(self):
        f = open("./challenges/8/input.txt", "r")
        chal = Challenge(f.read())
        self.assertEqual(chal.star1(), 1553)

    def test_2(self):
        f = open("./challenges/8/input.txt", "r")
        chal = Challenge(f.read())
        self.assertEqual(chal.star2(), 1877)


if __name__ == '__main__':
    unittest.main()
