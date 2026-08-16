import unittest

from mathedu_core.algebra import solve_quadratic


class QuadraticTests(unittest.TestCase):
    def test_two_real_roots(self):
        root1, root2, msg = solve_quadratic(1, -3, 2)
        self.assertEqual(sorted([root1, root2]), [1, 2])
        self.assertIsNone(msg)

    def test_equal_roots(self):
        root1, root2, msg = solve_quadratic(1, -2, 1)
        self.assertEqual(root1, root2)
        self.assertEqual(root1, 1)
        self.assertIsNotNone(msg)

    def test_imaginary_roots_raise(self):
        with self.assertRaises(ValueError):
            solve_quadratic(1, 2, 2)

    def test_float_coefficients(self):
        root1, root2, _ = solve_quadratic(0.5, -1.0, -1.5)
        self.assertEqual(sorted([root1, root2]), [-1.0, 3.0])


if __name__ == "__main__":
    unittest.main()