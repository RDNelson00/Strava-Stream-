import unittest

from GetActivities import get_access_token, get_last_fetched_datetime, save_last_fetched_datetime

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