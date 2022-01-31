from django.test import SimpleTestCase


class SimpleTests(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_about_page_status_code(self):
        response = self.client.get('/admin/')
        self.assertEqual(response.status_code, 200)

    def test_about_page_status_code(self):
        response = self.client.get('/news/')
        self.assertEqual(response.status_code, 200)

    def test_about_page_status_code(self):
        response = self.client.get('/projects/')
        self.assertEqual(response.status_code, 200)        

    def test_about_page_status_code(self):
        response = self.client.get('/photos/')
        self.assertEqual(response.status_code, 200)

    def test_about_page_status_code(self):
        response = self.client.get('/files/')
        self.assertEqual(response.status_code, 200)  

    def test_about_page_status_code(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)

    def test_about_page_status_code(self):
        response = self.client.get('/accounts/')
        self.assertEqual(response.status_code, 200)