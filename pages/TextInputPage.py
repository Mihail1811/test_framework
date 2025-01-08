import allure
from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class TextInputPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, timeout=60)
        self.new_btn_name = (By.ID, 'newButtonName')
        self.updating_btn = (By.ID, 'updatingButton')

    @allure.step(r'Ввести в поле ввода новое имя кнопки')
    def input_new_name_button(self, text: str) -> None:
        self.fill_field(self.new_btn_name, text)

    @allure.step(r'Получить значение кнопки')
    def get_name_button(self) -> str:
        return self.get_text(self.updating_btn)

    @allure.step(r'Нажать на кнопку с первоначальным названием')
    def click_original_button(self) -> None:
        self.click_element(self.updating_btn)
