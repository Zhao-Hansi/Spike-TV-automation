from pimsleur_test_files.pages.app import App


class TestLoginPage:

    def setup(self):
        self.login_page = App.app_start()

    def test_login_successful(self):
        library_page = self.login_page.login()
        self.choose_user_test = library_page.choose_a_user_text()
        assert self.choose_user_test == 'Choose a User'

    def test_login_page(self):
        assert self.login_page.signIn_button_text() == "sign in with Email"

    def teardown(self):
        App.quit()
