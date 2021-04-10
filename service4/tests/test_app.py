from flask import url_for
from flask_testing import TestCase
from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestService4(TestBase):
    def test_service_4(self):
        response = self.client.get(url_for('service4'), follow_redirects =True)
        self.assertEqual(response.status_code, 200)