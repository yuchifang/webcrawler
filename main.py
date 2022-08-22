# 找尋 ig 上的美食
# 在 ig 搜尋 新竹美食
# 搜尋方式等於 ig ( 可以讓使用者輸入 )
# 找尋 有沒有 新竹市 或是 新竹縣 的字
#
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
PATH = "chromedriver_win32/chromedriver.exe"
# "D:/work/python/webcrawler/chromedriver_win32/chromedriver.exe"

driver = webdriver.Chrome(PATH)
driver.get("https://www.dcard.tw/f")
searchElement = driver.find_element(by=By.NAME, value="query")
searchElement.send_keys("美食", Keys.ENTER)

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "sc-f860e6e9-1"))
)

files = driver.find_elements(by=By.CLASS_NAME, value="sc-8fe4d6a1-3")


for file in files:
    title = file.find_element(by=By.TAG_NAME, value="span")
    link = driver.find_element(By.LINK_TEXT, title.text)
    link.click()


# print(files)
# searchElement.send_keys(Keys.ENTER)
# time.sleep(3)
# submitButton.click()
# driver.quit()
