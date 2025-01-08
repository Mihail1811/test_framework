from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
from selenium.common.exceptions import NoSuchElementException
import allure


class LoadDelayPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, timeout=60)
        self.btn_after_delay = (
            By.XPATH,
            '//div[@class="container"]//button[@type="button"]'
        )

    @allure.step(r'Проверить, что кнопка "Button '
                 r'Appearing After Delay" отображается')
    def present_button_after_delay(self) -> None:
        self.check_existence_element(self.btn_after_delay)
