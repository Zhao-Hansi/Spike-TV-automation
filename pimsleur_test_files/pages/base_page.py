from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from appium import webdriver


class BasePage:
    _black_list = [
        (AppiumBy.ID, "image_cancel"),
        (AppiumBy.ID, "tips")
    ]

    def __init__(self, driver: webdriver):
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

    def swipe_one_button_to_another_button(self, start_element, end_element):
        action = TouchAction(self.driver)
        start_location = start_element.location
        start_x = start_location['x']
        start_y = start_location['y']
        end_location = end_element.location
        end_x = end_location['x']
        end_y = end_location['y']
        action.press(x=start_x, y=start_y).move_to(x=end_x, y=end_y).release().perform()

    def swipe_from_current_to_button(self, target_element):
        action = TouchAction(self.driver)
        action.move_to(target_element).release().perform()

    def swipe_random_up_distance(self):
        action = TouchAction(self.driver)
        screen_size = self.driver.get_window_size()
        screen_width = screen_size['width']
        screen_height = screen_size['height']
        start_x = screen_width // 2
        start_y = screen_height // 2
        end_x = start_x
        end_y = start_y - 200
        action.press(x=start_x, y=start_y).move_to(x=end_x, y=end_y).release().perform()

    def swipe_random_down_distance(self):
        action = TouchAction(self.driver)
        screen_size = self.driver.get_window_size()
        screen_width = screen_size['width']
        screen_height = screen_size['height']
        start_x = screen_width // 2
        start_y = screen_height // 2
        end_x = start_x
        end_y = start_y + 200
        print(screen_size, start_x, start_y, end_x, end_y)
        action.press(x=start_x, y=start_y).move_to(x=end_x, y=end_y).release().perform()

    def swipe_screen_until_to_element(self, locator):
        while True:
            try:
                self.driver.find_element(*locator)
                break
            except NoSuchElementException:
                self.swipe_random_down_distance()

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
