from requests_toolbelt.multipart.encoder import MultipartEncoder
import allure
from api.url import Urls


class AdvertsApi:
    def __init__(self, client):
        self.client = client

    @allure.step("Создание объявления")
    def create_advert(self, advert_data, auth_token):
        m = MultipartEncoder(fields=advert_data)
        headers = {
            "Authorization": auth_token,
            "Content-Type": m.content_type}
        return self.client.post(Urls.ADD_ADVERT_URL, data=m, headers=headers)


    @allure.step("Редактирование объявления")
    def edit_advert(self, advert_id, new_data, auth_token):
        m = MultipartEncoder(fields=new_data)
        headers = {
            "Authorization": auth_token,
            "Content-Type": m.content_type}
        return self.client.patch(f"{Urls.EDIT_ADVERT_URL}{advert_id}", data=m, headers=headers)


    @allure.step("Удаление объявления")
    def delete_advert(self, advert_id, auth_token):
        headers = {"Authorization": auth_token}
        return self.client.delete(f"{Urls.DELETE_ADVERT_URL}{advert_id}", headers=headers)
