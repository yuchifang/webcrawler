from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from utils import waitUntil
import data
service = ChromeService(
    executable_path='D:\work\python\webcrawlerBasic\chromedriver_win32\chromedriver.exe')

# todo 取得當前的路徑

driver = webdriver.Chrome(service=service)
driver.get("https://www.instagram.com/")
# cookie 登入法 需要先在其他 瀏覽器 登入你的 IG 帳號 才可使用
# 且關閉 webdriver 時 不能登出

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
