from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

from utils import waitUntil
from login import login

import data
import pathlib
import platform

print("some", __file__)

currentFolderPath = pathlib.Path(__file__).parent.resolve()
MY_OS = platform.system()
if MY_OS == "Linux":
    path = str(currentFolderPath) + '/chromedriver_linux64/chromedriver'
else:
    path = str(currentFolderPath) + '\chromedriver_win32\chromedriver.exe'

service = ChromeService(executable_path=path)


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

try:
    # 找到 lightbox 並點擊關閉按鈕
    # lightboxElement = waitUntil(driver,10,By.XPATH,'//*[@id="scrollview"]/following-sibling::div/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')
    # lightboxElement.click()
    # 找到 lightbox 刪除
    lightboxElement = waitUntil(
        driver, 10, By.XPATH, '/html/body/div[1]/div/div/div')
    driver.execute_script('''
        lightboxElement=document.querySelector("#scrollview").nextElementSibling
        lightboxElement.parentElement.removeChild(lightboxElement)
    ''')
except TimeoutException or NoSuchElementException:
    login(driver)

searchElemnt = driver.find_element(
    By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/nav/div[2]/div/div/div[2]')
searchElemnt.click()
searchInputElement = driver.find_element(
    By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/nav/div[2]/div/div/div[2]/input')
searchInputElement.send_keys("新竹美食")
sleep(1)
searchInputElement.send_keys(Keys.RETURN)
searchInputElement.send_keys(Keys.ENTER)
