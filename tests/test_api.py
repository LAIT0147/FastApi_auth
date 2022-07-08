from unittest import TestCase
from fastapi.testclient import TestClient
from app.main import app as web_app


class APITest(TestCase):
    def setUp(self):
        self.client = TestClient(web_app)

    def test_main(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 404)

    def test_create_user(self):
        user_data = {
            'user': {
                'email': 'test102@test.com',
                'password': '123',
                'first_name': 'lol',
                'last_name': 'kek',
                'nickname': 'lolkek122'
            }
        }
        response = self.client.post('/register', json=user_data)
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        user_data = {
            'user_form': {
                'email': 'test1@test.com',
                'password': '123'
            }
        }
        response = self.client.post('/login', json=user_data)
        self.assertEqual(response.status_code, 200)

