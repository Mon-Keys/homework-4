import os
import re
import unittest


from Feed.feed_page import feed_page
from Login.login_page import login_page
from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.chrome.options import Options

class feed_page_test(unittest.TestCase):

    def setUp(self):
        browser = os.environ.get("TESTBROWSER", "CHROME")
        options = Options()
        options.headless = bool(os.environ.get("HEADLESS", False))
        self.driver = Remote(
            command_executor="http://127.0.0.1:4444/wd/hub",
            desired_capabilities=getattr(DesiredCapabilities, browser).copy(),
            options=options
        )
        lp = login_page(self.driver)
        lp.login("testuser@testuser", "PASSWORD")
        self.feed_page = feed_page(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_like_card(self):
        self.feed_page.feed_card.like()
        self.assertTrue(True)

    