#!/usr/bin/env python3.6

import random
from user import User
from credentials import Credentials

# functions that add credentials


def create_new_credentials(account_name, account_username, account_password):
    """
    function to create new acc with its credentials
    """
    new_credentials = Credentials(
        account_name, account_username, account_password)
    return new_credentials


def save_new_credentials(credentials):
    """
    function to save the new credentials
    """
    credentials.save_credentials()


def locate_credentials(account_name):
    """
    function to locate credentials based on account_name
    """
    return Credentials.locate_by_name(account_name)


def credentials_existance(name):
    """
    function that checks if a a particular account and its credentials exist based on searched account_name
    """
    return Credentials.credentials_exists(name)


def delete_credentials(credentials):
    """
    function that deletes credentials
    """
    return Credentials.delete_credentials(credentials)

