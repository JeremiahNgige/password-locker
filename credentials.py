class Credentials:
    """
    create class for user credentials
    """

    def __init__(self, account_name, account_username, account_password):
        self.account_name = account_name
        self.account_username = account_username
        self.account_password = account_password

    credentials_list = []

    def save_credentials(self):
        """
        method that saves credentials' object in credentials' list
        """
        self.credentials_list.append(self)


if __name__ == "__main__":
    main()
