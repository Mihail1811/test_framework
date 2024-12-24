from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class LoadDelayPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, timeout=60)
        self.btn_after_delay = (
            By.XPATH,
            '//div[@class="container"]//button[@type="button"]'
        )

    def present_button_after_delay(self) -> bool:
        return self.check_existence_element(self.btn_after_delay)
