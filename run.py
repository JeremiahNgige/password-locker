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

