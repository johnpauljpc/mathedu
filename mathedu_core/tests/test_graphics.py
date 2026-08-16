import unittest

from mathedu_core.graphics import dda_line


class DDATests(unittest.TestCase):
    def test_single_point_no_crash(self):
        x, y, x_inc, y_inc = dda_line(2, 2, 2, 2)
        self.assertEqual(x, [2])
        self.assertEqual(y, [2])

    def test_line_endpoints(self):
        x, y, _, _ = dda_line(0, 0, 4, 6)
        self.assertEqual(x[0], 0)
        self.assertEqual(y[0], 0)
        self.assertEqual(x[-1], 4)
        self.assertEqual(y[-1], 6)

    def test_coordinate_lists_match_length(self):
        x, y, x_inc, y_inc = dda_line(0, 0, 10, 5)
        self.assertEqual(len(x), len(y))
        self.assertEqual(len(x_inc), len(y_inc))
        self.assertEqual(len(x_inc), len(x))


if __name__ == "__main__":
    unittest.main()