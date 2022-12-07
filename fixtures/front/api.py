from fixtures.front.login.api import Login


class Front:
    def __init__(self, app):
        self.app = app
        self.Login = Login(self)
