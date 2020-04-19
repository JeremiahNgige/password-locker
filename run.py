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


def display_credentials():
    """
    fuction that returns all saved credentials
    """
    return Credentials.display_credentials()


def main():
    while True:
        print("Welcome to Password Locker.")
        print('\n')
        print("Use these short codes to select an option: To create New User - cu, To login your account - lg, To exit - ex")
        short_code = input().lower()
        print('\n')

        if short_code == 'cu':
            print("Create a UserName")
            created_user_name = input()

            print("Select a Password")
            created_password = input()

            print("Confirm Your Password")
            confirm_password = input()

            while confirm_password != created_password:
                print("Sorry, your password did not match!")
                print("Enter a password")
                created_password = input()
                print("Confirm your Password")
                confirm_password = input()
            else:
                print(
                    f"Congratulations {created_user_name}! You have created your new account.")
                print('\n')
                print("Proceed to Log In to your Account")
                print("Username")
                entered_userName = input()
                print("Your Password")
                entered_password = input()

                while entered_userName != created_user_name or entered_password != created_password:
                    print("You entered a wrong username or password")
                    print("Username")
                    entered_userName = input()
                    print("Your Password")
                    entered_password = input()
                else:
                    print(f"Welcome: {entered_userName} to your Account")
                    print('\n')

                    print("Select an option below to continue: Enter 1, 2, 3, 4 or 5")
                    print('\n')

                while True:
                    print("1: View Your saved credentials")
                    print("2: Add new credentials")
                    print("3: Remove credentials")
                    print("4: Search credentials")
                    print("5: Log Out")
                    option = input()
