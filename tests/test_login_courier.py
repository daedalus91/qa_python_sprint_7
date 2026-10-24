import allure
import pytest

from data import Messages
from helpers import generate_random_string, login_courier


@allure.feature("Логин курьера")
class TestLoginCourier:

    @allure.title("Курьер может авторизоваться: код 200 и в ответе есть id")
    def test_login_courier_success(self, registered_courier):
        payload = {"login": registered_courier["login"], "password": registered_courier["password"]}
        response = login_courier(payload)

        assert response.status_code == 200
        assert isinstance(response.json().get("id"), int)

    @allure.title("Неверное поле {wrong_field}: код 404")
    @pytest.mark.parametrize("wrong_field", ["login", "password"])
    def test_login_with_wrong_credentials(self, registered_courier, wrong_field):
        payload = {"login": registered_courier["login"], "password": registered_courier["password"]}
        payload[wrong_field] = payload[wrong_field] + "wrong"
        response = login_courier(payload)

        assert response.status_code == 404
        assert response.json()["message"] == Messages.ACCOUNT_NOT_FOUND

    @allure.title("Без поля {missing_field} в запросе: код 400")
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_login_without_required_field(self, registered_courier, missing_field):
        payload = {"login": registered_courier["login"], "password": registered_courier["password"]}
        del payload[missing_field]
        response = login_courier(payload)

        assert response.status_code == 400
        assert response.json()["message"] == Messages.LOGIN_NOT_ENOUGH_DATA

    @allure.title("С пустым значением поля {empty_field}: код 400")
    @pytest.mark.parametrize("empty_field", ["login", "password"])
    def test_login_with_empty_field(self, registered_courier, empty_field):
        payload = {"login": registered_courier["login"], "password": registered_courier["password"]}
        payload[empty_field] = ""
        response = login_courier(payload)

        assert response.status_code == 400
        assert response.json()["message"] == Messages.LOGIN_NOT_ENOUGH_DATA

    @allure.title("Авторизация несуществующего курьера: код 404")
    def test_login_nonexistent_courier(self):
        payload = {"login": generate_random_string(12), "password": generate_random_string(12)}
        response = login_courier(payload)

        assert response.status_code == 404
        assert response.json()["message"] == Messages.ACCOUNT_NOT_FOUND
