from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open target page')
def open_target_main(context):
    context.driver.get('https://www.target.com/')


@when('Click on cart icon')
def click_on_cart_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/CartLink']").click()
    sleep(4)


@then('“Your cart is empty” message is shown')
def check_message_empty(context):
    actual_text = context.driver.find_element(By.XPATH, "//*[text()='Your cart is empty']").text
    expected_text = 'Your cart is empty'
    assert actual_text == expected_text, f'Error. Text {expected_text} not in {actual_text}'