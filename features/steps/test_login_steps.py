from behave import given, when, then
from selenium import webdriver

@given('I open the browser')
def step_open_browser(context):
    context.driver = webdriver.Chrome()

@when('I navigate to the homepage')
def step_navigate_home(context):
    context.driver.get("https://www.simplepractice.com/")

@then('the page title should contain "SimplePractice"')
def step_check_title(context):
    assert "SimplePractice" in context.driver.title
    context.driver.quit()