import unittest
from .index import Challenge


class TestStringMethods(unittest.TestCase):

    def test_small_1(self):
        f = open("./challenges/9/smallinput.txt", "r")
        chal = Challenge(f.read(), 5)
        self.assertEqual(chal.star1(), 127)

    def test_small_2(self):
        f = open("./challenges/9/smallinput.txt", "r")
        chal = Challenge(f.read(), 5)
        self.assertEqual(chal.star2(), 62)

    def test_1(self):
        f = open("./challenges/9/input.txt", "r")
        chal = Challenge(f.read(), 25)
        self.assertEqual(chal.star1(), 18272118)

    def test_2(self):
        f = open("./challenges/9/input.txt", "r")
        chal = Challenge(f.read(), 25)
        self.assertEqual(chal.star2(), 2186361)


if __name__ == '__main__':
    unittest.main()
