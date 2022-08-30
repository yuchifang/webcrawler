from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver

def login(driver:WebDriver):
    usernameInputElement = driver.find_element(By.NAME, 'username')
    usernameInputElement.clear()
    usernameInputElement.send_keys("testDanFang")

    passwordInputElement = driver.find_element(By.NAME, 'password')
    passwordInputElement.clear()
    passwordInputElement.send_keys("D12345678")
    loginButton = driver.find_element(
        By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
    loginButton.click()