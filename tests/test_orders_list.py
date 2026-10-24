import allure
import pytest

from helpers import get_orders


@allure.feature("Список заказов")
class TestOrdersList:

    @allure.title("В теле ответа возвращается список заказов: код 200, orders — массив")
    @pytest.mark.usefixtures("created_order")
    def test_get_orders_returns_list(self):
        response = get_orders({"limit": 10, "page": 0})

        assert response.status_code == 200
        assert isinstance(response.json().get("orders"), list)
