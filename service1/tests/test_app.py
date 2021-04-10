from flask import url_for
from flask_testing import TestCase
from application import db
from application.models import Prizes
from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestPrizeGenerator(TestBase):
    def test_prize_generator(self):
        response = self.client.get(url_for('home'), follow_redirects =True)
        self.assertEqual(response.status_code, 200)