import pytest
from selenium import webdriver

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.set_window_size(1296, 756)
    driver.get("https://stellarburgers.nomoreparties.site/")
    yield driver


