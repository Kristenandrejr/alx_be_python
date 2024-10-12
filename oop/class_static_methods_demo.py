# class_static_methods_demo.py

class Calculator:
    # This class attribute is shared by all instances of Calculator
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        Static method for adding two numbers.
        This doesn't require access to class-level data,
        so it's defined as a static method.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        Class method for multiplying two numbers.
        This method has access to the class itself via 'cls', which is useful
        for accessing or modifying class-level attributes.
        """
        # Show the type of calculation before proceeding
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
