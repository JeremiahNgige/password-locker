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

    def test_save_credentials(self):
        """
        tests if credentials is saved in credentials' list
        """
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list), 1)

    def test_save_multiple_credentials(self):
        """
        tests if i can save multiple credentials in credentials' list
        """
        self.new_credentials.save_credentials()
        test_credentials = Credentials(
            "TestAccount", "TestAccountName", "TestAccountPassword")  # new cred
        test_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list), 2)


if __name__ == "__main__":
    unittest.main()
