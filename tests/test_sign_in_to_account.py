from locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from user_data import *
from conftest import driver


class TestSignIn:

    def test_sign_in_button_on_main_page(self, driver):
        driver.find_element(*Locators.ENTER_TO_ACCOUNT_BUTTON).click()  # кнопка "Войти в аккаунт"
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(email)  # Почта
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(password)
        driver.find_element(*Locators.ENTER_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((Locators.MAKE_ORDER_BUTTON)))
        assert driver.find_element(*Locators.MAKE_ORDER_BUTTON).text == 'Оформить заказ'


    def test_account_button_on_main_page(self, driver):
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()  # кнопка "Личный кабинет"
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(email)  # Почта
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(password)
        driver.find_element(*Locators.ENTER_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((Locators.MAKE_ORDER_BUTTON)))
        assert driver.find_element(*Locators.MAKE_ORDER_BUTTON).text == 'Оформить заказ'


    def test_sign_in_button_on_register_page(self, driver):
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()  # кнопка "Личный кабинет"
        driver.find_element(*Locators.REGISTRATION_ON_ENTER_PAGE).click()  # кнопка "Зарегистрироваться"
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()  # кнопка "Войти"
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(email)  # Почта
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(password)
        driver.find_element(*Locators.ENTER_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((Locators.MAKE_ORDER_BUTTON)))
        assert driver.find_element(*Locators.MAKE_ORDER_BUTTON).text == 'Оформить заказ'


    def test_sign_in_button_on_recovery_password_page(self, driver):
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()  # кнопка "Личный кабинет"
        driver.find_element(*Locators.RECOVERY_PASSWORD_ON_ENTER_PAGE).click()  # кнопка "Восстановить пароль"
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()  # кнопка "Войти"
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(email)  # Почта
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(password)
        driver.find_element(*Locators.ENTER_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((Locators.MAKE_ORDER_BUTTON)))
        assert driver.find_element(*Locators.MAKE_ORDER_BUTTON).text == 'Оформить заказ'
