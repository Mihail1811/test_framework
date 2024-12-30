import allure
from pages.MainPage import MainPage
from pages.LoadDelayPage import LoadDelayPage
from pages.ProgressBarPage import ProgressBarPage
from pages.TextInputPage import TextInputPage
from pages.DynamicTablePage import DynamicTablePage
from pages.NBSPPage import NBSPPage


@allure.title('Проверка работы Progress Bar')
@allure.description('''
Тест проверяет, что:
1. Значение Result < 5;
2. Значение Duration < 17000;
''')
def test_progress_bar(driver):
    main_page = MainPage(driver)
    main_page.click_link_progress_bar()
    progress_bar_page = ProgressBarPage(driver)
    progress_bar_page.click_start_button()
    progress_bar_page.wait_until_desired_value()
    progress_bar_page.click_stop_button()
    with allure.step(r'Проверить, что значение "Result" < 5'):
        assert progress_bar_page.get_result_text() < 5, \
            'Значение Result больше 5'
    with allure.step(r'Проверить, что значение "Duration " < 17000'):
        assert progress_bar_page.get_duration_text() < 17000, \
            'Значение Duration больше 17000'


@allure.title('Проверка отображения кнопки после загрузки страницы')
@allure.description('''
Шаги выполнения теста:
1. Загрузка страницы с задержкой;
2. Проверка, что кнопка отобразилась;
''')
def test_load_delay(driver):
    main_page = MainPage(driver)
    main_page.click_link_load_delay()
    load_delay_page = LoadDelayPage(driver)
    with allure.step(r'Проверить, что кнопка "Button '
                     r'Appearing After Delay" отображается'):
        assert load_delay_page.present_button_after_delay() is \
               True, 'Кнопка не отображается!'


@allure.title('Проверка изменения названия кнокпи')
@allure.description('''
Шаги выполнения теста:
1. Ввести текст в поле для ввода;
2. Нажать кнопку;
3. Удостовериться, что название до нажатия кнопки было одно, после - другое;
''')
def test_text_input(driver):
    main_page = MainPage(driver)
    main_page.click_link_text_input()
    text_input_page = TextInputPage(driver)
    original_name_button = text_input_page.get_name_button()
    with allure.step(r'''Проверить, что кнопка имеет значение -
    "Button That Should Change it's Name Based on Input Value"'''):
        assert original_name_button == \
               "Button That Should Change it's Name Based on Input Value", \
               'Текст кнопки не совпадает с ожидаемым!'
    text_input_page.input_new_name_button(
        text='Name of button has been changed'
    )
    text_input_page.click_original_button()
    updated_name_button = text_input_page.get_name_button()
    with allure.step(r'Проверить, что название кнопки изменилось на то, '
                     r'что было введено в поле ввода'):
        assert updated_name_button == 'Name of button has been changed', \
            'Текст кнопки не совпадает с ожидаемым!'
    with allure.step(f'Проверить, что до нажатия было одно имя кнопки'
                     f'({original_name_button}), '
                     f'после - {updated_name_button}'):
        assert updated_name_button != original_name_button, \
            'Название кнопки изменилось'


@allure.title(r'Проверка схожесть значений CPU в '
              r'таблице и в выделенной желтым строке')
@allure.description('''
Шаги выполнения теста:
1. Считать значение CPU для Chrome в таблице;
2. Сравнить считанное значение со значением в
выделенной желтым строке в точности до символа;
''')
def test_dynamic_table(driver):
    main_page = MainPage(driver)
    main_page.click_link_dynamic_table()
    dynamic_table = DynamicTablePage(driver)
    with allure.step(r'Проверить, что считанное значение в столбце '
                     r'CPU для Chrome в точности до символа равно значению'
                     r' в выделенной желтым строке'):
        assert dynamic_table.get_cpu_value_table() == \
               dynamic_table.get_highlighted_value_cpu(), \
               'Значения не совпадают!'


@allure.title(r'Проверка отображения кнопки с неразрывным пробелом')
@allure.description('''
Тест проверяет, что кнопка "My Button" с неразрывным
пробелом отображается на странице
''')
def test_nbsp(driver):
    main_page = MainPage(driver)
    main_page.click_link_unbroken_space()
    nbsp_page = NBSPPage(driver)
    with allure.step(r'Проверить, что кнопка "My Button" отображается'):
        assert nbsp_page.present_my_button() is True, 'Кнопка не отображается!'
