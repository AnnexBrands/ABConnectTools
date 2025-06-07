import unittest
import logging
from tests.base import ABConnectTestCase

logging.basicConfig(level=logging.DEBUG)

class TestABConnectAPI(ABConnectTestCase):
    """Test ABConnect API endpoints."""
    
    def test_users_me(self):
        response = self.api.users.me()
        
        # Response should be a dictionary
        self.assertIsInstance(response, dict, "Expected dict response from users.me()")
        
        # Check that userName matches our config
        self.assertEqual(response.get('userName'), self.test_username, 
                        f"Expected userName to be '{self.test_username}'")
        
        # Print user info for debugging
        print(f"User Info: {response}")
        
        # Additional assertions to verify we got valid user data
        self.assertIn('userName', response, "Response should contain userName")
        self.assertIn('email', response, "Response should contain email")

if __name__ == '__main__':
    unittest.main()