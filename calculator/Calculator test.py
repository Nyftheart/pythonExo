import unittest

from main import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        result = self.calculator.add(1, 2)
        self.assertEqual(result, 3)

    def test_subtract(self):
        result = self.calculator.subtract(2, 1)
        self.assertEqual(result, 1)

    def test_multiply(self):
        result = self.calculator.multiply(2, 3)
        self.assertEqual(result, 6)

    def test_divide(self):
        result = self.calculator.divide(6, 3)
        self.assertEqual(result, 2)

    def test_power(self):
        result = self.calculator.power(2, 3)
        self.assertEqual(result, 8)

    def test_square_root(self):
        result = self.calculator.square_root(1)
        self.assertAlmostEqual(result, 1)

    def test_calculate(self):
        result = self.calculator.calculate("add", 1, 2)
        self.assertEqual(result, 3)
        result = self.calculator.calculate("subtract", 2, 1)
        self.assertEqual(result, 1)
        result = self.calculator.calculate("multiply", 2, 3)
        self.assertEqual(result, 6)
        result = self.calculator.calculate("divide", 6, 3)
        self.assertEqual(result, 2)
        result = self.calculator.calculate("power", 2, 3)
        self.assertEqual(result, 8)
        result = self.calculator.calculate("square_root", 1, 0)
        self.assertEqual(result, 1, 0)

if __name__ == '__main__':
    unittest.main()
