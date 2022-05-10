from Base.base_component import component
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class login_form(component):
    EMAIL = '//input[@name="email"]'
    PASSWORD = '//input[@name="password"]'
    LOGIN_BUTTON = '//button[@class="button-white-small"]'


    def set_email(self,email):
        input = WebDriverWait(self.driver, self.TIMEOUT,self.CHECK_FREQ).until(
            lambda d: d.find_element(by=By.XPATH, value=self.EMAIL)
        )
        input.send_keys(email)

    def set_password(self, password):
        input = WebDriverWait(self.driver, self.TIMEOUT,self.CHECK_FREQ).until(
            lambda d: d.find_element(by=By.XPATH, value=self.PASSWORD)
        )
        input.send_keys(password)

    def login(self):
        button = WebDriverWait(self.driver, self.TIMEOUT,self.CHECK_FREQ).until(
            lambda d: d.find_element(by=By.XPATH, value=self.LOGIN_BUTTON)
        )
        button.click()

    

