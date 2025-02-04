import sys
import os
import unittest
import unittest
import json
# Add the parent directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
#import the module I want to test
import StravaStream.GetActivities as GetActivities

#get my env variables
activities_url = os.getenv('activities_url')
last_fetched_file = os.getenv('last_fetched_file')


#we're creating a test class that inherits from unittest.TestCase
class TestClass(unittest.TestCase):
    def test_get_access_token(self):
        # Test the function to retrieve the access token
       self.assertIsNotNone(GetActivities.get_access_token(), "Access token not found")
    
   
    def test_get_last_fetched_datetime(self):
        # Test the function to retrieve the last fetched datetime
       self.assertIsNotNone(GetActivities.get_last_fetched_datetime(), "No date file found")

    def test_get_last_fetched_datetime_exists(self):
        # Create a mock last fetched file with a known timestamp
        mock_data = {'last_fetched_epoch': 1609459200}  # Example epoch timestamp
        with open(last_fetched_file, 'w') as f:
            json.dump(mock_data, f)
        
        # Test the function to retrieve the last fetched datetime
        result = GetActivities.get_last_fetched_datetime()
        self.assertEqual(result, 1609459200, "The retrieved timestamp does not match the expected value")
    
    def test_save_last_fetched_datetime(self):
        # Test saving a known timestamp
        test_timestamp = "2021-01-01T00:00:00Z"
        expected_epoch = 1609459200  # Corresponding epoch time for the test timestamp

        # Call the function to save the timestamp
        result = GetActivities.save_last_fetched_datetime(test_timestamp)

        # Verify the saved data
        self.assertEqual(result['last_fetched_datetime'], test_timestamp, f"The saved datetime {result['last_fetched_datetime']} does not match the expected value {test_timestamp}")
        self.assertEqual(result['last_fetched_epoch'], expected_epoch, f"The saved epoch time {result['last_fetched_epoch']} does not match the expected value {expected_epoch}")

        # Verify the file content
        with open(last_fetched_file, 'r') as f:
            data = json.load(f)
            self.assertEqual(data['last_fetched_datetime'], test_timestamp, "The file datetime does not match the expected value")
            self.assertEqual(data['last_fetched_epoch'], expected_epoch, "The file epoch time does not match the expected value")
    

#If the script is run directly, the following code will execute the tests
if __name__ == '__main__':
    unittest.main()