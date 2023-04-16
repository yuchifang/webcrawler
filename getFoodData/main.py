from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from utils import waitUntil
from login import login
from bs4 import BeautifulSoup
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

# 使用 cookie 登入 需要先在其他 瀏覽器 登入你的 IG 帳號 才可使用 且必須保持登入狀態
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


# 關閉 lightbox

try:
    # 找到 lightbox 並點擊關閉按鈕
    # 使用 XPATH
    # lightboxElement = waitUntil(driver,10,By.XPATH,'//*[@id="scrollview"]/following-sibling::div/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')
    # lightboxElement.click()
    # 找到 lightbox 刪除
    # 使用 execute_script
    lightboxElement = waitUntil(
        driver, 10, By.XPATH, '/html/body/div[1]/div/div/div')
    driver.execute_script('''
        lightboxElement=document.querySelector("#scrollview").nextElementSibling
        lightboxElement.parentElement.removeChild(lightboxElement)
    ''')
except TimeoutException or NoSuchElementException:
    login(driver)


loginDataElement = waitUntil(driver,5,By.CLASS_NAME,"_a9-y")
print(loginDataElement)
print(loginDataElement.tag_name)
print(loginDataElement.text)
print(loginDataElement.parent)

# # 點擊 searchButton
# searchButton = driver.find_element(
#     By.XPATH, '//*[@id="scrollview"]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div[2]/div[2]/div')
# searchButton.click()
# waitUntil(driver, 10, By.CLASS_NAME, '_aagu')

# # search
# searchElement = driver.find_element(
#     By.XPATH, '/html/body/div[1]/div/div/div/div/div/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div[1]'
# )
# searchElement.click()

# searchInputElement = driver.find_element(
#     By.XPATH, '/html/body/div[1]/div/div/div/div/div/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/input')
# searchInputElement.send_keys("新竹美食")

# sleep(2)
# searchInputElement.send_keys(Keys.RETURN)
# searchInputElement.send_keys(Keys.ENTER)

# # 搜尋完成
# # 找尋熱門貼文 class
# print("start")
# waitUntil(driver, 15, By.CLASS_NAME, '_aaq9')

# # 不知為什麼一定要 refresh 過後才點的到 貼文
# driver.refresh()
# # 找尋貼文 class
# foodPostItem = waitUntil(
#     driver, 15, By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div[1]/div[2]')

# foodPostItem.click()

# postLightbox = waitUntil(
#     driver, 10, By.CSS_SELECTOR, 'div.o9w3sbdw.bdao358l.alzwoclg.cqf1kptm.cgu29s5g.jcxyg2ei'
# )
# postLightboxHTML = postLightbox.get_attribute('innerHTML')
# soup = BeautifulSoup(postLightboxHTML)
# soup.find()
# print()

# # soup = BeautifulSoup(driver.page_source)
# # print(soup)
# # actions = ActionChains(driver)

# # actions.click_and_hold(foodPostItem)
# # sleep(0.5)
# # actions.release(foodPostItem)
# # actions.perform()

# '''
# https://i.instagram.com/api/v1/media/2923973691486745905/comments/?can_support_threading=true&permalink_enabled=false
# '''

# '''
#     抓之前 判斷 貼文是否存在
#     抓一個 刪一個
#     抓三個 移動一次

#     取得當前資料的總數 dataAll1
#     滾到底
#     取得當前資料的總數 dataAll2
#     相減 計算多了幾個處理多出來的資料
# '''

# '''
#     取得當前資料
#     往下捲
#     依據 request 取值
# '''
# # todo selenium get HTML dom for bs4 get

# # searchElement = driver.find_element(
# #     By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/nav/div[2]/div/div/div[2]')
# # searchInputElement = driver.find_element(
# #     By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/nav/div[2]/div/div/div[2]/input')
# # searchInputElement.send_keys("新竹美食")
# # sleep(1)
# # searchInputElement.send_keys(Keys.RETURN)
# # searchInputElement.send_keys(Keys.ENTER)
