from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
from selenium.common.exceptions import NoSuchElementException
import allure


class NBSPPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, timeout=60)
        self.my_btn = (By.XPATH, '//button[text()="My\u00A0Button"]')

    @allure.step('Проверить, что кнопка "My Button" отображается')
    def present_my_button(self) -> None:
        self.check_existence_element(self.my_btn)
