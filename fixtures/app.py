from fixtures.front.api import Front


class App:
    def __init__(self, url, url_pub):
        self.url = url
        self.url_pub = url_pub
        self.front = Front(self)
