import unittest
from app import app  # Adjust according to your app file name

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_negative_sum(self):
        response = self.app.get('/sum?num1=-5&num2=-10')
        self.assertEqual(response.data.decode('utf-8'), '-15')  # Adjust the expected output as needed

if __name__ == '__main__':
    unittest.main()
