import allure
from urls import BASE_URL
import requests


class TestDeleteCourierApi:
    @allure.title('Проверка успешного удаления созданного курьера. Возвращение 200')
    def test_delete_courier_success_returns_201_and_ok_true(
        self, create_courier
    ):  # курьера можно создать успешный запрос возвращает {"ok":true};
        courier_id = create_courier
        delete_response = requests.delete(
            f"{BASE_URL}/courier/{courier_id}"
        )  # ОЧИСТКА Удаляем курьера по id. Эндпоинт удаления обычно такой: DELETE /courier/{login}

        assert delete_response.status_code == 200
        assert delete_response.text == '{"ok":true}'

    @allure.title("Проверка удаления несуществующего курьера.")
    def test_delete_nonexistent_courier_returns_404(
        self,
    ):
        delete_response = requests.delete(
            f"{BASE_URL}/courier/{999999999}"
        )  # ОЧИСТКА Удаляем курьера по id. Эндпоинт удаления обычно такой: DELETE /courier/{login}

        assert delete_response.status_code == 404
