from Base.base_component import component
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class feed_card(component):
    LIKEBUTTON = '//img[@alt="like"]'
    DISLIKEBUTTON = '//img[@alt="dislike"]'
    EXPANDBUTTON = '//img[@alt="expand"]'


    def like(self):
        likebutton = WebDriverWait(self.driver, self.TIMEOUT, self.CHECK_FREQ).until(
            lambda d: d.find_element(by=By.XPATH, value=self.LIKEBUTTON)
        )
        likebutton.click()
        WebDriverWait(self.driver, self.TIMEOUT,self.CHECK_FREQ).until(
            lambda d: len(d.find_elements(by=By.XPATH, value=main_layout.LAY_CHILDREN)) == 0
        )

    def dislike(self):
        likebutton = WebDriverWait(self.driver, self.TIMEOUT,self.CHECK_FREQ).until(
            lambda d: d.find_element(by=By.XPATH, value=self.DISLIKEBUTTON)
        )
        likebutton.click()
        WebDriverWait(self.driver, self.TIMEOUT,self.CHECK_FREQ).until(
            lambda d: len(d.find_elements(by=By.XPATH, value=main_layout.LAY_CHILDREN)) == 0
    )

    def expand(self):
        likebutton = WebDriverWait(self.driver, self.TIMEOUT,self.CHECK_FREQ).until(
            lambda d: d.find_element(by=By.XPATH, value=self.EXPANDBUTTON)
        )
        likebutton.click()
        WebDriverWait(self.driver, self.TIMEOUT,self.CHECK_FREQ).until(
            lambda d: len(d.find_elements(by=By.XPATH, value=main_layout.LAY_CHILDREN)) == 0
    )

class main_layout(component):
    LAY = '//div[@class="main-layout__content"]'
    LAY_CHILDREN = LAY + "/*"
    NOT_FOUND = '//div[@class="search__content__not-found"]'

    def has_no_content(self):
        return len(self.driver.find_elements(by=By.XPATH, value=self.LAY_CHILDREN)) == 0

    def not_found(self):
        return len(self.driver.find_elements(by=By.XPATH, value=self.NOT_FOUND)) == 1
