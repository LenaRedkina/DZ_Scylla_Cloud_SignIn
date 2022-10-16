import string
from Scylla_Cloud import conftest
import pytest
from pages.signIn import SignIn
from browser import Browser
import time
from selenium import webdriver

class TestSignInPage:

    def test_signin(self, browser, user_test):
        browser.go_to_site(SignIn.path)
        browser.driver.implicitly_wait(5)
        page = signin(User=user_test)
        print(page.email.get_text())
        time.sleep(2)
