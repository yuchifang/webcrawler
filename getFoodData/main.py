from selenium import webdriver
from selenium.webdriver.common.by import By
from utils import waitUntil


PATH = "chromedriver_win32/chromedriver.exe"

driver = webdriver.Chrome(PATH)
driver.get("https://www.instagram.com/")
driver.add_cookie({
    'name': 'sessionid',
    'value': '55076376813%3Ae90FlRQ8SmowCU%3A23%3AAYcsNaa3y4vrR5ZSGcXK3AqGOtmDtDiyAGmkYyOxdg',
    'domain': '.instagram.com',
    'path': '/',
    'expires': '2023-08-27T08:25:22.975Z',
    'secure': True,
    'httpOnly': True
})

# 重新整理
# 等待 如果有取到某個值 就繼續下去

# try:
# except

# 沒有就用登入的方式

# 等入的 function
# 是否進入登入畫面
waitUntil(driver, 10, By.XPATH, '//*[@id="loginForm"]/div/div[3]')
