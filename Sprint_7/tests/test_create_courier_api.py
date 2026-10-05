import allure
import helpers
import pytest
import api_methods as M


class TestCreateCourierApi:
    @allure.title('Проверка создания курьера. Возвращение 201')
    def test_create_new_courier_success_returns_201_and_ok_true(
        self, create_delete_courier
    ):  # курьера можно создать успешный запрос возвращает {"ok":true};
        # yield возвращает payload, response  нам нужен response
        response = create_delete_courier[1]
        assert response.status_code == 201
        assert response.text == '{"ok":true}'

    @pytest.mark.parametrize(
        "allure_title, payload",
        [
            (
                "Проверка регистрации курьера без логина",
                helpers.generate_payloads_with_login_null(),
            ),
            (
                "Проверка регистрации курьера без пароля",
                helpers.generate_payloads_with_password_null(),
            ),
        ],
    )
    def test_create_courier_missing_required_field_returns_400(
        self, allure_title, payload
    ):  # В данных тестах фиктура не используется так как пользователь не создаётся и его не надо удалять
        allure.dynamic.title(allure_title)
        # меняем заголовок allure после каждой итерации
        response = M.post_response_for_create(payload)

        assert response.status_code == 400

    @allure.title(
        "Проверка невозможности создать курьера с одинаковым логином - 409 conflict"
    )
    def test_create_two_equal_courier_return_409_conflict(
        self, create_delete_courier
    ):  # нельзя создать двух одинаковых курьеров
        # получаем значение логина, пароля и имени yield возвращает payload, response  нам нужен payload
        payload, first_response, _ = create_delete_courier
        # ещё раз отправляем запрос на создание пользователя с уже существующими лог\пасс

        second_response = M.post_response_for_create(payload)
        assert second_response.status_code == 409