from django.test import TestCase
from django.urls import reverse


class StorefrontTests(TestCase):
    def test_homepage_renders_product_catalog(self):
        response = self.client.get(reverse("my_home"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "The everyday edit")
        self.assertContains(response, "Sunday Morning Mug")
        self.assertContains(response, "KSh 1,850")
        self.assertContains(response, "Kenyan homes")
        self.assertNotContains(response, "$28.00")

    def test_homepage_includes_product_data_for_storefront(self):
        response = self.client.get(reverse("my_home"))

        self.assertEqual(len(response.context["products"]), 8)
        self.assertEqual(response.context["products"][0]["price"], 1850)
