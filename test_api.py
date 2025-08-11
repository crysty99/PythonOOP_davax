import unittest

from app import app, db


class MathApiTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_pow(self):
        response = self.app.post('/api/pow', json={'base': 2, 'exp': 3})
        print("[test_pow] status:", response.status_code)
        data = response.get_json()
        print("[test_pow] response:", data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['result'], '8')
        self.assertEqual(data['operation'], 'pow')

    def test_fibonacci(self):
        response = self.app.post('/api/fibonacci', json={'n': 7})
        print("[test_fibonacci] status:", response.status_code)
        data = response.get_json()
        print("[test_fibonacci] response:", data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['result'], '13')
        self.assertEqual(data['operation'], 'fibonacci')

    def test_factorial(self):
        response = self.app.post('/api/factorial', json={'n': 5})
        print("[test_factorial] status:", response.status_code)
        data = response.get_json()
        print("[test_factorial] response:", data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['result'], '120')
        self.assertEqual(data['operation'], 'factorial')

    def test_history(self):
        self.app.post('/api/pow', json={'base': 2, 'exp': 2})
        self.app.post('/api/fibonacci', json={'n': 5})
        response = self.app.get('/api/history')
        print("[test_history] status:", response.status_code)
        data = response.get_json()
        print("[test_history] response:", data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(isinstance(data, list))
        self.assertGreaterEqual(len(data), 2)


if __name__ == '__main__':
    unittest.main()
