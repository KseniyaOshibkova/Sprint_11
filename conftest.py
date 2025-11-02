import allure
import pytest

import helpers
from api.api_adverts import AdvertsApi
from api.api_client import ClientApi
from api.api_user import UserApi
from data.data import Data


@pytest.fixture
def client():
    return ClientApi()

@pytest.fixture
def user_api(client):
    return UserApi(client)

@pytest.fixture
def adverts_api():
    client = ClientApi()
    return AdvertsApi(client)


@pytest.fixture
@allure.step("Регистрация и авторизация пользователя, получение токена")
def get_auth_token(user_api):
    user_data = helpers.get_user_data()

    with allure.step("Регистрация нового пользователя"):
        create_resp = user_api.create_user(user_data)
        assert create_resp.status_code == 201, f"Ошибка при создании пользователя: {create_resp.text}"

    with allure.step("Авторизация пользователя"):
        login_resp = user_api.login_user({"email": user_data["email"], "password": user_data["password"]})
        assert login_resp.status_code == 201, f"Ошибка при авторизации: {login_resp.text}"

    with allure.step("Получение Bearer-токена"):
        login_json = login_resp.json()
        access_token = login_json["token"]["access_token"]
        bearer_token = f"Bearer {access_token}"

    return bearer_token
