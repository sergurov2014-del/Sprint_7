import random
import string
from urls import BASE_URL
import data as D
import main as M


def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = "".join(random.choice(letters) for i in range(length))
    return random_string


def generate_payloads_with_login_null():
    payloads_with_login_null = {
        "login": None,
        "password": generate_random_string(10),
        "firstName": generate_random_string(10),
    }
    return payloads_with_login_null


def generate_payloads_with_password_null():
    payloads_with_password_null = {
        "login": generate_random_string(10),
        "password": None,
        "firstName": generate_random_string(10),
    }
    return payloads_with_password_null


def new_courier_data():

    # собираем тело запроса
    payload = {
        "login": generate_random_string(10),
        "password": generate_random_string(10),
        "firstName": generate_random_string(10),
    }
    return payload


def return_some_order():
    some_order = {
        "firstName": generate_random_string(5),
        "lastName": generate_random_string(5),
        "address": generate_random_string(5) + "," + generate_random_string(4),
        "metroStation": random.choice(D.station_list),
        "phone": f"+7{random.randint (1000000000, 9999999999)}",
        "rentTime": random.randint(1, 20),
        "deliveryDate": "2026-06-26",
        "comment": generate_random_string(20),
        "color": [],
    }
    return some_order


def return_order_id():
    payloads = return_some_order()  # получаем рандомный словарь с данными для заказа
    # создаём заказ с рандомными данными
    response_make_order = M.return_post_response_for_make_order(payloads)
    track_number = response_make_order.json()["track"]
    # запрос на получерие заказ по его номеру
    response_order = M.return_get_response_for_get_order_with_track_number(track_number)
    # вытягиваем id заказа, чтобы передать его в принятие заказа
    order_id = response_order.json()["order"]["id"]
    return order_id
