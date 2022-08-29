from re import search
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from utils import waitUntil
import data
import pathlib

currentFolderPath = pathlib.Path(__file__).parent.resolve() 
# todo test window

service = ChromeService(
    executable_path= str(currentFolderPath) + '/chromedriver_linux64/chromedriver' # linux
    #executable_path='D:\work\python\webcrawlerBasic\chromedriver_win32\chromedriver.exe' # window
    )


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


driver.refresh()

# searchElement = waitUntil(driver, 10, By.CLASS_NAME, '_a9-- _a9_1')

try:
    searchElement = waitUntil(driver, 10, By.CLASS_NAME, "_a9-- _a9_1")
except TimeoutException:
    try:
        searchElemen2 = waitUntil(driver, 10, By.CLASS_NAME, "_a9-- _a9_1")
    except:
        searchElemen3 = waitUntil(driver, 10, By.XPATH,'//*[@id="scrollview"]/div/div/div/div[1]/div[1]/section/nav/div[2]/div/div/div[2]')
except NoSuchElementException:
    print("abv")

# 重新整理
# 等待 如果有取到某個值 就繼續下去

# 沒有就用登入的方式

# 等入的 function
# 是否進入登入畫面
# waitUntil(driver, 10, By.XPATH, '//*[@id="loginForm"]/div/div[3]')
