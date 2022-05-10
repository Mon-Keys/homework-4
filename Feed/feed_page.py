from Base.base_page import page
from Feed.feed_components import main_layout, feed_card


class feed_page(page):
    path = "feed"

    @property
    def feed_card(self):
        return feed_card(self.driver)

    @property
    def main_layout(self):
        return main_layout(self.driver)

    