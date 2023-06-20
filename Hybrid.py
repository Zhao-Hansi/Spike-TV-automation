import datetime
from time import sleep

import pytest
import yaml
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestDemo:

    def setup(self):
        caps = {"platformName": "android",
                "deviceName": "111",
                "appPackage": "com.xueqiu.android",
                "appActivity": ".view.WelcomeActivityAlias",
                "autoGrantPermissions": True,
                # "appium:chromedriverExecutable": "/Users/seveniruby/projects/chromedriver/2.20/",
                "showChromedriverLog": True,
                "appium:automationName": "UiAutomator2",
                }

        self.driver = webdriver.Remote("http://localhost:4723", caps)
        self.driver.implicitly_wait(10)

    def test_webview(self):
        self.driver.find_element(by=AppiumBy.XPATH, value="//*[@text='交易']").click()
        for i in range(5):
            sleep(1)
            print(self.driver.contexts)

        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="A股开户").click()

    def test_webview_api_23(self):
        self.driver.find_element(by=AppiumBy.XPATH, value="//*[@text='交易']").click()
        for i in range(5):
            print(self.driver.contexts)

        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="A股开户").click()
        self.driver.switch_to.context(self.driver.contexts[1])
        print(self.driver.current_context)
        WebDriverWait(self.driver, 20) \
            .until(expected_conditions.visibility_of_element_located((By.ID, "phone-number")))
        self.driver.find_element(By.ID, "phone-number").send_keys("15600534760")
