# 找尋 ig 上的美食
# 在 ig 搜尋 新竹美食
# 搜尋方式等於 ig ( 可以讓使用者輸入 )
# 找尋 有沒有 新竹市 或是 新竹縣 的字
#

from selenium import webdriver
PATH = "chromedriver_win32/chromedriver.exe"
# "D:/work/python/webcrawler/chromedriver_win32/chromedriver.exe"

driver = webdriver.Chrome(PATH)
driver.get("https://www.dcard.tw/f")
print(driver.title)
# driver.quit()
