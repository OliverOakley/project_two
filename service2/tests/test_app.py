from flask import url_for
from flask_testing import TestCase
from app import app

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///",
            SECRET_KEY='TEST_SECRET_KEY',
            DEBUG=True,
            WTF_CSRF_ENABLED=False
            )
        return app

class TestService2(TestBase):
    def test_service_2(self):
        response = self.client.get(url_for('service2'), follow_redirects =True)
        self.assertEqual(response.status_code, 200)