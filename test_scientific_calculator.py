"""
Unit tests for the calculator library
"""
import scientific_calculator


class TestCalculator:

    def test_sqrt(self):
        assert 14 == scientific_calculator.square_root(196)

    def test_factorial(self):
        assert 5040 == scientific_calculator.factorial(7)

    def test_natural_log(self):
        assert 2.995732273553991 == scientific_calculator.natural_log(20)

    def test_power(self):
        assert 512 == scientific_calculator.power(2, 9)
