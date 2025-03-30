import unittest
import logging
from ABConnect import ABConnectAPI

logging.basicConfig(level=logging.DEBUG)

class TestABConnectAPI(unittest.TestCase):
    def setUp(self) -> None:
        self.abc = ABConnectAPI()
    
    def test_users_me(self):
        response = self.abc.users.me()
        self.assertTrue(response.ok)
        try:
            data = response.json()
            print("User Info:", data)
        except Exception:
            data = response.text
            print("Response Text:", data)

        self.assertTrue(data, "Expected response data, but got nothing.")

if __name__ == '__main__':
    unittest.main()