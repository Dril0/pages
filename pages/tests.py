from django.test import (
    SimpleTestCase,
)  # simple porque no vamos a usar por ahora una base de datos.
from django.urls import reverse

# Create your tests here.


class HomepageTests(SimpleTestCase):
    def test_url_exist_at_corrent_location(
        self,
    ):  # Test para que las url retornen un http status code 200.
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(
        self,
    ):  # Test para chequear los nombres de las url. app/urls.py
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)


class AboutpageTests(SimpleTestCase):
    def test_url_exist_at_corrent_location(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)
