"""
Sample test
"""

from django.test import SimpleTestCase
from app.calc import add, subtract


class CalcTests(SimpleTestCase):

    def test_add_numbers(self):
        """Test adding numbers together 2"""
        res = add(5, 6)

        self.assertEqual(res, 11)

    def test_subtract_numbers(self):
        res = subtract(10, 5)

        self.assertEqual(res, 5)
