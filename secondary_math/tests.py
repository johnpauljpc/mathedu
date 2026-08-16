from django.test import SimpleTestCase
from django.urls import reverse


class PageTests(SimpleTestCase):
    def test_home_page(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)

    def test_simple_interest_calculation(self):
        response = self.client.post(
            reverse("simple_interest"),
            {"principal": 1000, "rate": 5, "time": 2},
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "100.0")

    def test_compound_interest_calculation(self):
        response = self.client.post(
            reverse("compound_interest"),
            {"principal": 1000, "rate": 5, "time": 2},
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "102.5")

    def test_quadratic_roots(self):
        response = self.client.post(reverse("quadratic"), {"a": 1, "b": -3, "c": 2})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "1.0")
        self.assertContains(response, "2.0")

    def test_quadratic_invalid_input_does_not_crash(self):
        response = self.client.post(reverse("quadratic"), {"a": "abc", "b": 1, "c": 1})
        self.assertEqual(response.status_code, 200)

    def test_dda_page(self):
        response = self.client.get(reverse("dda"))
        self.assertEqual(response.status_code, 200)