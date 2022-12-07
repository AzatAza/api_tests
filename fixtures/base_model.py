import attr


@attr.s
class UserModel:
    token: str = attr.ib(default=None)
    uuid: int = attr.ib(default=None)
