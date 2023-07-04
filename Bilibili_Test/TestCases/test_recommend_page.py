from time import sleep

from Bilibili_Test.Pages.App import App


class TestLoginPage:

    def setup(self):
        self.login_page = App.start()

    def test(self):
        # self.login_page.click_items_button()
        sleep(7)
        self.login_page.swipe_random_down_distance()
        sleep(3)


    def teardown(self):
        App.quit()