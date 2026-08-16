import unittest

from mathedu_core.expressions import ExpressionError, build_equation


class BuildEquationTests(unittest.TestCase):
    def test_polynomial_evaluation(self):
        f = build_equation("x^3 - 4x - 8.95")
        self.assertAlmostEqual(f(3), 27 - 12 - 8.95)

    def test_implicit_multiplication(self):
        f = build_equation("4x + 1")
        self.assertEqual(f(2), 9)

    def test_exponent_shorthand(self):
        f = build_equation("x2")
        self.assertEqual(f(2), 4)

    def test_trig_is_degrees(self):
        self.assertAlmostEqual(build_equation("tan(x)")(45), 1.0, places=6)
        self.assertAlmostEqual(build_equation("sin(x)")(30), 0.5, places=6)

    def test_compact_function_spelling(self):
        self.assertAlmostEqual(build_equation("sinx")(30), 0.5, places=6)

    def test_log_base_10(self):
        self.assertEqual(build_equation("log10(x)")(100), 2.0)

    def test_exponential(self):
        self.assertAlmostEqual(build_equation("e**x")(0), 1.0)

    def test_other_single_letters_are_x(self):
        f = build_equation("y**2")
        self.assertEqual(f(3), 9)

    def test_equation_lhs_only(self):
        f = build_equation("x + 1 = 5")
        self.assertEqual(f(2), 3)

    def test_invalid_expression_raises(self):
        for bad in ["", "()", "x +* 2"]:
            with self.assertRaises(ExpressionError):
                build_equation(bad)

    def test_code_execution_is_blocked(self):
        for attack in [
            "os.system('id')",
            "__import__('os')",
            "__import__('os').system('id')",
            "eval('1')",
            "x; __import__('os').system('ls')",
        ]:
            with self.assertRaises(ExpressionError):
                build_equation(attack)


if __name__ == "__main__":
    unittest.main()