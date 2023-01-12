from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement

def waitUntil(webdirver, waitTime, ElementKey, ElementValue) -> WebElement:
    element = WebDriverWait(webdirver, waitTime).until(
        EC.presence_of_element_located((ElementKey, ElementValue))
    )
    return element
