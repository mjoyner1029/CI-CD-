# app_test.py

import unittest
from app import app, calculate_sum

class AppTestCase(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.app = app.test_client()
        cls.app.testing = True

    def test_negative_sum(self):
        result = calculate_sum(-5, -10)
        self.assertEqual(result, -15, "The sum of -5 and -10 should be -15")

    # Add other tests as needed...

if __name__ == '__main__':
    unittest.main()
