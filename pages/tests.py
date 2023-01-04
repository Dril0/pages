from django.test import (
    SimpleTestCase,
)  # simple porque no vamos a usar por ahora una base de datos.

# Create your tests here.

"""Test para que las url retornen un http status code 200."""


class HomepageTests(SimpleTestCase):
    def test_url_exist_at_corrent_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)


class AboutpageTests(SimpleTestCase):
    def test_url_exist_at_corrent_location(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)
