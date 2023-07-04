from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    _black_list = [
        (AppiumBy.ID, "image_cancel"),
        (AppiumBy.ID, "tips")
    ]

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find_element(self, locator):
        print(locator)
        try:
            return self.driver.find_element(*locator)
        except:
            self.handle_exception()
            return self.driver.find_element(*locator)

    def find_element_and_click(self, locator):
        print("click")
        try:
            self.find_element(locator).click()
        except:
            self.handle_exception()
            self.find_element(locator).click()

    def handle_exception(self):
        print(":exception")
        self.driver.implicitly_wait(0)
        for locator in self._black_list:
            print(locator)
            elements = self.driver.find_elements(*locator)

            if len(elements) >= 1:
                # todo: 不是所有的弹框处理都是要点击弹框，可根据业务需要自行封装
                elements[0].click()
            else:
                print("%s not found" % str(locator))

            # todo: 私用page source会更快的定位

            # page_source=self.driver.page_source
            # if "image_cancel" in page_source:
            #     self.driver.find_element(*locator).click()
            # elif "tips" in page_source:
            #     pass

        self.driver.implicitly_wait(10)
