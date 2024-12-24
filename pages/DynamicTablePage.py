from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class DynamicTablePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, timeout=60)
        self.highlighted_value_cpu = (By.CSS_SELECTOR, '.bg-warning')
        self.cpu_value_table = (
            By.XPATH,
            '//span[parent::div/span/text()="Chrome"]'
        )

    def get_cpu_value_table(self) -> str:
        rows = self.find_elements(*self.cpu_value_table)
        for count in range(5):
            if rows[count].text[-1] == '%':
                return rows[count].text

    def get_highlighted_value_cpu(self) -> str:
        return self.get_text(self.highlighted_value_cpu).split()[-1]
