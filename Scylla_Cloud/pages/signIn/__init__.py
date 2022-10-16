from Scylla_Cloud.pages.signIn import locators
from Scylla_Cloud.conftest import User
from Scylla_Cloud.pages.signIn.element import InputElement, ButtonElement

class SignIn():
        path = "/user/signin"
        def __init__(self, browser):
            self.email = InputElement(driver=browser.get_driver(), locator=locators.email_locator)
            self.password = InputElement(driver=browser.get_driver(), locator=locators.password_locator)
            self.signin_button = ButtonElement(driver=browser.get_driver(), locator=locators.signin_button_locator)


        def signin(self, user: User):
            self.email.enter_text(user.email)
            self.password.enter_text(user.password)


