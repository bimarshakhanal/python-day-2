'''
Implement a program that reads user input for a password. Create a custom exception
WeakPasswordError to handle cases where the password is shorter than 8 characters.
'''

import logging

logging.basicConfig(filename='example.log',
                    encoding='utf-8', level=logging.DEBUG)


class WeakPasswordError(Exception):
    '''Custom error for weak password check.'''

    def __init__(self):
        self.message = "Weak password: Password must be of 8 or more characters."

    def __str__(self):
        return self.message


def check_password(password):
    '''Function to validate length of passeord.'''
    if len(password) < 8:
        raise WeakPasswordError()


if __name__ == '__main__':
    # take user input
    password = input("Enter password: ")
    try:
        check_password(password)
        logging.info('Password Validation completed.')
    except WeakPasswordError as e:
        logging.error(e)
