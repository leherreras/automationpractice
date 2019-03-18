import unittest
from selenium import webdriver
import os
from Pages.page_index import PageIndex


class AutomationPracticeSingUp(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(os.path.abspath(os.path.join(__file__, "..", "..", "drivers/chromedriver")))
        url_base = "http://automationpractice.com"
        self.driver.get(url_base)
        self.page_index = PageIndex(self.driver)

    def test_search_query(self):
        # validate if isn't possible create a account
        self.page_index.search_query("dress")

    def tearDown(self):
        self.driver.quit()
