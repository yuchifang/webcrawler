# 寫個網路爬蟲的程式 爬 特定的 地區
import pathlib
import platform
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
import data
from utils import waitUntil
from login import login
from selenium.webdriver.common.by import By
'''
find
龍山寺 江子翠 新埔 板橋 亞東 海山 土城 

板新 中原 橋和 中和

新埔民生 幸福 頭前庄 新莊 先嗇宮

2022 12 11  2023
check 最新貼文

end 2021 stop
'''


currentFolderPath = pathlib.Path(__file__).parent.resolve()
MY_OS = platform.system()
if MY_OS == "Linux":
    path = str(currentFolderPath) + '/chromedriver_linux64/chromedriver'
else:
    path = str(currentFolderPath) + '\chromedriver_win32\chromedriver.exe'

service = ChromeService(executable_path=path)


driver = webdriver.Chrome(service=service)
driver.get("https://www.facebook.com/groups/1834309463450416/")

# 登入 getCookie 記錄 取得 cookie setCookie

# driver.add_cookie({
#     'domain': '.facebook.com',
#     'path': '/',
#     'name': data.name,
#     'expiry':data.expiry,
#     'httpOnly':True,
#     'sameSite' : 'None',
#     'secure':True,
#     'value' : 'Dqm_Y_abGbv95WgwG79opi7B'
# })

# driver.refresh()

goLoginInButton = waitUntil(driver,10,By.ID, 'login_form')
goLoginInButton.click()

waitUntil(driver, 10, By.CLASS_NAME, '_9axz')
login(driver)
# 找到一則貼文
# 找裡面有沒有 關鍵字
# x1cy8zhl x78zum5 x1q0g3np xod5an3 x1pi30zi x1swvt13 xz9dl7a
# x1cy8zhl x78zum5 x1q0g3np xod5an3 x1pi30zi x1swvt13 xz9dl7a
postElement = driver.find_element(By.CLASS_NAME, 'x1cy8zhl x78zum5 x1q0g3np xod5an3 x1pi30zi x1swvt13 xz9dl7a')

'''
    find 2021 
        end
    find 求租
        delete
    find 2022 12 11  2023
        and 
            龍山寺 江子翠 新埔 板橋 亞東 海山 土城 
            板新 中原 橋和 中和
            新埔民生 幸福 頭前庄 新莊 先嗇宮
        add save
        delet

    
'''