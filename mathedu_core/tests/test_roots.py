import unittest

from mathedu_core.roots import (
    bisection_method,
    has_root_between,
    newton_raphson_method,
    successive_approximation,
)

POLY = lambda x: x ** 3 - 4 * x - 8.95  # root near 2.7038
TRUE_ROOT = 2.7038035


class BisectionTests(unittest.TestCase):
    def test_returns_dict(self):
        result = bisection_method(POLY, 2, 4, 1e-4)
        self.assertIsInstance(result, dict)
        self.assertAlmostEqual(float(result["result"]), TRUE_ROOT, places=2)

    def test_iteration_lists(self):
        result = bisection_method(POLY, 2, 4, 1e-4)
        self.assertEqual(len(result["a"]), len(result["b"]))
        self.assertEqual(len(result["b_c"]), len(result["func"]))
        self.assertEqual(len(result["other_results"]), len(result["a"]))


class NewtonRaphsonTests(unittest.TestCase):
    def test_converges(self):
        result = newton_raphson_method(POLY, 3)
        self.assertAlmostEqual(float(result["result"]), TRUE_ROOT, places=2)

    def test_reports_non_convergence(self):
        result = newton_raphson_method(POLY, 3, tolerance=1e-30, max_iterations=2)
        self.assertIn("did not converge", result["result"])


class SuccessiveApproximationTests(unittest.TestCase):
    def test_converges(self):
        result = successive_approximation(POLY, 2, 4, 1e-4, 1000)
        self.assertAlmostEqual(float(result["result"]), TRUE_ROOT, places=2)

    def test_reports_max_iterations(self):
        result = successive_approximation(POLY, 2, 4, 1e-30, 3)
        self.assertIn("maximum iterations", result["result"])


class SignChangeTests(unittest.TestCase):
    def test_root_bracketed(self):
        self.assertTrue(has_root_between(POLY, 2, 4))

    def test_root_not_bracketed(self):
        self.assertFalse(has_root_between(POLY, 0, 1))


if __name__ == "__main__":
    unittest.main()