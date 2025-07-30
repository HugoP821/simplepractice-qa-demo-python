from utils.driver_factory import get_driver

def test_homepage_loads():
    driver = get_driver()
    driver.get("https://www.simplepractice.com/")
    assert "SimplePractice" in driver.title
    driver.quit()