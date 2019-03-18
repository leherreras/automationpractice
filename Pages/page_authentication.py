import unittest

from selenium.webdriver.common.by import By

from Pages.page_index import PageIndex


class PageAuthenticator:
    def __init__(self, my_driver):
        self.driver = my_driver
        self.page_index = PageIndex(self.driver)
        self.page_index.click_sign_in()
        self.ut = unittest.TestCase()
        self.email = (By.ID, 'email')
        self.passwd = (By.ID, 'passwd')
        self.submit_login = (By.ID, 'SubmitLogin')
        self.email_create = (By.ID, 'email_create')
        self.submit_create = (By.ID, 'SubmitCreate')

    def __select_email_pass(self, email_account, password):
        self.driver.implicitly_wait(5)
        email = self.driver.find_element(*self.email)
        email.clear()
        email.send_keys(email_account)
        passwd = self.driver.find_element(*self.passwd)
        passwd.clear()
        passwd.send_keys(password)
        submit_login = self.driver.find_element(*self.submit_login)
        submit_login.click()

    def login_fail(self, email: str, password: str, message: str):
        self.__select_email_pass(email, password)
        invalid_login = self.driver.find_element_by_xpath('//*[@id="center_column"]/div[1]/ol/li')
        self.ut.assertEqual(invalid_login.text, message)

    def login_successful(self, email, password, message):
        self.__select_email_pass(email, password)
        valid_login = self.driver.find_element_by_xpath('//*[@id="center_column"]/p')
        self.ut.assertEqual(valid_login.text, message)
        sign_out = self.driver.find_element_by_xpath('/html/body/div/div[1]/header/div[2]/div/div/nav/div[2]/a')
        sign_out.click()

    def __select_create_account(self, email_account):
        self.driver.implicitly_wait(5)
        email_create = self.driver.find_element(*self.email_create)
        email_create.clear()
        email_create.send_keys(email_account)
        submit_create = self.driver.find_element(*self.submit_create)
        submit_create.click()

    def create_account_fake(self, email_account, message):
        self.__select_create_account(email_account)
        error_messages = self.driver.find_element_by_xpath('//*[@id="create_account_error"]/ol/li')
        self.ut.assertEqual(error_messages.text, message)

    def create_account_successful(self, email_account, message):
        self.__select_create_account(email_account)
        error_messages = self.driver.find_element_by_xpath('//*[@id="account-creation_form"]/div[1]/h3')
        self.ut.assertEqual(error_messages.text, message)
