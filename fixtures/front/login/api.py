import json
import random
from datetime import datetime

import requests
import cattrs
from common.deco import logging as log
from fixtures.front.login.model import PostSignInV1Response
from fixtures.utils import hash_password


class Login:
    def __init__(self, front):
        self.front = front

    LOGIN_V1 = 'ver1/Login'
    LOGIN = '/Login'

    @log('SignIn')
    def sign_in_v1(self, email: str, password: str, type_response=PostSignInV1Response):
        """
        Логин
        :param email: почта пользователя
        :param password: пароль пользователя
        :param type_response вид ответа от сервера
        :return: Response
        """
        headers = {'accept': 'text/plain', 'Content-Type': 'application/json'}
        data = {"login": email, "password": password}
        res = requests.post(f'{self.front.app.url}{self.LOGIN_V1}/SignIn', json=data, headers=headers)
        if 'error' not in res.text:
            res.data = cattrs.structure(res.json(), type_response)
        return res

    @log('Logout')
    def log_out_v1(self, token: str):
        """
        Логаут
        :param token: токен доступа
        :return: Response
        """
        headers = {'token': token, 'accept': '*/*'}
        res = requests.post(f'{self.front.app.url}{self.LOGIN_V1}/Logout', headers=headers)
        return res

    @log('SignUp')
    def sign_up_v1(self, email: str, password: str, user_name: str, type_response=PostSignInV1Response):
        """
        Регистрация нового юзера
        :param email: почта пользователя
        :param password: пароль пользователя
        :param type_response вид ответа от сервера
        :return: Response
        """
        # используется v1 запрос для получение токена без почты
        headers = {'accept': 'text/plain', 'Content-Type': 'application/json'}
        hashed_password = hash_password(password, email)
        data = {"email": email, "password": password, "userName": user_name}
        res = requests.post(f'{self.front.app.url}{self.LOGIN_V1}/SignUp', json=data, headers=headers)
        if 'error' not in res.text:
            res.data = cattrs.structure(res.json(), type_response)
        return res
