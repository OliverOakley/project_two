from flask import url_for
from flask_testing import TestCase
from app import app
import requests
from mock import patch

class TestBase(TestCase):
    def create_app(self):
        return app

class TestGetRequests(TestBase):
    def test_get_requests(self):
        with patch('requests.get') as test:
            response = self.client.get(url_for('service4'))
            test.return_value.text = "test"
            self.assertIn:(b'test', response.data)

class TestService4(TestBase):
    def test_service_4(self):
        response = self.client.get(url_for('service4'), follow_redirects =True)
        self.assertEqual(response.status_code, 500)