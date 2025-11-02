import allure
from data.data import Data
from helpers import get_user_data

class TestUser:

    @allure.title("Успешная регистрация нового пользователя с уникальным email")
    def test_successful_registration(self, user_api):
        user_data = get_user_data()
        response = user_api.create_user(user_data)

        assert response.status_code == 201
        assert response.json()["user"]["email"] == user_data["email"]


    @allure.title("Повторная регистрация пользователя с уже существующим email")
    def test_registration_existing_email(self, user_api):
        user_data = get_user_data()
        user_api.create_user(user_data)  # первая регистрация

        response = user_api.create_user(user_data)  # повторная
        assert response.status_code == 400
        assert response.json().get("message") == Data.MESSAGE_CREATE_SAME_COURIER


    @allure.title("Успешная авторизация ранее зарегистрированного пользователя")
    def test_login_user(self, user_api):
        user_data = get_user_data()
        user_api.create_user(user_data)

        login_resp = user_api.login_user({"email": user_data["email"], "password": user_data["password"]})
        assert login_resp.status_code == 201

        token = login_resp.json()["token"]["access_token"]
        assert token is not None
