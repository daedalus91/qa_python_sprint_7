import allure
import pytest

from data import ORDER_BASE_PAYLOAD
from helpers import create_order

NO_COLOR = object()


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
            pytest.param(NO_COLOR, id="no_color_field"),
        ],
    )
    def test_create_order_with_color(self, created_order_tracks, color):
        payload = dict(ORDER_BASE_PAYLOAD)
        if color is not NO_COLOR:
            payload["color"] = color

        response = create_order(payload)
        body = response.json()
        if "track" in body:
            created_order_tracks.append(body["track"])

        assert response.status_code == 201
        assert isinstance(body.get("track"), int)
