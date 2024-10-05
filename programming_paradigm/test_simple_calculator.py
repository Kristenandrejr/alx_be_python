import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """Test suite for the SimpleCalculator class."""

    def setUp(self):
        """Create a SimpleCalculator instance for use in the tests."""
        self.calculator = SimpleCalculator()

    def test_addition(self):
        """Test the addition of two numbers."""
        self.assertEqual(self.calculator.add(2, 3), 5)  # Normal case
        self.assertEqual(self.calculator.add(-1, 1), 0)  # Edge case
        self.assertEqual(self.calculator.add(0, 0), 0)   # Edge case

    def test_subtraction(self):
        """Test the subtraction of two numbers."""
        self.assertEqual(self.calculator.subtract(10, 5), 5)  # Normal case
        self.assertEqual(self.calculator.subtract(-1, -1), 0)  # Edge case
        self.assertEqual(self.calculator.subtract(5, 10), -5)  # Normal case

    def test_multiplication(self):
        """Test the multiplication of two numbers."""
        self.assertEqual(self.calculator.multiply(3, 5), 15)  # Normal case
        self.assertEqual(self.calculator.multiply(-1, 1), -1)  # Edge case
        self.assertEqual(self.calculator.multiply(0, 10), 0)   # Edge case

    def test_division(self):
        """Test the division of two numbers."""
        self.assertEqual(self.calculator.divide(10, 2), 5)       # Normal case
        self.assertEqual(self.calculator.divide(-9, 3), -3)      # Normal case
        self.assertEqual(self.calculator.divide(10, 0), None)    # Division by zero case

if __name__ == "__main__":
    unittest.main()
