import data as D
import allure
import helpers
from urls import BASE_URL
import requests


class TestGetOrder:

    @allure.title("Проверка успешного возвращения созданного заказа. ")
    def test_get_created_order_success_returns_200(self):
        payloads = D.some_order
        response = helpers.return_post_response_for_make_order(payloads)  # создаём заказ с рандомными данными
        track_number = response.json()["track"]
        send_order_text = response.json()

        get_order_response = helpers.return_get_response_for_get_order(track_number)
        data = get_order_response.json()
        assert get_order_response.status_code == 200  # проверяем 200 код
        assert (
            data["order"]["track"]
            and data["order"]["id"]
            and data["order"]["firstName"]
            and data["order"]["lastName"]
            and data["order"]["address"]
            and data["order"]["metroStation"]
            and data["order"]["phone"]
            and data["order"]["rentTime"]
            and data["order"]["deliveryDate"]
        )  # проверяем "обязательные"-нифига они не обязательные по факту поля

    @allure.title("Проверка удаления несуществующего курьера.")
    def test_delete_nonexistent_courier_returns_404(
        self,
    ):
        delete_response = requests.delete(
            f"{BASE_URL}/courier/{999999999}"
        )  # ОЧИСТКА Удаляем курьера по несуществующему id

        assert delete_response.status_code == 404
