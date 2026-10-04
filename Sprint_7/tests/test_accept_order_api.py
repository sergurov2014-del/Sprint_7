import allure
import helpers
import main as M


class TestAcceptOrderAPI:

    @allure.title(
        'Проверка принятия созданного заказа, с id заказа и курьера, Возвращение 201'
    )
    def test_accept_created_order_success_returns_201_and_ok_true(
        self, create_delete_courier
    ):
        courierId = create_delete_courier[2]  # из фикстуры получаем clientID
        order_id = helpers.return_order_id()
        response_accept_order = M.return_put_response_for_accept_order(
            order_id, courierId
        )  # принимаем заказ передвая туда id заказа и id созданного курьера
        assert response_accept_order.status_code == 200
        assert response_accept_order.text == '{"ok":true}'

    @allure.title(
        "Проверка  принятия созданного заказа, с некорректным номером заказа. Возвращение 404 ошибки"
    )
    def test_accept_created_order_incorrect_order_id(self, create_delete_courier):
        courierId = create_delete_courier[2]  # из фикстуры получаем clientID
        order_id = -666
        response_accept_order = M.return_put_response_for_accept_order(
            order_id, courierId
        )  # принимаем заказ передвая туда id заказа и id созданного курьера
        assert response_accept_order.status_code == 404
        assert (
            response_accept_order.text
            == '{"code":404,"message":"Заказа с таким id не существует"}'
        )

    @allure.title(
        "Проверка  принятия созданного заказа, с некорректным номером курьера. Возвращение 404 ошибки"
    )
    def test_accept_created_order_incorrect_courierid(self):
        courierId = -666
        order_id = helpers.return_order_id()
        response_accept_order = M.return_put_response_for_accept_order(
            order_id, courierId
        )  # принимаем заказ передвая туда id заказа и id созданного курьера
        assert response_accept_order.status_code == 404
        assert (
            response_accept_order.text
            == '{"code":404,"message":"Курьера с таким id не существует"}'
        )

    @allure.title(
        "Проверка  принятия созданного заказа,  без номера заказа. Возвращение 404 ошибки"
    )
    def test_accept_created_order_without_order_id(self, create_delete_courier):
        courierId = create_delete_courier[2]
        order_id = None
        response_accept_order = M.return_put_response_for_accept_order(
            order_id, courierId
        )
        assert response_accept_order.status_code == 400
        assert (
            response_accept_order.text
            == '{"code":400,"message":"Недостаточно данных для поиска"}'
        )

    @allure.title(
        "Проверка  принятия созданного заказа, без номера курьера. Возвращение 400 ошибки"
    )
    def test_accept_created_order_without_courierid(self, create_delete_courier):
        courierId = None
        order_id = helpers.return_order_id()
        response_accept_order = M.return_put_response_for_accept_order(
            order_id, courierId
        )  # принимаем заказ передвая туда id заказа и id созданного курьера
        assert response_accept_order.status_code == 400
        assert (
            response_accept_order.text
            == '{"code":400,"message":"Недостаточно данных для поиска"}'
        )
