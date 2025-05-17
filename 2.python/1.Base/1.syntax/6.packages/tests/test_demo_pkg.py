
import unittest
from demo_pkg import add, subtract, to_upper, to_lower

class TestDemoPkg(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)

    def test_to_upper(self):
        self.assertEqual(to_upper("hello"), "HELLO")

    def test_to_lower(self):
        self.assertEqual(to_lower("WORLD"), "world")

if __name__ == '__main__':
    unittest.main()

