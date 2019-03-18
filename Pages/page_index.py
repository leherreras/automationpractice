import unittest

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class PageIndex:
    def __init__(self, my_driver):
        self.driver = my_driver
        self.ut = unittest.TestCase()
        self.search_query_top = (By.ID, 'search_query_top')
        self.contact_us_btn = (By.XPATH, '//*[@id="contact-link"]/a')
        self.sing_up_btn = (By.XPATH, "/html/body/div/div[1]/header/div[2]/div/div/nav/div[1]/a")

    def click_sign_in(self):
        # Go to sign in
        sign_up = self.driver.find_element(*self.sing_up_btn)
        sign_up.click()

    def search_query(self, query):
        self.driver.implicitly_wait(2)
        search = self.driver.find_element(*self.search_query_top)
        search.send_keys(query + Keys.ENTER)
        dress_page = self.driver.find_element_by_xpath('/html/body/div/div[2]/div/div[3]/div[2]/ul/li[1]/div/div[2]/h5/a')
        self.ut.assertTrue("dress" in dress_page.text.lower())

    def click_contact_us(self):
        # Go to contact us
        contact_us = self.driver.find_element(*self.contact_us_btn)
        contact_us.click()
