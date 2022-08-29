from time import sleep
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
    # element = driver.find_element(By.CLASS_NAME,"_a9-- _a9_1").size()
    searchElement = waitUntil(driver, 10, By.CLASS_NAME, "_a9-- _a9_1")
except TimeoutException:
    try:
        lightboxElement = driver.find_element(By.XPATH,'//*[@id="scrollview"]/following-sibling::div')
        # lightboxElement = waitUntil(driver,10,By.XPATH,'//*[@id="scrollview"]')
        print("-----------------------")
        print(lightboxElement.tag_name)
        print("-----------------------")
        print(lightboxElement.text)
        print("-----------------------")
        print("-----------------------")
        driver.switch_to.frame(lightboxElement)
        testText=lightboxElement.find_element(By.XPATH,'//*[@id="scrollview"]/div/div/div/div[1]/div[1]/section/main/div[1]/section/div/div[2]/h4')
        print(testText.text)
        # driver.switch_to.window()
        # todo 抓抓看 純 div
        # //*[@id="mount_0_0_zF"]/div/div/div/div[2]
    except NoSuchElementException:
        print("some")
    except TimeoutException:
        print("TimeError")
except NoSuchElementException:
    print("abv")

# 重新整理
# todo 感覺抓不到 lightbox html 

# 等待 如果有取到某個值 就繼續下去

# 沒有就用登入的方式

# 等入的 function
# 是否進入登入畫面
# waitUntil(driver, 10, By.XPATH, '//*[@id="loginForm"]/div/div[3]')
