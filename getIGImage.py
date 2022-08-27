# 推 github
# 紀錄一下 最近學的東西

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
# 48:47

PATH = "chromedriver_win32/chromedriver.exe"

driver = webdriver.Chrome(PATH)
driver.get("https://www.instagram.com/")

# add_cookie
driver.add_cookie({
    'name': 'sessionid',
    'value': '1444456714%3A5GpeXdpsYybpDN%3A12%3AAYfaUmoQuW2XNNp4HMEF8ABQ1RFdYGkLidVJIG8x9A',
    'domain': '.instagram.com',
    'path': '/',
    'expiry': '2023-08-27T06:47:59.686Z',
    'secure': True,
    'httpOnly': True
})

# 3:13 休息

# 重新整理 等待 如果有取到某個值 就繼續下去
# 沒有就用登入的方式

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, '//*[@id="loginForm"]/div/div[3]'))
)


usernameInputElement = driver.find_element(By.NAME, 'username')
usernameInputElement.clear()
usernameInputElement.send_keys("fang_felipe")

passwordInputElement = driver.find_element(By.NAME, 'password')
passwordInputElement.clear()
passwordInputElement.send_keys("Dan112358")
loginButton = driver.find_element(
    By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
loginButton.click()


WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.CLASS_NAME, "cTBqC")
    )
)
searchElement = driver.find_element(By.CLASS_NAME, "cTBqC")
searchElement.click()
searchInputElement = driver.find_element(By.CLASS_NAME, "XTCLo")
searchInputElement.send_keys("新竹美食")

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div'))
)
searchInputElement.send_keys(Keys.RETURN)

# 換帳號
# 找美食 會想知道 價位 營業時間 地址


# csrftoken 不一樣

# 多出了
# sessionid = 1444456714%3AQgvBUk79yocH1W%3A26%3AAYexiiyA2ZoDW39g5fIFa4BN0oe6GQwYJLUupFllZg
# rur = 不一樣
# YqFNZLGmCg6zgci7VQ5bLixRssPNeS8z
'''
'dpr=1.5;
 ig_nrcb=1;
  mid=Ywm51wALAAGy5w0Kr1CqdAk7Xspm;
   csrftoken=YqFNZLGmCg6zgci7VQ5bLixRssPNeS8z;
    ds_user_id=1444456714'
'''
