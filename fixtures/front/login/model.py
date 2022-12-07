import attr


@attr.s
class PostSignInV1Response:
    accToken: str = attr.ib(validator=attr.validators.instance_of(str))
    refToken: str = attr.ib(validator=attr.validators.instance_of(str))


