from locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from user_data import *
from conftest import driver

class TestAccountsButtons:

    def test_personal_account_page(self, driver):
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()  # кнопка "Личный кабинет"
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(email)  # Почта
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(password)
        driver.find_element(*Locators.ENTER_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((Locators.ACCOUNT_BUTTON)))
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()  # кнопка "Личный кабинет"
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((Locators.SAVE_BUTTON_ON_ACCOUNT_PAGE)))
        assert driver.find_element(*Locators.SAVE_BUTTON_ON_ACCOUNT_PAGE).text == 'Сохранить'

    def test_constructor_buttton_on_personal_account_page(self, driver):
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()  # кнопка "Личный кабинет"
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(email)  # Почта
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(password)
        driver.find_element(*Locators.ENTER_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((Locators.ACCOUNT_BUTTON)))
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()  # кнопка "Личный кабинет"
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((Locators.SAVE_BUTTON_ON_ACCOUNT_PAGE)))
        driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()  # кнопка "Конструктор"
        assert driver.find_element(*Locators.ACCOUNT_BUTTON).text == 'Личный Кабинет'

    def test_logotip_on_personal_account_page(self, driver):
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()  # кнопка "Личный кабинет"
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(email)  # Почта
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(password)
        driver.find_element(*Locators.ENTER_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((Locators.ACCOUNT_BUTTON)))
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()  # кнопка "Личный кабинет"
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((Locators.SAVE_BUTTON_ON_ACCOUNT_PAGE)))
        driver.find_element(*Locators.LOGO_BURGERS).click()  # Логотип в хедере
        assert driver.find_element(*Locators.ACCOUNT_BUTTON).text == 'Личный Кабинет'

    def test_log_out_from_personal_account_page(self, driver):
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()  # кнопка "Личный кабинет"
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(email)  # Почта
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(password)
        driver.find_element(*Locators.ENTER_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((Locators.ACCOUNT_BUTTON)))
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()  # кнопка "Личный кабинет"
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((Locators.SAVE_BUTTON_ON_ACCOUNT_PAGE)))
        driver.find_element(*Locators.LOG_OUT_BUTTON).click()  # кнопка "Выход"
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((Locators.ENTER_BUTTON)))
        assert driver.find_element(*Locators.ENTER_BUTTON).text == 'Войти'