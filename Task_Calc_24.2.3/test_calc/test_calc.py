import pytest

from app.calculator import Calculator

class TestCalculator:
    def setup(self):
        self.calculator = Calculator

    def test_multiply(self):
        assert self.calculator.multiply(self, 1, 1) == 1

    def test_division(self):
        assert self.calculator.division(self, 1, 1) == 1

    def test_subtraction(self):
        assert self.calculator.subtraction(self, 1, 1) == 0

    def test_adding(self):
        assert self.calculator.adding(self, 1, 1) == 2