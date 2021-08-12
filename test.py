import unittest
from vector import Vector


class TestVectors(unittest.TestCase):
    def setUp(self):
        self.v1 = Vector(1.0, -2.0, -2.0)
        self.v2 = Vector(3.0, 6.0, 9.0)

    def test_magnitude(self):
        self.assertEqual(self.v1.magnitude(), 3.0)

    def test_normalize(self):
        self.assertEqual(self.v1.normalize(), self.v1 / self.v1.magnitude())

    def test_addition(self):
        sum = self.v1 + self.v2
        self.assertEqual(getattr(sum, "x"), 4.0)

    def test_subtraction(self):
        diff = self.v2 - self.v1
        self.assertEqual(getattr(diff, "x"),2.0)

    def test_multiplication(self):
        product = self.v1 * 2
        product2 = 3 * self.v2
        self.assertEqual(getattr(product,"x"), 2.0)
        self.assertEqual(getattr(product2, "x"), 9.0)

    def test_division(self):
        result = self.v2 / 2
        self.assertEqual(getattr(result,"x"), 1.5)

    def test_equal(self):
        self.assertEqual(self.v1 == self.v1, True)


if __name__ == '__main__':
    unittest.main()
