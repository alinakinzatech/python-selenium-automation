Amazon logo $x("//i[@class='a-icon a-icon-logo']")
driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo']")

Email field
driver.find_element(By.ID, 'ap_email')

Continue button
driver.find_element(By.ID, 'continue')

Conditions of use link $x("//*[text()='Conditions of Use']")
driver.find_element(By.XPATH, "//*[text()='Conditions of Use']")

Privacy Notice link  $x("//*[text()='Privacy Notice']")
driver.find_element(By.XPATH, "//*[text()='Privacy Notice']")

Need help link $x("//span[contains(text(), 'help')]")
driver.find_element(By.XPATH, "//span[contains(text(), 'help')]")

Forgot your password link
driver.find_element(By.ID, 'auth-fpp-link-bottom')

Other issues with Sign-In link
driver.find_element(By.ID, 'ap-other-signin-issues-link')

Create your Amazon account button
driver.find_element(By.ID, 'createAccountSubmit')



from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.target.com/')
#find and click on the element
driver.find_element(By.XPATH, "//span[text()='Sign in']").click()
sleep(3)
#find sign in on the nav menu and click
driver.find_element(By.XPATH, "//button[text()='Sign in']").click()
sleep(3)
# verification:
# by finding 1 element
# driver.find_element(By.XPATH, "//div[@data-test='lp-resultsCount']")
# print('Test case passed')

# by checking text
actual_text = driver.find_element(By.XPATH, "//span[text()='Sign into your Target account']").text
expected_text = 'Sign into your Target account'

assert expected_text in actual_text, f'Error. Text {expected_text} not in {actual_text}'
driver.find_element(By.ID, 'login')
print('Test case passed')