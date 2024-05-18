import unittest
from dummy_project import sum
from fractions import Fraction

class testSum(unittest.TestCase):
    def test_sum_list(self):
        """
        testing the dummy sum function
        """

        sum_list = sum([1, 2, 3])
        self.assertEqual(sum_list, 6)

    def test_list_fraction(self):
        """
        Test that it can sum a list of fractions
        """
        data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]
        result = sum(data)
        self.assertEqual(result, 1)

if __name__ == "__main__":
    unittest.main()

