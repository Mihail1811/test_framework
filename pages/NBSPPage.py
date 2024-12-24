from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class NBSPPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, timeout=60)
        self.my_btn = (By.XPATH, '//button[text()="My\u00A0Button"]')

    def present_my_button(self):
        return self.check_existence_element(self.my_btn)
