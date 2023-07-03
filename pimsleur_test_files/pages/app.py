from appium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from pimsleur_test_files.pages.login_page import LoginPage


class App:
    driver: WebDriver = None

    @classmethod
    def app_start(cls):
        caps = {
            "platformName": "Android",
            "appium:deviceName": "test",
            "appium:appPackage": "com.thoughtworks.pimsleur.unlimited.qa",
            "appium:appActivity": "com.pimsleur.MainActivity",
            "appium:newCommandTimeout": 6000,
            "appium:automationName": "UiAutomator2",
            "appium:ensureWebviewsHavePages": True,
            "appium:nativeWebScreenshot": True,
            "appium:connectHardwareKeyboard": True
        }
        cls.driver = webdriver.Remote("http://127.0.0.1:4723", caps)
        cls.driver.implicitly_wait(10)
        return LoginPage(cls.driver)

    @classmethod
    def quit(cls):
        cls.driver.quit()


