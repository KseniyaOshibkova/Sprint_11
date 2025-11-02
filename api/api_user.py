import allure

from api.url import Urls


class UserApi:
    def __init__(self, client):
        self.client = client

    @allure.step('Создание нового пользователя')
    def create_user(self, user_data):    #добавить данные для создания пользователя
        """Создание пользователя"""
        return self.client.post(Urls.CREATE_USER_URL, json=user_data)

    @allure.step('Авторизация пользователя')
    def login_user(self, creds):   #данные для логина
        """Логин пользователя в системе"""
        return self.client.post(Urls.LOGIN_USER_URL, json=creds)
