from appium.webdriver.common.appiumby import AppiumBy

from pimsleur_test_files.pages.base_page import BasePage


class LibraryPage(BasePage):
    _choose_user_locator = (AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout"
                                            "/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                                            ".FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android"
                                            ".view.ViewGroup/android.view.ViewGroup["
                                            "2]/android.view.ViewGroup/android.widget.TextView")

    def choose_a_user_text(self):
        return self.driver.find_element(self._choose_user_locator).text
