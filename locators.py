
from selenium.webdriver.common.by import By

class Locators:
    ACCOUNT_BUTTON = [By.XPATH, "//*[contains(text(), 'Личный Кабинет')]"]
    REGISTRATION_BUTTON = [By.XPATH, '//*[@id="root"]/div/main/div/div/p/a']
    INPUT_NAME = [By.XPATH, '//input[@class="text input__textfield text_type_main-default"]']
    INPUT_EMAIL = [By.XPATH, '//label[text()="Email"]/following-sibling::input']
    INPUT_PASSWORD = [By.XPATH, '//label[text()="Пароль"]/following-sibling::input']
    FINAL_REGISTRATION_BUTTON = [By.XPATH, '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]']
    ENTER_TO_ACCOUNT_BUTTON = [By.XPATH, "//button[text()='Войти в аккаунт']"]
    ENTER_BUTTON = [By.XPATH, ".//button[contains(text(),'Войти')]"]
    MAKE_ORDER_BUTTON = [By.XPATH, ".//button[contains(text(), 'Оформить заказ')]"]
    REGISTRATION_ON_ENTER_PAGE = [By.XPATH, "//*[contains(text(), 'Зарегистрироваться')]"]
    RECOVERY_PASSWORD_ON_ENTER_PAGE = [By.XPATH, "//*[contains(text(), 'Восстановить пароль')]"]
    SAVE_BUTTON_ON_ACCOUNT_PAGE = [By.XPATH, "//*[contains(text(), 'Сохранить')]"]
    CONSTRUCTOR_BUTTON = [By.XPATH, "//*[contains(text(), 'Конструктор')]"]
    LOGO_BURGERS = [By.CLASS_NAME, 'AppHeader_header__logo__2D0X2']
    LOG_OUT_BUTTON = [By.XPATH, "//*[contains(text(), 'Выход')]"]
    CONSTRUCTOR_CURRENT_SECTION = [By.XPATH, "//*[contains(@class, 'tab_tab_type_current')]"]
    TRANSFER_BREAD_SECTION = [By.XPATH, "//*[contains(text(), 'Булки')]"]
    TRANSFER_FILLINGS_SECTION = [By.XPATH, "//*[contains(text(), 'Начинки')]"]
    TRANSFER_SAUCES_SECTION = [By.XPATH, "//*[contains(text(), 'Соусы')]"]
    INCORRECT_PASSWORD = [By.XPATH, "//p[contains(text(),'Некорректный пароль')]"]


