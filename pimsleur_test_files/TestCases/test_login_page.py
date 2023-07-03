from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import WebDriver

from pimsleur_test_files.pages.app import App

from pimsleur_test_files.pages.login_page import LoginPage


class TestLoginPage:

    def setup(self):
        self.login_page = App.app_start()

    def test_login_successful(self):
        library_page = self.login_page.login('toc@tw.com', 'Pims9999')
        self.choose_user_test = library_page.choose_a_user_text()
        assert self.choose_user_test == 'Choose a User'

    def teardown(self):
        App.quit()
