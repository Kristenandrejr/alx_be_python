class SimpleCalculator:
    """A simple calculator class that supports basic arithmetic operations."""

    def add(self, a, b):
        """Return the sum of a and b."""
        return a + b

    def subtract(self, a, b):
        """Return the result of subtracting b from a."""
        return a - b

    def multiply(self, a, b):
        """Return the product of a and b."""
        return a * b

    def divide(self, a, b):
        """Return the result of dividing a by b. If b is zero, return None."""
        # Check if the denominator is zero to avoid division by zero
        if b == 0:
            return None
        return a / b
