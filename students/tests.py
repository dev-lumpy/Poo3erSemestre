from django.test import TestCase

# Create your tests here.
class UrlTests(TestCase):

    def test_test_api_route(self):
        response = self.client.get("/students/test/")
        self.assertEqual(response.status_code, 200)