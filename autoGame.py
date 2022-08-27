from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
# PATH = "chromedriver_win32/chromedriver.exe"
PATH = "edgedriver_win32/msedgedriver.exe"
driver = webdriver.Edge(PATH)
driver.get("https://tsj.tw/")

blowButton = driver.find_element(By.ID, "click")
blowCount = driver.find_element(
    By.XPATH, '//*[@id="app"]/div[2]/div[4]/div[2]/h4[2]')

actions = ActionChains(driver)

totalClickCount = driver.find_element(
    By.XPATH, '//*[@id="app"]/div[2]/div[4]/div[2]/h4[2]')
print(totalClickCount.text)


# for i in range(100):
#     actions.click(blowButton)
#     actions.release(blowButton)
# actions.perform()


# 取得當前得點數
# 價格會因為 點及次數不同而改變
# 先點擊 最貴的 不行就點擊 第二貴的

# 網站不能用 所以改用 ig 40:26
actions.perform()

print(blowCount.text)
