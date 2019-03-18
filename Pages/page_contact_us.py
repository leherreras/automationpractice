import unittest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from Pages.page_index import PageIndex


class PageContactUs:
    def __init__(self, my_driver):
        self.driver = my_driver
        self.page_index = PageIndex(self.driver)
        self.page_index.click_contact_us()
        self.ut = unittest.TestCase()
        self.contact_slc = (By.ID, 'id_contact')
        self.email_ipt = (By.ID, 'email')
        self.order_ipt = (By.ID, 'id_order')
        self.message_txa = (By.ID, 'message')
        self.submit_btn = (By.ID, 'submitMessage')

    def __send_message(self, select_number, email_account, order_number, message_send):
        subject = Select(self.driver.find_element(*self.contact_slc))
        subject.select_by_index(select_number)
        email = self.driver.find_element(*self.email_ipt)
        email.send_keys(email_account)
        order = self.driver.find_element(*self.order_ipt)
        order.send_keys(order_number)
        message = self.driver.find_element(*self.message_txa)
        message.send_keys(message_send)
        submit = self.driver.find_element(*self.submit_btn)
        submit.click()

    def send_message_fake(self, select_number, email_account, order_number, message_send):
        self.__send_message(select_number, email_account, order_number, message_send)
        message_end = self.driver.find_element_by_xpath('//*[@id="center_column"]/div/ol/li')
        self.ut.assertEqual(message_end.text, 'Please select a subject from the list provided.')

    def send_message(self, select_number, email_account, order_number, message_send):
        self.__send_message(select_number, email_account, order_number, message_send)
        message_end = self.driver.find_element_by_xpath('//*[@id="center_column"]/p')
        self.ut.assertEqual(message_end.text, 'Your message has been successfully sent to our team.')
