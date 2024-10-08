import unittest
import json
from app import app  # Import your Flask app from the main app file

class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        # Set up the test client
        self.app = app.test_client()
        self.app.testing = True

   

    def test_predict_api(self):
        # Test the predict_api route with JSON data
        test_data = {
            "N": 90, 
            "P": 42, 
            "K": 43, 
            "temperature": 20.87974371, 
            "humidity": 82.00274423, 
            "ph": 6.502985292000001, 
            "rainfall": 202.9355362
        }

        # Send POST request to the API
        response = self.app.post('/predict_api', 
            data=json.dumps({"data": test_data}),
            content_type='application/json'
        )

        # Check if the status code is OK (200)
        self.assertEqual(response.status_code, 200)
        
        # Check if the response contains the correct crop (output should be tested based on your model)
        self.assertIn(b'rice', response.data)  # Change "rice" to expected prediction

    def test_predict(self):
        # Test the predict route with form data
        test_data = {
            "N": "90", 
            "P": "42", 
            "K": "43", 
            "temperature": "20.87974371", 
            "humidity": "82.00274423", 
            "ph": "6.502985292000001", 
            "rainfall": "202.9355362"
        }

        # Send POST request to the predict form
        response = self.app.post('/predict', 
            data=test_data
        )

        # Check if the status code is OK (200)
        self.assertEqual(response.status_code, 200)

        # Check if the response contains the correct crop (again, based on the output from your model)
        self.assertIn(b'rice', response.data)  # Adjust based on actual prediction

if __name__ == "__main__":
    unittest.main()
