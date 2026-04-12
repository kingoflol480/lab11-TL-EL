
from math import *
import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(0, 5), -5)
        self.assertEqual(subtract(-2, -3), 1)
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(2, 3), 6)
        self.assertEqual(mul(-4, 5), -20)
        self.assertEqual(mul(0, 100), 0)

    def test_divide(self): # 3 assertions
        self.assertAlmostEqual(div(10, 2), 5.0)
        self.assertAlmostEqual(div(7, 2), 3.5)
        self.assertAlmostEqual(div(-9, 3), -3.0)
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(5, 0)

    def test_logarithm(self): # 3 assertions
        self.assertEqual(logarithm(8, 2), 3)
        self.assertEqual(logarithm(1, 10), 0)
        self.assertEqual(logarithm(100, 10), 2)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(10, 1)
    # ##########################
    
    ######## Partner 1
        def test_log_invalid_argument(self): # 1 assertion
            with self.assertRaises(ValueError):
                logarithm(0, 5)

    def test_hypotenuse(self): # 3 assertions
        self.assertAlmostEqual(hypotenuse(3, 4), 5.0)
        self.assertAlmostEqual(hypotenuse(5, 12), 13.0)
        self.assertAlmostEqual(hypotenuse(1.5, 2.0), math.hypot(1.5, 2.0))

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-1)
        self.assertAlmostEqual(square_root(0), 0.0)
        self.assertAlmostEqual(square_root(9), 3.0)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()