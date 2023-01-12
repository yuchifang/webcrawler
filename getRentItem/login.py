from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
def login(driver:WebDriver):
    usernameInputElement = driver.find_element(By.ID, 'email')
    usernameInputElement.clear()
    usernameInputElement.send_keys("fang91013715@yahoo.com.tw")
    passwordInputElement = driver.find_element(By.ID, 'pass')
    passwordInputElement.clear()
    passwordInputElement.send_keys("root1234")
    loginButton = driver.find_element(
        By.ID, 'loginbutton')
    loginButton.click()