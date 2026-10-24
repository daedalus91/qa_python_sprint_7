import allure
import pytest

from data import ORDER_BASE_PAYLOAD
from helpers import create_order


@allure.feature("Создание заказа")
class TestCreateOrder:

    @allure.title("Заказ создаётся с цветом {color}: код 201 и в ответе есть track")
    @pytest.mark.parametrize(
        "color",
        [
            pytest.param(["BLACK"], id="black"),
            pytest.param(["GREY"], id="grey"),
            pytest.param(["BLACK", "GREY"], id="black_and_grey"),
            pytest.param([], id="empty_list"),
        ],
    )
    def test_create_order_with_color(self, order_responses, color):
        payload = {**ORDER_BASE_PAYLOAD, "color": color}
        response = create_order(payload)
        order_responses.append(response)

        assert response.status_code == 201
        assert isinstance(response.json().get("track"), int)

    @allure.title("Заказ создаётся без поля color: код 201 и в ответе есть track")
    def test_create_order_without_color_field(self, order_responses):
        payload = dict(ORDER_BASE_PAYLOAD)
        response = create_order(payload)
        order_responses.append(response)

        assert response.status_code == 201
        assert isinstance(response.json().get("track"), int)
