import requests
from urls import BASE_URL


def post_response_for_create(
    payload,
):  # метод для создания запроса на регистрацию курьера
    response = requests.post(
        f"{BASE_URL}/courier",
        json=payload,
        headers={"Content-Type": "application/json"},
    )
    return response


def post_response_for_login(
    payload,
):  # метод для создания запроса на логин курьер
    response = requests.post(
        f"{BASE_URL}/courier/login",
        json=payload,
        headers={"Content-Type": "application/json"},
    )
    return response


def post_response_for_make_order(payload):
    response = requests.post(
        f"{BASE_URL}/orders",
        json=payload,
        headers={"Content-Type": "application/json"},
    )
    return response


def get_response_for_get_order():
    response = requests.get(
        f"{BASE_URL}/orders",
    )
    return response


def get_response_for_get_order_with_track_number(track_number):
    response = requests.get(
        f"{BASE_URL}/orders/track?t={track_number}",
    )
    return response


def put_response_for_accept_order(track_number, courier_id):
    url = f"{BASE_URL}/orders/accept/{track_number}"

    # Передаем параметры отдельным словарем!
    params = {"courierId": courier_id}  # <-- Строго так, как в документации

    response = requests.put(url, params=params)
    return response
