import unittest
import random
from main import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator(1)

    def test_add(self):
        calc_value = self.calculator.value
        self.assertEqual(self.calculator.add(1, 2, 3).value, calc_value + 6)

    def test_mul(self):
        calc_value = self.calculator.value
        self.assertEqual(self.calculator.multiply(5, 2, 90).value, calc_value * 900)

    def test_divide(self):
        calc_value = self.calculator.value
        self.assertEqual(self.calculator.divide(2, 3).value, calc_value / 6)

    def kek(self):
        self.assertEqual(1, 2)

    def test_power(self):
        calc_value = self.calculator.value
        self.assertEqual(self.calculator.power(2, 3).value, calc_value ** 6)

    def test_root(self):
        calc_value = self.calculator.value
        self.assertEqual(self.calculator.root(2, 3).value, calc_value ** (1./6))

    def test_power_add_mul(self):
        calc_value = self.calculator.value
        self.assertAlmostEqual(self.calculator.power(2, 5).add(12, 18).multiply(5, 6).value, (calc_value ** 10 + 30) * 30)

    def test_add_mul(self):
        self.calculator = Calculator(random.random() * 20)
        calc_value = self.calculator.value
        self.assertAlmostEqual(self.calculator.add(12, 17).multiply(11, 12).value, (calc_value + 29) * 132)

    def test_xor(self):
        calc_value = self.calculator.value
        self.assertEqual(self.calculator.xor(3, 4).value, calc_value ^ 7)

    def test_xor2(self):
        calc_value = self.calculator.value
        self.assertEqual(self.calculator.xor(3, 3).value, calc_value ^ 0)


if __name__ == '__main__':
    unittest.main()