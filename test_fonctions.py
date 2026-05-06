import unittest
from mesfonctions import *

class TestFonctions(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(addition(2,3), 5)

    def test_soustraction(self):
        self.assertEqual(soustraction(5,2), 3)

    def test_multiplication(self):
        self.assertEqual(multiplication(2,3), 6)

    def test_division(self):
        self.assertEqual(division(6,2), 3)

    def test_carre(self):
        self.assertEqual(carre(4), 16)

if __name__ == '__main__':
    unittest.main()