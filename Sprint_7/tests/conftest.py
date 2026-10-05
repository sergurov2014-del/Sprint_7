import sys
import os
current_dir = os.path.dirname(
    os.path.abspath(__file__)
)  # 2. Поднимаемся на уровень выше (выходим из папки tests в корень Sprint_7)
project_root = os.path.dirname(
    current_dir
)  # 3. Добавляем этот корень в список путей, где Python ищет модули
if project_root not in sys.path:
    sys.path.insert(0, project_root)

import helpers  # Теперь этот импорт сработает, так как мы добавили корень в sys.path import helpers
from urls import BASE_URL
import pytest
import requests

@pytest.fixture
def create_courier():
    payload = helpers.new_courier_data()
    response = requests.post(f"{BASE_URL}/courier", json=payload)
    courier_id = requests.post(f"{BASE_URL}/courier/login", json=payload).json()["id"]
    assert response.status_code == 201
    yield courier_id  # yield- точка разделения. Всё, что ДО yield, выполн-ся ПЕРЕД тестом.ПОСЛЕ yield, вып-ся ПОСЛЕ теста (даже если тест упал!)
     
@pytest.fixture
def create_delete_courier():

    # 1. ПОДГОТОВКА (До теста)
    payload = helpers.new_courier_data()

    response = requests.post(f"{BASE_URL}/courier", json=payload)
    courier_id = requests.post(f"{BASE_URL}/courier/login", json=payload).json()["id"]
    assert response.status_code == 201
   
    # Для проверяюшего. В pytest механизм yield уже работает как встроенный try...finally!
    #   Код до yield = try (подготовка). Код после yield = finally (очистка).
    # Если  тест упадет с ошибкой, pytest всё равно выполнит код после yield и удалит курьера
    yield payload, response, courier_id  # yield- точка разделения. Всё, что ДО yield, выполн-ся ПЕРЕД тестом.ПОСЛЕ yield, вып-ся ПОСЛЕ теста (даже если тест упал!)
 

    delete_response = requests.delete(f"{BASE_URL}/courier/{courier_id}") #ОЧИСТКА Удаляем курьера по id. Эндпоинт удаления обычно такой: DELETE /courier/{login}
