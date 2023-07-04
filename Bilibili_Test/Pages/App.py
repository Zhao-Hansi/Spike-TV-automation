from appium import webdriver

from Bilibili_Test.Pages.Recommended_Page import RecommendedPage


class App:
    driver: webdriver = None

    @classmethod
    def start(cls):
        caps = {
            "platformName": "Android",
            "appium:deviceName": "simulator",
            "appium:appPackage": "tv.danmaku.bili",
            "appium:appActivity": ".MainActivityV2",
            "appium:newCommandTimeout": 6000,
            "appium:automationName": "UiAutomator2",
            "appium:ensureWebviewsHavePages": True,
            "appium:nativeWebScreenshot": True,
            "appium:connectHardwareKeyboard": True
        }

        cls.driver = webdriver.Remote("http://127.0.0.1:4723", caps)
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

        return RecommendedPage(cls.driver)

    @classmethod
    def quit(cls):
        cls.driver.quit()
