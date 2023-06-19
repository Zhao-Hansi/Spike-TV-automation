# This sample code uses the Appium python client v2
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
import time
import pytest
import json
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

with open('locator.json', 'r') as f:
    data = json.load(f)


class TestTedTVApp:
    def setup(self):
        caps = {
            "platformName": "Android",
            "appium:deviceName": "xxx",
            "appium:appPackage": "com.ted.android.tv",
            "appium:appActivity": ".view.MainActivity",
            "appium:newCommandTimeout": 6000,
            "appium:automationName": "UiAutomator2",
            "appium:autoGrantPermissions": True,
            "appium:ensureWebviewsHavePages": True,
            "appium:nativeWebScreenshot": True,
            "appium:connectHardwareKeyboard": True
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723", caps)
        self.driver.implicitly_wait(15)

    def test_add_to_playlist(self):
        Feature_button = self.driver.find_element(by=AppiumBy.XPATH,
                                                  value="//androidx.recyclerview.widget.RecyclerView["
                                                        "@content-desc=\"Navigation menu\"]/android.widget.FrameLayout["
                                                        "1]/android.widget.FrameLayout/android.widget.CheckedTextView[2]")
        Feature_button.click()
        Episode_button = self.driver.find_element(by=AppiumBy.XPATH,
                                                  value="//androidx.recyclerview.widget.RecyclerView["
                                                        "@content-desc=\"Latest talks\"]/android.widget.FrameLayout["
                                                        "1]/android.widget.RelativeLayout/android.widget.LinearLayout"
                                                        "/android.widget.TextView[2]")
        Episode_button.click()
        episode_name = self.driver.find_element(by=AppiumBy.ID, value='com.ted.android.tv:id/detail_speaker').text
        Add_playlist = self.driver.find_element(by=AppiumBy.ID, value="com.ted.android.tv:id/my_list_image")
        Add_playlist.click()
        Add_playlist.click()
        self.driver.back()
        self.driver.back()
        My_play_button = self.driver.find_element(by=AppiumBy.XPATH, value='//androidx.recyclerview.widget'
                                                                           '.RecyclerView[@content-desc="Navigation '
                                                                           'menu"]/android.widget.FrameLayout['
                                                                           '4]/android.widget.FrameLayout/android.widget.CheckedTextView[2]')
        My_play_button.click()
        My_play_episode_name = self.driver.find_element(by=AppiumBy.ID, value="com.ted.android.tv:id/talk_speaker").text
        assert episode_name == My_play_episode_name

    def test_search_video(self):
        el4 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Search")
        el4.click()
        el5 = self.driver.find_element(by=AppiumBy.ID, value="com.ted.android.tv:id/lb_search_text_editor")
        el5.send_keys("apple")
        el6 = self.driver.find_element(by=AppiumBy.XPATH, value="//androidx.recyclerview.widget.RecyclerView["
                                                                "@content-desc=\"Talks\"]/android.widget.FrameLayout["
                                                                "1]/android.widget.RelativeLayout/android.widget.ImageView")
        el6.click()

    def teardown(self):
        self.driver.quit()
