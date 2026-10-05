import api_methods as M
import allure
import helpers
from urls import BASE_URL


class TestGetOrder:

    @allure.title("Проверка успешного возвращения созданного заказа. ")
    def test_get_created_order_success_returns_200(self):
        payloads = helpers.return_some_order()
        response = M.return_post_response_for_make_order(
            payloads
        )  # создаём заказ с рандомными данными
        track_number = response.json()["track"]
        send_order_text = response.json()

        get_order_response = M.get_response_for_get_order_with_track_number(
            track_number
        )
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

    @allure.title("Проверка - Запрос без номера заказа возвращает 400 ошибку")
    def test_get_order_without_order_numder_returns_404(
        self,
    ):
        get_order_response = M.get_response_for_get_order_with_track_number("")
        assert get_order_response.status_code == 400
        assert (
            get_order_response.text
            == '{"code":400,"message":"Недостаточно данных для поиска"}'
        )

    @allure.title("Проверка - запрос с несуществующим заказом возвращает 404 ошибку.")
    def test_get_created_order_without_order_numder_returns_404(
        self,
    ):
        get_order_response = M.get_response_for_get_order_with_track_number(
            9999999
        )

        assert get_order_response.status_code == 404
        assert get_order_response.text == '{"code":404,"message":"Заказ не найден"}'
