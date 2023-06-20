from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By


class TestWeb:

    def setup(self):
        caps = {"browserName": "chrome",
                "deviceName": "hogwarts",
                "platformName": "android",
                # "chromedriverExecutable": "/Users/seveniruby/projects/chromedriver/2.34/chromedriver",
                "showChromedriverLog": True
                }

        self.driver = webdriver.Remote("http://localhost:4723", caps)
        self.driver.implicitly_wait(10)

    def test_testerHome_search(self):
        self.driver.get("https://testerhome.com")
        self.driver.switch_to.context("NATIVE_APP")
        self.driver.find_element(by=AppiumBy.ID, value="com.android.chrome:id/button_secondary").click()
        self.driver.switch_to.context(self.driver.contexts[1])
        print(self.driver.current_context)
        print(self.driver.page_source)

        self.driver.find_element(By.CSS_SELECTOR, "#mobile-search-form > input").send_keys("hogwarts")
