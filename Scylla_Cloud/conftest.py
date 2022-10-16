import pytest
import random
import string
import datetime
from Scylla_Cloud.browser import Browser

class User:
    def __init__(self, email, password):
        self.email = email
        self._password = password

@pytest.fixture()
def browser():
    return Browser()

@pytest.fixture()
def user_test():
    return User(email="lenochkar35+1@mail.ru", password="lenochkar35+1")




