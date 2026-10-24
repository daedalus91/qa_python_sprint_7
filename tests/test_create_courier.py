import allure
import pytest

from data import Messages
from helpers import create_courier


@allure.feature("Создание курьера")
class TestCreateCourier:

    @allure.title("Курьера можно создать: код 201 и в ответе ok = true")
    def test_create_courier_success(self, courier_payload):
        response = create_courier(courier_payload)

        assert response.status_code == 201
        assert response.json() == {"ok": True}

    @allure.title("Нельзя создать двух одинаковых курьеров: код 409")
    def test_create_duplicate_courier_conflict(self, registered_courier):
        response = create_courier(registered_courier)

        assert response.status_code == 409
        assert Messages.LOGIN_ALREADY_USED in response.json()["message"]

    @allure.title("Нельзя создать курьера с уже существующим логином: код 409")
    def test_create_courier_with_existing_login_conflict(self, registered_courier):
        payload = {
            "login": registered_courier["login"],
            "password": "otherpassword",
            "firstName": "othername",
        }
        response = create_courier(payload)

        assert response.status_code == 409
        assert Messages.LOGIN_ALREADY_USED in response.json()["message"]

    @allure.title("Без обязательного поля {missing_field} курьер не создаётся: код 400")
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_create_courier_without_required_field(self, courier_payload, missing_field):
        payload = dict(courier_payload)
        del payload[missing_field]
        response = create_courier(payload)

        assert response.status_code == 400
        assert response.json()["message"] == Messages.CREATE_COURIER_NOT_ENOUGH_DATA
