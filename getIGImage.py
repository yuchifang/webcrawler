from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import getFoodData.data as data
from selenium.webdriver.chrome.service import Service as ChromeService

from getFoodData.utils import waitUntil

# 48:47

service = ChromeService(
    executable_path='D:\work\python\webcrawlerBasic\chromedriver_win32\chromedriver.exe')

driver = webdriver.Chrome(service=service)
driver.get("https://www.instagram.com/")

print(data)
driver.add_cookie({
    'name': data.sessionidName,
    'value': data.sessionidValue,
    'domain': '.instagram.com',
    'path': '/',
    'expires': data.sessionidExpires,
    'secure': True,
    'httpOnly': True
})

# 3:13 休息

# 重新整理 等待 如果有取到某個值 就繼續下去
# 沒有就用登入的方式

waitUntil(driver, 10, By.XPATH, '//*[@id="loginForm"]/div/div[3]')

# WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located(
#         (By.XPATH, '//*[@id="loginForm"]/div/div[3]'))
# )


usernameInputElement = driver.find_element(By.NAME, 'username')
usernameInputElement.clear()
usernameInputElement.send_keys("testDanFang")

passwordInputElement = driver.find_element(By.NAME, 'password')
passwordInputElement.clear()
passwordInputElement.send_keys("D12345678")
loginButton = driver.find_element(
    By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
# loginButton.click()

# 找到 search input
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

# 換帳號
# 找美食 會想知道 價位 營業時間 地址
