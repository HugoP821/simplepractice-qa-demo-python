import pytest
from pages.login_page import LoginPage
from utils.driver_factory import get_driver

@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

def test_open_login_page(driver):
    page = LoginPage(driver)
    page.open()
    assert "SimplePractice" in driver.title