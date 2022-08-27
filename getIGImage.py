from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
# 48:47

PATH = "chromedriver_win32/chromedriver.exe"

driver = webdriver.Chrome(PATH)
driver.get("https://www.instagram.com/")

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, '//*[@id="loginForm"]/div/div[3]'))
)


usernameInputElement = driver.find_element(By.NAME, 'username')
usernameInputElement.clear()
usernameInputElement.send_keys("fang_felipe")

passwordInputElement = driver.find_element(By.NAME, 'password')
passwordInputElement.clear()
passwordInputElement.send_keys("Dan112358")
loginButton = driver.find_element(
    By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
loginButton.click()


WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.CLASS_NAME, "cTBqC")
    )
)
searchElement = driver.find_element(By.CLASS_NAME, "cTBqC")
searchElement.click()
searchInputElement = driver.find_element(By.CLASS_NAME, "XTCLo")
searchInputElement.send_keys("新竹美食")

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div'))
)
searchInputElement.send_keys(Keys.RETURN)
