from selenium.webdriver.common.by import By
from features.steps.target_sign_in_script import driver


#amazon_logo
driver.find_element(By.CSS_SELECTOR, 'i.a-icon-logo')

#your_name_field
driver.find_element(By.ID, 'ap_customer_name')

#mobile_number_or_email_field
driver.find_element(By.ID, 'ap_email')

#password_field
driver.find_element(By.ID, 'ap_password')

#password_context_field
driver.find_element(By.ID, 'ap_password_context_message_section')

#reenter_password_field
driver.find_element(By.ID, 'ap_password_check')

#continue_button
driver.find_element(By.ID, 'continue')

#conditions_of_use
driver.find_element(By.XPATH, "//*[text()='Conditions of Use']")

#privacy_notice
driver.find_element(By.XPATH, "//*[text()='Privacy Notice']")

#sign_in_link
driver.find_element(By.CSS_SELECTOR, "//a.a-link-emphasis")
