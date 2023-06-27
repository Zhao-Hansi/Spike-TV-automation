# This sample code uses the Appium python client v2
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

caps = {
        "platformName": "Android",
        "appium:deviceName": "xxx",
        "appium:appPackage": "tv.danmaku.bili",
        "appium:appActivity": ".MainActivityV2",
        "appium:newCommandTimeout": 6000,
        "appium:automationName": "UiAutomator2",
        "appium:ensureWebviewsHavePages": True,
        "appium:nativeWebScreenshot": True,
        "appium:connectHardwareKeyboard": True
        }

driver = webdriver.Remote("http://127.0.0.1:4723", caps)

driver.implicitly_wait(10)

el1 = driver.find_element(by=AppiumBy.ID, value="tv.danmaku.bili:id/agree")
el1.click()
el2 = driver.find_element(by=AppiumBy.ID, value="tv.danmaku.bili:id/tv_skip")
el2.click()
el4 = driver.find_element(by=AppiumBy.ID, value="tv.danmaku.bili:id/search_text")
el4.click()
el5 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Search query")
el5.send_keys("鬼灭之刃")
el6 = driver.find_element(by=AppiumBy.ID, value="tv.danmaku.bili:id/action_search")
el6.click()

driver.quit()