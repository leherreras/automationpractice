import unittest
from selenium import webdriver
import os
from Pages.page_contact_us import PageContactUs


class AutomationPracticeSingUp(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(os.path.abspath(os.path.join(__file__, "..", "..", "drivers/chromedriver")))
        url_base = "http://automationpractice.com"
        self.driver.get(url_base)
        self.page_contact_us = PageContactUs(self.driver)

    def test_send_message(self):
        # validate if isn't possible create a account
        self.page_contact_us.send_message(1, 'test@test.com', '312435', 'this is a message of test')

    def test_send_message_fake(self):
        # validate if isn't possible create a account
        self.page_contact_us.send_message_fake(0, 'test@test.com', '312435', 'this is a message of test')

    def tearDown(self):
        self.driver.quit()
