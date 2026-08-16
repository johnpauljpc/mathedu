from django.test import SimpleTestCase
from django.urls import reverse


class RootFindingTests(SimpleTestCase):
    def test_page_loads(self):
        response = self.client.get(reverse("trans_eqn"))
        self.assertEqual(response.status_code, 200)

    def test_bisection(self):
        response = self.client.post(
            reverse("trans_eqn"),
            {
                "interval1": 2,
                "interval2": 4,
                "equation": "x^3 - 4x - 8.95",
                "tolerance": 0.0001,
                "root_method": "bisection",
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "2.703")

    def test_newton_raphson(self):
        response = self.client.post(
            reverse("trans_eqn"),
            {
                "interval1": 2,
                "interval2": 4,
                "equation": "x^3 - 4x - 8.95",
                "tolerance": 0.0001,
                "root_method": "newton_raphson",
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "2.703")

    def test_successive_approximation(self):
        response = self.client.post(
            reverse("trans_eqn"),
            {
                "interval1": 2,
                "interval2": 4,
                "equation": "x^3 - 4x - 8.95",
                "tolerance": 0.0001,
                "root_method": "successive_approximation",
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "2.703")

    def test_invalid_interval_shows_error(self):
        response = self.client.post(
            reverse("trans_eqn"),
            {
                "interval1": "abc",
                "interval2": "def",
                "equation": "x",
                "tolerance": "0.001",
                "root_method": "bisection",
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "numeric")

    def test_equation_injection_is_blocked(self):
        response = self.client.post(
            reverse("trans_eqn"),
            {
                "interval1": 0,
                "interval2": 1,
                "equation": "__import__('os').system('echo PWNED')",
                "tolerance": 0.0001,
                "root_method": "bisection",
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "not a valid equation")

    def test_tan_function_works(self):
        response = self.client.post(
            reverse("trans_eqn"),
            {
                "interval1": 0,
                "interval2": 1,
                "equation": "tan(x)",
                "tolerance": 0.0001,
                "root_method": "bisection",
            },
        )
        self.assertEqual(response.status_code, 200)