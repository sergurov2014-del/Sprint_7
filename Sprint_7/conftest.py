import pytest
import requests
import helpers
import time

# Базовый URL вынеси в константу, чтобы не дублировать
BASE_URL = "https://qa-scooter.education-services.ru/api/v1"


@pytest.fixture
def created_courier():

    # 1. ПОДГОТОВКА (До теста)
    payload = helpers.new_courier_data()

    response = requests.post(f"{BASE_URL}/courier", json=payload)
    id = requests.post(f"{BASE_URL}/courier/login", json=payload).json()['id']

    return response
    yield payload

    # 2. ОЧИСТКА (После теста)
    # Удаляем курьера по логину. Эндпоинт удаления обычно такой: DELETE /courier/{login}
   

    delete_response = requests.delete(f"{BASE_URL}/courier/:{id}")

    if delete_response.status_code not in [200, 204]:# Логируем, прошло ли удаление 
        
        print(
            f"Предупреждение: не удалось удалить курьера {payload['login']} после теста. Статус: {delete_response.status_code}"
        )
