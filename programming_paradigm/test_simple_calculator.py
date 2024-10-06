import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5, "Expected 2 + 3 to equal 5")
        self.assertEqual(self.calc.add(-1, 1), 0, "Expected -1 + 1 to equal 0")
        self.assertEqual(self.calc.add(0, 0), 0, "Expected 0 + 0 to equal 0")

    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(5, 3), 2, "Expected 5 - 3 to equal 2")
        self.assertEqual(self.calc.subtract(3, 5), -2, "Expected 3 - 5 to equal -2")
        self.assertEqual(self.calc.subtract(0, 0), 0, "Expected 0 - 0 to equal 0")

    def test_multiply(self):
        """Test the multiplication method."""
        self.assertEqual(self.calc.multiply(3, 5), 15, "Expected 3 * 5 to equal 15")
        self.assertEqual(self.calc.multiply(-1, 1), -1, "Expected -1 * 1 to equal -1")
        self.assertEqual(self.calc.multiply(0, 5), 0, "Expected 0 * 5 to equal 0")

    def test_divide(self):
        """Test the division method."""
        self.assertEqual(self.calc.divide(10, 2), 5, "Expected 10 / 2 to equal 5")
        self.assertEqual(self.calc.divide(5, 0), None, "Expected division by zero to return None")
        self.assertEqual(self.calc.divide(0, 5), 0, "Expected 0 / 5 to equal 0")

if __name__ == "__main__":
    unittest.main()
