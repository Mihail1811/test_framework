import allure
from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class ProgressBarPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, timeout=60)
        self.start_btn = (By.ID, 'startButton')
        self.stop_btn = (By.ID, 'stopButton')
        self.value_scale = (By.ID, 'progressBar')
        self.result_text = (By.ID, 'result')

    @allure.step(r'Нажать кнопку "Start"')
    def click_start_button(self) -> None:
        self.click_element(self.start_btn)

    @allure.step(r'Ждать, когда ProgressBar станет 75%')
    def wait_until_desired_value(self) -> None:
        while True:
            progress = self.get_text(self.value_scale)[:2]
            if int(progress) == 75:
                break

    @allure.step(r'Нажать кнопку "Stop"')
    def click_stop_button(self) -> None:
        self.click_element(self.stop_btn)

    def get_result_text(self) -> int:
        return int(self.get_text(self.result_text)[8])

    def get_duration_text(self) -> int:
        return int(self.get_text(self.result_text)[22:])
