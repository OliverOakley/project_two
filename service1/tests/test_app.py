from flask import url_for
from flask_testing import TestCase
from application import db
from application.models import Prizes
from app import app
import requests
from mock import patch

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///",
            SECRET_KEY='TEST_SECRET_KEY',
            DEBUG=True,
            WTF_CSRF_ENABLED=False
            )
        return app
    def setUp(self):
        db.create_all()
        test_prizes = Prizes(diceroll="20", fruit = "melon", amount = "120")
        db.session.add(test_prizes)
        db.session.commit()
    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestGetRequests(TestBase):
    def test_get_requests(self):
        with patch('requests.get') as test:
            response = self.client.get(url_for('prizegenerator'))
            test.return_value.text = "test"
            self.assertIn:(b'test', response.data)

class TestService1(TestBase):
    def test_service_2(self):
        response = self.client.get(url_for('home'), follow_redirects =True)
        self.assertEqual(response.status_code, 200)

class TestService1(TestBase):
    def test_service_2(self):
        response = self.client.get(url_for('prizegenerator'), follow_redirects =True)
        self.assertEqual(response.status_code, 500)