from locators import Locators
from conftest import driver




class TestConstructor:

    def test_transfer_to_bread_section(self, driver):

        driver.find_element(*Locators.TRANSFER_SAUCES_SECTION).click()  # кнопка "Соусы"
        driver.find_element(*Locators.TRANSFER_BREAD_SECTION).click()  # кнопка "Булки"
        assert "tab_tab_type_current" in driver.find_element(*Locators.CONSTRUCTOR_CURRENT_SECTION).get_attribute('class')

    def test_transfer_to_sauce_section(self, driver):

        driver.find_element(*Locators.TRANSFER_SAUCES_SECTION).click()  # кнопка "Соусы"
        assert "tab_tab_type_current" in driver.find_element(*Locators.CONSTRUCTOR_CURRENT_SECTION).get_attribute('class')

    def test_transfer_to_fillings_section(self, driver):

        driver.find_element(*Locators.TRANSFER_FILLINGS_SECTION).click()  # кнопка "начинки"
        assert "tab_tab_type_current" in driver.find_element(*Locators.CONSTRUCTOR_CURRENT_SECTION).get_attribute('class')