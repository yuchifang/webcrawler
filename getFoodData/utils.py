from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


def waitUntil(webdirver, waitTime, ElementKey, ElementValue):
    element = WebDriverWait(webdirver, waitTime).until(
        EC.presence_of_element_located((ElementKey, ElementValue))
    )
    return element
