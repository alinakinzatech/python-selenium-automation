from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from behave import given, when, then


@when ('Click Sign In')
def click_sign_in(context):
    context.driver.find_element(By.XPATH, "//span[text()='Sign in']").click()
sleep(3)


@when ('From right side navigation menu, click Sign In')
def click_sign_in_right(context):
    context.driver.find_element(By.XPATH, "//button[text()='Sign in']").click()



@then ('Sign In form opened')
def sign_in_form(context):
    sign_in_form = context.driver.find_element(By.XPATH, "//*[text()='Sign into your Target account']").text
    assert sign_in_form.is_displayed(), "Sign In form did not open"
