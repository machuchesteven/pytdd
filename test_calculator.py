import unittest

from Calculator import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add_returns_sum(self):
        self.assertEqual(self.calc.add(2, 2), 4)
        self.assertEqual(self.calc.add(2, -2), 0)
        self.assertEqual(self.calc.add(-2.1, -2.1), -4.2)

    def test_add_non_numbers_raises_exception(self):
        # with self.assertRaises(TypeError):
        #     self.calc.add('two', 2)
        self.assertRaises(TypeError, self.calc.add('two', 2))
        self.assertRaises(TypeError, self.calc.add(2, '5s'))

    def test_add_string_numbers_returns_sum(self):
        self.assertEqual(self.calc.add('2', 5), 7)
        self.assertEqual(self.calc.add('2', '-2'), 0)
        self.assertEqual(self.calc.add('-2.1', '-2.1'), -4.2)
