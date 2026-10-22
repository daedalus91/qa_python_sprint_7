import os

BASE_URL = os.getenv("SCOOTER_BASE_URL", "https://qa-scooter.praktikum-services.ru")

COURIER_URL = f"{BASE_URL}/api/v1/courier"
COURIER_LOGIN_URL = f"{BASE_URL}/api/v1/courier/login"
ORDERS_URL = f"{BASE_URL}/api/v1/orders"
ORDER_CANCEL_URL = f"{BASE_URL}/api/v1/orders/cancel"

REQUEST_TIMEOUT = 15
# список заказов отвечает медленно добавлен таймаут
ORDERS_LIST_TIMEOUT = 60


class Messages:
    CREATE_COURIER_NOT_ENOUGH_DATA = "Недостаточно данных для создания учетной записи"
    LOGIN_ALREADY_USED = "Этот логин уже используется"
    LOGIN_NOT_ENOUGH_DATA = "Недостаточно данных для входа"
    ACCOUNT_NOT_FOUND = "Учетная запись не найдена"


ORDER_BASE_PAYLOAD = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2026-12-06",
    "comment": "Saske, come back to Konoha",
}
