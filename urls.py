import os


class Urls:
    BASE_URL = os.getenv("SCOOTER_BASE_URL", "https://qa-scooter.praktikum-services.ru")

    COURIER = f"{BASE_URL}/api/v1/courier"
    COURIER_LOGIN = f"{BASE_URL}/api/v1/courier/login"
    ORDERS = f"{BASE_URL}/api/v1/orders"
    ORDER_CANCEL = f"{BASE_URL}/api/v1/orders/cancel"
