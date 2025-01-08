@echo off

:: Проверить наличие allure
where allure >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo Allure не найден.
    exit /b 1
)

:: Удалить старые отчеты
rmdir /s /q allure-results
rmdir /s /q allure-report

:: Запуск тестов
pytest --alluredir=allure-results

:: Генерация отчета
allure generate allure-results --clean -o allure-report

:: Открыть отчет
allure open allure-results
