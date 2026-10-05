import allure
import pytest
import helpers
import data as D
import api_methods as M


class TestOrderApi:
    @pytest.mark.parametrize(
        "allure_title, scooter_color",
        [
            ("Проверка создания заказа самоката: без цвета ", []),
            (
                "Проверка создания заказа самоката: цвет BLACK",
                ["BLACK"],
            ),
            (
                "Проверка создания заказа самоката: цвет GREY",
                ["GREY"],
            ),
            (
                "Проверка создания заказа самоката: оба цвета BLACK+GREY",
                ["BLACK", "GREY"],
            ),
        ],
    )
    def test_make_order_with_correct_data(self, allure_title, scooter_color):
        allure.dynamic.title(allure_title)
        payloads = helpers.return_some_order()
        payloads["color"] = scooter_color
        response = M.post_response_for_make_order(payloads)

        assert response.status_code == 201
        assert "track" in response.text

    @allure.title("Проверка получения списка заказов: структура и наличие данных")
    def test_get_orders_list_returns_valid_structure(self):

        response = M.get_response_for_get_order()
        assert response.status_code == 200  # Проверяем статус 200
        data = response.json()  # Парсим JSON
        assert "orders" in data, "В ответе отсутствует ключ 'orders'"
        # Значение по ключу "orders" — это СПИСОК (а не словарь, строка или None)

        assert isinstance(
            data["orders"], list
        ), "Поле 'orders' должно быть списком (массивом)"
        # Список не пустой (в нем есть хотя бы один заказ) =>API реально отдает данные, а не пустой массив []
        assert (
            len(data["orders"]) > 0
        ), "Список заказов пуст, хотя должен содержать элементы"
        # Берем ПЕРВЫЙ заказ из списка и проверяем его структуру
        first_order = data["orders"][0]

        required_fields = [
            "id",
            "courierId",
            "firstName",
            "lastName",
            "address",
            "metroStation",
            "phone",
            "rentTime",
            "deliveryDate",
            "track",
            "color",
            "comment",
            "createdAt",
            "updatedAt",
            "status",
        ]  # Проверяем, что у первого заказа есть обязательные поля

        for field in required_fields:
            assert (
                field in first_order
            ), f"В заказе отсутствует обязательное поле '{field}'"

        assert isinstance(first_order["track"], int), "Поле 'track' должно быть числом"
