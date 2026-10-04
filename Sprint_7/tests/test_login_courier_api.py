import helpers
import pytest
import allure
import main as M


class TestLoginCourierApi:

    @allure.title('Проверка логина созданного курьера. Возвращение 201')
    def test_courier_login_success_returns_id(self, create_delete_courier):
        payload = create_delete_courier[0]
        response_login = M.return_post_response_for_login(payload)

        assert response_login.status_code == 200
        assert response_login.json()["id"] is not None

    @pytest.mark.parametrize(
        "allure_title, field",
        [
            ("Проверка входа существуеющего курьера без логина", "login"),
            ("Проверка входа существуеющего курьера без пароля", "password"),
        ],
    )
    def test_courier_login_missing_field_returns_error_400(
        self, allure_title, field, create_delete_courier
    ):
        allure.dynamic.title(allure_title)
        payload = create_delete_courier[0]
        # Делаем копию, чтобы не портить оригинальные данныe
        bad_payload = payload.copy()
        # удаляем логин или пароль в зависимости от параметра теста
        del bad_payload[field]
        # Отправляем запрос с битыми данными
        response_login = M.return_post_response_for_login(bad_payload)

        assert response_login.status_code == 400

    @pytest.mark.parametrize(
        "allure_title, field",
        [
            ("Проверка входа курьера с несуществующим логином", "login"),
            ("Проверка входа курьера с несуществующим паролем", "password"),
        ],
    )
    # параметризация «Неверный пароль» и «Не существующий пользователь»
    def test_courier_login_invalid_data_return_error_404(
        self, allure_title, field, create_delete_courier
    ):
        allure.dynamic.title(allure_title)
        payload = create_delete_courier[0]
        # Делаем копию, чтобы не портить оригинальные данныe
        bad_payload = payload.copy()
        # заменяем логин или пароль в зависимости от параметра теста
        bad_payload[field] = helpers.generate_random_string(9)
        # Отправляем запрос с битыми данными
        response_login = M.return_post_response_for_login(bad_payload)

        assert response_login.status_code == 404
