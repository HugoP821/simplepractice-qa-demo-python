from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    URL = "https://secure.simplepractice.com/login"

    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")

    def open(self):
        self.driver.get(self.URL)

    def login(self, username, password):
        self.type(self.USERNAME, username)
        self.type(self.PASSWORD, password)
        self.click(self.LOGIN_BTN)