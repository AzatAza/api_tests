import hashlib
import random
from decimal import Decimal
from fixtures import app
from fixtures.constants import COMPLETED, COMMENT


def get_total_amount(data):
    """
    Функция расчета суммы количества(amount)
    :return float
    """
    total = 0
    total = sum([total + trans['amount'] for trans in data])
    total = Decimal(f'{total}')  # Округление
    total = float(total.quantize(Decimal(f'{data[0]["amount"]}')))
    return total


def expected_statuses(data):
    """
    Функция создания ожидаемых данных
    :return dict
    """
    statuses = {'status': COMPLETED,
                'count': len(payment_data),
                'total': get_total(data)
                }
    return statuses


def calc_diff(funds_before, funds_after) -> list:
    """
    Расчет разницы до и после
    :return: list
    """
    result = []
    for before, after in zip(funds_before, funds_after):
        res = round(abs(before - after), 6)
        result.append(res)
    return result


def get_user_id(app, user, user_params):
    user_id = None
    users_list = app.front.get_users_id(user)
    for user in users_list.data.users:
        if user['userName'] == user_params.user_name:
            user_id = user['id']
    return user_id


def get_num(nums_list, existing=False, next_num=False) -> str:
    """
    Метод получает список доступных параметров
    :param nums_list: список доступных номеров
    :param existing: истино если надо получить существующий номер
    :param next_num: истино если надо получить следующий порядковый номер
    """
    start_num = 1
    last_num = 0
    for curr in nums_list:
        if 'TEST' in curr['symbol']:
            if last_num < int(curr['name'].split(' ')[2]):
                last_num = int(curr['name'].split(' ')[2])

    if next_num and not existing:
        if not last_num:
            last_num = start_num
        else:
            last_num += 1
        return str(last_num).zfill(3)

    elif not next_num and existing:
        return str(last_num).zfill(3)

    elif not next_num and not existing:
        raise AttributeError("Один из параметров должен быть истинным")

    elif next_num and existing:
        raise AttributeError("Один из параметров должен быть ложным")
