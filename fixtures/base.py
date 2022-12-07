import hashlib
import hmac
import json


class BaseClass(object):
    def to_dict(self) -> dict:
        """
        Convert nested object to dict
        :return: dict
        """
        return json.loads(json.dumps(self, default=lambda o: o.__dict__))

    @staticmethod
    def hashing(signature, query_string=""):
        return 'hashing'

    @staticmethod
    def hash_password(pas: str, email: str) -> str:
        return 'hash_password'
