from urllib.parse import urljoin


class page:
    BASE_URL = "https://drip.monkeys.team/"
    PATH = ""

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        url = urljoin(self.BASE_URL, self.PATH)
        self.driver.get(url)
        self.driver.maximize_window()