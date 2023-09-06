import unittest
from Scripts.Services.Calculation import calc


# class MyTestCase(unittest.TestCase):
#     def test_something(self):
#         self.assertEqual(True, False)  # add assertion here


class TestCalculation(unittest.TestCase):

    def test_add(self):
        calc_obj = calc.AlgebraicCalculation()

        self.assertEqual(calc_obj.add(10, 5), 15)
        self.assertEqual(calc_obj.add(-1, 1), 0)
        self.assertEqual(calc_obj.add(-1, -1), -2)

    def test_subtract(self):
        calc_obj = calc.AlgebraicCalculation()

        self.assertEqual(calc_obj.subtract(10, 5), 5)
        self.assertEqual(calc_obj.subtract(-1, 1), -2)
        self.assertEqual(calc_obj.subtract(-1, -1), 0)

    def test_multiply(self):
        calc_obj = calc.AlgebraicCalculation()

        self.assertEqual(calc_obj.multiply(10, 5), 50)
        self.assertEqual(calc_obj.multiply(-1, 1), -1)
        self.assertEqual(calc_obj.multiply(-1, -1), 1)

    def test_divide(self):
        calc_obj = calc.AlgebraicCalculation()

        self.assertEqual(calc_obj.divide(10, 5), 2)
        self.assertEqual(calc_obj.divide(-1, 1), -1)
        self.assertEqual(calc_obj.divide(-1, -1), 1)
        self.assertEqual(calc_obj.divide(5, 2), 2.5)

        with self.assertRaises(ValueError):
            calc_obj.divide(10, 0)


if __name__ == '__main__':
    unittest.main()

    # test_cases = [
    #     {'operation': 'add', 'x': 20, 'y': 40, 'output': 60},
    #     {'operation': 'multiply', 'x': 20, 'y': 4, 'output': 80},
    #     {'operation': 'subtract', 'x': 20, 'y': 40, 'output': -20},
    #     {'operation': 'divide', 'x': 200, 'y': 40, 'output': 5},
    #     {'operation': 'add', 'x': 20, 'y': 50, 'output': 70},
    #     {'operation': 'subtract', 'x': 100, 'y': 40, 'output': 60},
    #     {'operation': 'divide', 'x': 20, 'y': 0, 'output': None}
    # ]

