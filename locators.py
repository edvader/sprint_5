
from selenium.webdriver.common.by import By

class Locators:
    ACCOUNT_BUTTON = [By.XPATH, '//*[@id="root"]/div/header/nav/a/p']
    REGISTRATION_BUTTON = [By.XPATH, '//*[@id="root"]/div/main/div/div/p/a']
    INPUT_NAME = [By.XPATH, '//input[@class="text input__textfield text_type_main-default"]']
    INPUT_EMAIL = [By.XPATH, '//label[text()="Email"]/following-sibling::input']
    INPUT_PASSWORD = [By.XPATH, '//label[text()="Пароль"]/following-sibling::input']
    FINAL_REGISTRATION_BUTTON = [By.XPATH, '//*[@id="root"]/div/main/div/form/button']
    ENTER_TO_ACCOUNT_BUTTON = [By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button']
    ENTER_BUTTON = [By.XPATH, '//*[@id="root"]/div/main/div/form/button']
    MAKE_ORDER_BUTTON = [By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button']
    REGISTRATION_ON_ENTER_PAGE = [By.XPATH, '//*[@id="root"]/div/main/div/div/p[1]/a']
    RECOVERY_PASSWORD_ON_ENTER_PAGE = [By.XPATH, '//*[@id="root"]/div/main/div/div/p[2]/a']
    SAVE_BUTTON_ON_PERSONAL_PAGE = [By.XPATH, '//*[@id="root"]/div/main/div/div/div/div/button[2]']
    CONSTRUCTOR_BUTTON = [By.XPATH, '//*[@id="root"]/div/header/nav/ul/li[1]/a/p']
    LOGO_BURGERS = [By.CLASS_NAME, 'AppHeader_header__logo__2D0X2']
    LOG_OUT_BUTTON = [By.XPATH, '//*[@id="root"]/div/main/div/nav/ul/li[3]/button']
    CONSTRUCTOR_CURRENT_SECTION = [By.XPATH, "//*[contains(@class, 'tab_tab_type_current')]"]
    TRANSFER_BREAD_SECTION = [By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[1]/span']
    TRANSFER_SAUCES_SECTION = [By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[2]/span']
    TRANSFER_FILLINGS_SECTION = [By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[3]/span']

