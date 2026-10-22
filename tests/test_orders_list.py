import allure

from data import ORDER_BASE_PAYLOAD
from helpers import create_order, get_orders


@allure.feature("Список заказов")
class TestOrdersList:

    @allure.title("В теле ответа возвращается список заказов: код 200, orders — непустой массив")
    def test_get_orders_returns_list(self, created_order_tracks):
        create_response = create_order(dict(ORDER_BASE_PAYLOAD))
        assert create_response.status_code == 201
        created_order_tracks.append(create_response.json()["track"])

        response = get_orders({"limit": 10, "page": 0})
        body = response.json()

        assert response.status_code == 200
        assert isinstance(body.get("orders"), list)
        assert len(body["orders"]) > 0
