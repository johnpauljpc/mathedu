import unittest

from mathedu_core.finance import compound_interest, simple_interest


class FinanceTests(unittest.TestCase):
    def test_simple_interest(self):
        self.assertEqual(simple_interest(1000, 5, 2), 100.0)

    def test_simple_interest_rounds(self):
        self.assertEqual(simple_interest(1000, 5, 1), 50.0)

    def test_compound_interest(self):
        ci, amount = compound_interest(1000, 5, 2)
        self.assertAlmostEqual(amount, 1102.5)
        self.assertAlmostEqual(ci, 102.5)


if __name__ == "__main__":
    unittest.main()