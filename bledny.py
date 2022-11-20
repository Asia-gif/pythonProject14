from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome(executable_path='C:/Users/Asia/PycharmProjects/chromedriver.exe')
driver.get('https://demoblaze.com')

loginButton = driver.find_element_by_id('login2')
loginButton.click()

driver.implicitly_wait(5)

loginFieldUsername = driver.find_element_by_id('loginusername')
loginFieldUsername.send_keys('123')

loginFieldPassword = driver.find_element_by_id('loginpassword')
loginFieldPassword.send_keys('cacek')

loginSubmitButton = driver.find_element_by_xpath('//button[contains(text(), "Log in")]')
loginSubmitButton.click()

try:
    WebDriverWait(driver, 3).until(expected_conditions.alert_is_present(), 'timeout')
    passwordAlert = driver.switch_to.alert
    print ('alert: ' + passwordAlert.text)
    passwordAlert.accept()

except TimeoutException:
    print('alert not displayed')

# driver.quit()






