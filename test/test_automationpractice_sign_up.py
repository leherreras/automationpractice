import unittest
from selenium import webdriver
import os
from Pages.page_authentication import PageAuthenticator


class AutomationPracticeSingUp(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(os.path.abspath(os.path.join(__file__, "..", "..", "drivers/chromedriver")))
        url_base = "http://automationpractice.com"
        self.driver.get(url_base)
        self.page_authenticator = PageAuthenticator(self.driver)
        # WebDriverWait(self.driver, 5).until(expected_conditions.presence_of_element_located(self.message_invalid_login))

    def test_create_account(self):
        # validate if isn't possible create a account
        self.page_authenticator.create_account_fake("test@test.com",
                                               "An account using this email address has already been registered. Please enter a valid password or request a new one.")

        # validate if is possible create a account with email that not exist
        self.page_authenticator.create_account_successful("test23198689742314@test.com", 'YOUR PERSONAL INFORMATION')

    def test_login(self):
        # validate if isn't possible login in system with valid user
        self.page_authenticator.login_fail("test@test.com", "tessadfasdfsdafasdfdsa3t", 'Authentication failed.')

        # validate if isn't possible login in system with valid user
        self.page_authenticator.login_fail("test@test.com", "test", 'Invalid password.')

        # validate if is possible login in system
        self.page_authenticator.login_successful("automationpractice-test@gmail.com", "automationpractice_test@123",
                                                 "Welcome to your account. Here you can manage all of your personal information and orders.")

    def tearDown(self):
        self.driver.quit()
