from Scylla_Cloud.pages.signIn import locators
from Scylla_Cloud.conftest import User
from Scylla_Cloud.pages.signIn.element import InputElement, ButtonElement

class SignIn():
        path = "/user/signin"
        def __init__(self, browser):
            self.email = InputElement(driver=browser.get_driver(), locator=locators.email_locator)
            self.password = InputElement(driver=browser.get_driver(), locator=locators.password_locator)
            self.signin_button = ButtonElement(driver=browser.get_driver(), locator=locators.signin_button_locator)

        def click_on_email_field(self):
            email_field = self.driver.find_element(locators.email_locator[0], locators.email_locator[1])
            email_field.click()
            return email_field

        def click_on_password_field(self):
            password_field = self.driver.find_element(locators.password_locator[0], locators.password_locator[1])
            password_field.click()
            return password_field

        def click_on_signin_button(self):
            signin_button = self.driver.find_element(locators.signin_button_locator[0], locators.signin_button_locator[1])
            signin_button.click()
            return signin_button