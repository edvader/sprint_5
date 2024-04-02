from locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from conftest import driver

class TestRegistration(Locators):


    def test_correct_registration(self, driver):
        driver.find_element(*self.ACCOUNT_BUTTON).click()  # клик на Личный кабинет
        driver.find_element(*self.REGISTRATION_BUTTON).click()  # Зарегистрироваться
        driver.find_element(*self.INPUT_NAME).send_keys('edvader')  # Имя
        driver.find_element(*self.INPUT_EMAIL).send_keys('ed_abakumov_7890@ya.ya')  # Почта
        driver.find_element(*self.INPUT_PASSWORD).send_keys('qwer12')  # Пароль
        driver.find_element(*self.FINAL_REGISTRATION_BUTTON).click()  # Зарегистрироваться
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((self.ENTER_BUTTON)))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/register', 'URL не совпадает'


    def test_incorrect_registration(self, driver):
        driver.find_element(* self.ACCOUNT_BUTTON).click()  # клик на Личный кабинет
        driver.find_element(*self.REGISTRATION_BUTTON).click()  # Зарегистрироваться
        driver.find_element(*self.INPUT_NAME).send_keys('ededed')  # Имя
        driver.find_element(*self.INPUT_EMAIL).send_keys('ed_abakumov_7890@ya.ya')  # Почта
        driver.find_element(*self.INPUT_PASSWORD).send_keys('qwer1')  # короткий ароль
        driver.find_element(*self.FINAL_REGISTRATION_BUTTON).click()  # Зарегистрироваться
        incorrect_password = driver.find_element(By.XPATH, "./html/body/div/div/main/div/form/fieldset[3]/div/p").text
        assert incorrect_password == 'Некорректный пароль'