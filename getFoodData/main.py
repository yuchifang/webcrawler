from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from utils import waitUntil
import data
service = ChromeService(
    executable_path='D:\work\python\webcrawlerBasic\chromedriver_win32\chromedriver.exe')

# todo 取得當前的路徑
# todo 看看位什麼 cookie 無法使用


print(data.sessionidName)
print(data.sessionidExpires)
print(data.sessionidValue)

driver = webdriver.Chrome(service=service)
driver.get("https://www.instagram.com/")
driver.add_cookie({
    'name': data.sessionidName,
    'value': data.sessionidValue,
    'domain': '.instagram.com',
    'path': '/',
    'expires': data.sessionidExpires,
    'secure': True,
    'httpOnly': True
})


# driver.refresh()
# 重新整理
# 等待 如果有取到某個值 就繼續下去

# try:
# except

# 沒有就用登入的方式

# 等入的 function
# 是否進入登入畫面
# waitUntil(driver, 10, By.XPATH, '//*[@id="loginForm"]/div/div[3]')
