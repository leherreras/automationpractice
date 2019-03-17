class PageIndex:
    def __init__(self, my_driver):
        self.driver = my_driver

    def click_sign_in(self):
        # Go to sign in
        sign_up = self.driver.find_element_by_xpath("/html/body/div/div[1]/header/div[2]/div/div/nav/div[1]/a")
        sign_up.click()
