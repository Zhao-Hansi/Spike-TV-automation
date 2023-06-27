import datetime

from appium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from Demo.page.main_page import MainPage


class App:
    driver: WebDriver = None

    @classmethod
    def start(cls):
        caps = {"platformName": "android",
                "deviceName": "seveniruby",
                "appPackage": "com.xueqiu.android",
                "appActivity": ".view.WelcomeActivityAlias",
                "autoGrantPermissions": "true",
                "chromedriverExecutable": "/Users/seveniruby/projects/chromedriver/2.20/chromedriver",
                "showChromedriverLog": True
                }
        # caps["udid"] = "emulator-5556"

        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        cls.driver.implicitly_wait(10)

        # sleep(20)
        # if len(self.driver.find_elements_by_id("image_cancel")) >=1:
        #     self.driver.find_element_by_id("image_cancel").click()
        #
        #

        # WebDriverWait(self.driver, 15).until(
        #     expected_conditions.visibility_of_element_located((By.ID, "image_cancel"))
        # )

        # def loaded(driver):
        #     print(datetime.datetime.now())
        #     if len(cls.driver.find_elements_by_id("image_cancel")) >=1:
        #         cls.driver.find_element_by_id("image_cancel").click()
        #         return True
        #     else:
        #         return False
        #
        # try:
        #     WebDriverWait(cls.driver, 20).until(loaded)
        # except:
        #     print("no update")

        return MainPage(cls.driver)

    @classmethod
    def quit(cls):
        cls.driver.quit()
