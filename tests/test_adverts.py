import allure
from data.data import Data


class TestAdverts:

    @allure.title("Создание объявления в любой категории")
    def test_create_advert(self, adverts_api, get_auth_token):
        advert_data = Data.TEST1.copy()
        response = adverts_api.create_advert(advert_data, get_auth_token)

        assert response.status_code == 201
        assert response.json().get("name") == advert_data["name"]


    @allure.title("Успешное редактирование любого поля объявления")
    def test_edit_advert(self, adverts_api, get_auth_token):
        advert_data = Data.TEST1.copy()
        create_resp = adverts_api.create_advert(advert_data, get_auth_token)
        advert_id = create_resp.json()["id"]

        new_data = Data.TEST2.copy()
        edit_resp = adverts_api.edit_advert(advert_id, new_data, get_auth_token)

        assert edit_resp.status_code == 200
        assert edit_resp.json().get("name") == new_data["name"]


    @allure.title("Редактирование объявления, созданного не тем пользователем")
    def test_edit_advert_different_user(self, adverts_api, get_auth_token):
        advert_id = "2222"
        new_data = Data.TEST2.copy()
        edit_resp = adverts_api.edit_advert(advert_id, new_data, get_auth_token)

        assert edit_resp.status_code == 401
        assert edit_resp.json().get("message") == Data.MESSAGE_EDIT_DIFFERENT_USER_ADVERT


    @allure.title("Успешное удаление объявления")
    def test_delete_advert(self, adverts_api, get_auth_token):
        advert_data = Data.TEST2.copy()
        create_resp = adverts_api.create_advert(advert_data, get_auth_token)
        advert_id = create_resp.json()["id"]

        delete_resp = adverts_api.delete_advert(advert_id, get_auth_token)

        assert delete_resp.status_code == 200
        assert delete_resp.json().get("message") == Data.MESSAGE_DELETE_ADVERT
