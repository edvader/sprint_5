from locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from user_data import *
from conftest import driver

class TestRegistration:


    def test_correct_registration(self, driver):
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()  # клик на Личный кабинет
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()  # Зарегистрироваться
        driver.find_element(*Locators.INPUT_NAME).send_keys(name)  # Имя
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(email_for_reg)  # Почта
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(password_for_reg)  # Пароль
        driver.find_element(*Locators.FINAL_REGISTRATION_BUTTON).click()  # Зарегистрироваться
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((Locators.ENTER_BUTTON)))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login', 'URL не совпадает'


    def test_incorrect_registration(self, driver):
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()  # клик на Личный кабинет
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()  # Зарегистрироваться
        driver.find_element(*Locators.INPUT_NAME).send_keys(name)  # Имя
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(email_for_reg)  # Почта
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(incorrect_password_for_reg)  # короткий ароль
        driver.find_element(*Locators.FINAL_REGISTRATION_BUTTON).click()  # Зарегистрироваться
        assert driver.find_element(*Locators.INCORRECT_PASSWORD)