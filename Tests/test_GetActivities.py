import sys
import os
import unittest

# Add the parent directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest

from StravaStream.GetActivities import get_access_token, get_last_fetched_datetime

#we're creating a test class that inherits from unittest.TestCase
class TestClass(unittest.TestCase):
    def test_get_access_token(self):
        # Test the function to retrieve the access token
       self.assertIsNotNone(get_access_token(), "Access token not found")

    def test_get_last_fetched_datetime(self):
        # Test the function to retrieve the last fetched datetime
       self.assertIsNotNone(get_last_fetched_datetime(), "No date file found")

    # def test_save_last_fetched_datetime(self):
    #     # Test the function to retrieve the last fetched datetime
    #    self.assertIsNotNone(save_last_fetched_datetime(), "No date file found")



if __name__ == '__main__':
    unittest.main()