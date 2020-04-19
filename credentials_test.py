import unittest
from credentials import Credentials


class TestCredentials(unittest.TestCase):
    """
    tests cases for credentials' class behaviours
    """

    def setUp(self):
        self.new_credentials = Credentials(
            "Account", "AccountUserName", "Allow1234")  # create credentials object

    def test_init(self):
        """
        tests if credentials object is proprely initialized
        """
        self.assertEqual(self.new_credentials.account_name, "Account")
        self.assertEqual(
            self.new_credentials.account_username, "AccountUserName")
        self.assertEqual(self.new_credentials.account_password, "Allow1234")


if __name__ == "__main__":
    unittest.main()
