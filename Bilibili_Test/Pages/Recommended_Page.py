from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

from Bilibili_Test.Pages.Base_Page import BasePage


class RecommendedPage(BasePage):
    _user_items_locator = (AppiumBy.ID, "tv.danmaku.bili:id/agree")
    _recommend_text_locator = (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="推荐,6之2,'
                                               '标签"]/android.widget.TextView')

    def click_items_button(self):
        self.driver.find_element_and_click(self._user_items_locator)


