import allure
import pytest
import helpers
import data as D


class TestAcceptOrderAPI:

    @allure.title(
        'Проверка создания возвращения созданного заказа. Возвращение 201 и {"ok":true}'
    )
    def test_accept_created_order_success_returns_201_and_ok_true(self, create_delete_courier):
        courierId = create_delete_courier[2]  # из фикстуры получаем clientID
        order_id=helpers.return_order_id()
        response_accept_order = (
            helpers.return_put_response_for_accept_order(
                order_id, courierId
            ) #принимаем заказ передвая туда id заказа и id созданного курьера
        )
        assert response_accept_order.status_code == 200
        assert response_accept_order.text == '{"ok":true}'

    
    
    def test_accept_created_order_incorrect_order_id(self, create_delete_courier):
        courierId = create_delete_courier[2]  # из фикстуры получаем clientID
        order_id=-666
        response_accept_order = (
                    helpers.return_put_response_for_accept_order(
                        order_id, courierId
                    ) #принимаем заказ передвая туда id заказа и id созданного курьера
                )
        assert response_accept_order.status_code == 404 
        assert response_accept_order.text == '{"code":404,"message":"Заказа с таким id не существует"}' 
    
"""    def test_accept_created_order_incorrect_courierid(self):
        courierId=-666
        order_id=helpers.return_order_id()
        response_accept_order = (
                    helpers.return_put_response_for_accept_order(
                        order_id, courierId
                    ) #принимаем заказ передвая туда id заказа и id созданного курьера
                )
        assert response_accept_order.status_code == 404
        assert response_accept_order.text == '{"code":404,"message":"Заказа с таким id не существует"}' 
    

        
    def test_accept_created_order_without_courierid(self, create_delete_courier):
        pass"""

    

"""Принять заказ
Проверь:
успешный запрос возвращает{"ok":true}; +
если не передать id курьера, запрос вернёт ошибку;
если передать неверный id курьера, запрос вернёт ошибку;
если не передать id заказа, запрос вернёт ошибку;
если передать неверный id заказа, запрос вернёт ошибку.

def test_accept_created_order_without_order_id(self, create_delete_courier):
        courierId = create_delete_courier[2]
        response_accept_order = (
                    helpers.return_put_response_for_accept_order(
                        None, courierId
                    ) #принимаем заказ передвая туда id заказа и id созданного курьера
                )
        assert response_accept_order.status_code == 400
        assert response_accept_order.text == '{"ok":true}'

        print(f"--- ОТЛАДКА ---")
        print(courierId)
        print(track_number)
        print(response_order.json()["order"])
        print(order_id)
    #    print(f"Статус создания: {response_accept_order}")
    #    print(f"Статус создания: {response_accept_order.status_code}")
        print(f"Статус создания: {response_make_order.text}")"""
