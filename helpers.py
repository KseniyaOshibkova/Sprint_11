import random
import string

from data.data import Data


def random_email(domain="yandex.ru"):
    """Генерация уникального email"""
    return "test_" + "".join(random.choices(string.ascii_lowercase, k=8)) + f"@{domain}"


def get_user_data(email=None):
    """Возвращает данные пользователя с уникальным email, используя шаблон из Data"""
    email = email or random_email()
    return {
        "email": email,
        "password": Data.USER_PASSWORD,
        "submitPassword": Data.USER_SUBMIT_PASSWORD}
