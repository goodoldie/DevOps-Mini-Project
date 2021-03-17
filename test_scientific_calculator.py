"""
Unit tests for the calculator library
"""
import scientific_calculator


class TestCalculator:

    def test_sqrt(self):
        assert 14.0 == scientific_calculator.square_root(196)
        assert -14.0 == scientific_calculator.square_root(-14)
        assert 1.0 == scientific_calculator.square_root(1)
        assert 2.23606797749979 == scientific_calculator.square_root(5)
        assert 0.0 == scientific_calculator.square_root(0)

    def test_factorial(self):
        assert 5040 == scientific_calculator.factorial(7)
        assert 0.0 == scientific_calculator.factorial(-22)
        assert 1 == scientific_calculator.factorial(0)
        assert 4 == scientific_calculator.factorial(3.89)
        assert 1 == scientific_calculator.factorial(1)

    def test_natural_log(self):
        assert 2.995732273553991 == scientific_calculator.natural_log(20)
        assert 0 == scientific_calculator.natural_log(0)
        assert 0 == scientific_calculator.natural_log(-23)

    def test_power(self):
        assert 512 == scientific_calculator.power(2, 9)
        assert 0 == scientific_calculator.power(0, 43)
        assert 1 == scientific_calculator.power(140, 0)
        assert 0.125 == scientific_calculator.power(2, -3)
        assert 16 == scientific_calculator.power(-2, 4)
        assert 1 == scientific_calculator.power(1, 22.4)
