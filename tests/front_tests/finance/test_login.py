import copy
from time import sleep

import allure
import pytest

from fixtures.constants import OK


class TestPositive:
    @pytest.mark.p0
    @pytest.mark.frontend
    def test_add_user_data(self, app, user):
        """
        Цель: Проверить добавления новые данные юзера
            1. Добавить новые данные юзера
            2. Проверить, что новые данные добавлены
        Приоритет: Medium
        """
        with allure.step('Добавляем новые данные юзера'):
            res = app.login.add_new_user_data(token=user.token, data=data)
            with allure.step('Подтверждаем добавление'):
                res2 = app.login.confirm_new_user_data(token=user.token)
                assert 'error' not in res2.text, f'status code:{res2.status_code}, text: {res2.text}'

            res3 = app.login.get_user_data(
                token=user.token,
                fields=[
                    f'Name',
                    f'Age',
                    f'Wight',
                ])
            assert 'error' not in res3.text, f'status_code: {res.status_code}, text: {res.text}'

        with allure.step('Проверяем корректность обновленных данных'):
            user_data = app.login.get_all_user_data(user.token)
            check_user_data_correct(user_data, new_user_data_list)


@pytest.mark.p2
@pytest.mark.frontend
@pytest.mark.parametrize('new_name', [1111, '#$@%', ' '])
class TestNegative:
    def test_add_user_with_incorrect_data(self, app, user, new_name):
        """
        Цель: Проверить невозможность добавления юзера с некорректными данными
            1. Добавить нового юзера с ником {}
            2. Убедиться, что юзер с некорректным ником не добавлен
        Приоритет: Medium
        """.format(new_name)

        with allure.step(f'Добавляем нового юзера с ником {new_name}'):
            res = app.login.add_new_user(name=new_name, password='hashed_password')
            assert 'error' in res.text, f'status code:{res.status_code}, text: {res.text}'

        with allure.step('Проверяем, что новый юзер не добавлен'):
            res2 = app.login.get_all_users(user.token)
            check_user_doesnt_exists(res2, user)
