# ��M ig �W������
# �b ig �j�M �s�ˬ���
# �j�M�覡���� ig ( �i�H���ϥΪ̿�J )
# ��M ���S�� �s�˥� �άO �s�˿� ���r
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
print("你好")
for file in files:
    title = file.find_element(by=By.TAG_NAME, value="span")
    print(title.text)
    link = driver.find_element(By.LINK_TEXT, title.text)
    link.click()


# print(files)
# searchElement.send_keys(Keys.ENTER)
# time.sleep(3)
# submitButton.click()
# driver.quit()
