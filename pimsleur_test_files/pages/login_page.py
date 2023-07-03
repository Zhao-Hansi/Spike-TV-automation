from time import sleep

from appium.webdriver.common.appiumby import AppiumBy

from pimsleur_test_files.pages.base_page import BasePage
from pimsleur_test_files.pages.forget_password_page import ForgetPasswordPage
from pimsleur_test_files.pages.library_page import LibraryPage


class LoginPage(BasePage):
    _login_button_locator = (AppiumBy.ACCESSIBILITY_ID, "signIn")
    _email_input_locator = (AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout"
                                            "/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                                            ".FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android"
                                            ".view.ViewGroup/android.view.ViewGroup["
                                            "1]/android.widget.ScrollView/android.view.ViewGroup/android.widget"
                                            ".EditText[1]")
    _password_input_locator = (AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout"
                                               "/android.widget.FrameLayout/android.widget.LinearLayout/android"
                                               ".widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup"
                                               "/android.view.ViewGroup/android.view.ViewGroup["
                                               "1]/android.widget.ScrollView/android.view.ViewGroup/android.widget"
                                               ".EditText[2]")
    _signIn_button_locator = (AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout"
                                              "/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                                              ".FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android"
                                              ".view.ViewGroup/android.view.ViewGroup["
                                              "1]/android.widget.ScrollView/android.view.ViewGroup/android.view"
                                              ".ViewGroup[4]/android.widget.TextView")
    _forget_password_locator = (AppiumBy.XPATH,
                                "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                                ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget"
                                ".FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup["
                                "1]/android.widget.ScrollView/android.view.ViewGroup/android.widget.TextView[2]")

    def login(self, username, password):
        self.find_element_and_click(self._login_button_locator)
        self.find_element(self._email_input_locator).send_keys(username)
        self.find_element(self._password_input_locator).send_keys(password)
        sleep(5)
        self.driver.find_element(self._signIn_button_locator).click()
        return LibraryPage(self.driver)

    def enter_forget_password_page(self):
        self.find_element_and_click(self._forget_password_locator)
        return ForgetPasswordPage(self.driver)
