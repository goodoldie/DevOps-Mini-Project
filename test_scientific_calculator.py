"""
Unit tests for the calculator library
"""
import scientific_calculator

class TestCalculator:


    def test_sqrt(self):
        assert 14 == scientific_calculator.square_root(196)


    def test_factorial(self):
        assert 5040 == scientific_calculator.factorial(7)
