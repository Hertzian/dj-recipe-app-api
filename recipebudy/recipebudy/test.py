from django.test import TestCase

from recipebudy.calc import add


class CalcTest(TestCase):
    def test_ad_numbers(self):
        """Test that two numbers are added together"""
        self.assertEqual(add(3, 8), 11)
