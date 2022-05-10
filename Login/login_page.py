from Base.base_page import page
from Login.login_components import login_form


class login_page(page):
    PATH = "login"

    @property
    def form(self):
        return login_form(self.driver)

    def login(self, email, password):
        self.open()

        login_form = self.form
        login_form.set_email(email)
        login_form.set_password(password)
        login_form.login()