import unittest
from .index import Challenge


class TestStringMethods(unittest.TestCase):

    def test_small_1(self):
        f = open("./challenges/10/smallinput.txt", "r")
        chal = Challenge(f.read())
        self.assertEqual(chal.star1(), 220)

    def test_small_2(self):
        f = open("./challenges/10/smallinput.txt", "r")
        chal = Challenge(f.read())
        self.assertEqual(chal.star2(), 19208)


    def test_1(self):
        f = open("./challenges/10/input.txt", "r")
        chal = Challenge(f.read())
        self.assertEqual(chal.star1(), 1876)

    def test_2(self):
        f = open("./challenges/10/input.txt", "r")
        chal = Challenge(f.read())
        self.assertEqual(chal.star2(), 14173478093824)

if __name__ == '__main__':
    unittest.main()
