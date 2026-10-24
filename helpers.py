import random
import string

import allure
import requests

from urls import Urls

REQUEST_TIMEOUT = 15
# список заказов отвечает медленно добавлен таймаут
ORDERS_LIST_TIMEOUT = 60


def generate_random_string(length=10):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


def generate_courier_payload():
    return {
        "login": generate_random_string(10),
        "password": generate_random_string(10),
        "firstName": generate_random_string(10),
    }


@allure.step("Создать курьера")
def create_courier(payload):
    return requests.post(Urls.COURIER, json=payload, timeout=REQUEST_TIMEOUT)


@allure.step("Залогинить курьера")
def login_courier(payload):
    return requests.post(Urls.COURIER_LOGIN, json=payload, timeout=REQUEST_TIMEOUT)


@allure.step("Удалить курьера с id {courier_id}")
def delete_courier(courier_id):
    return requests.delete(f"{Urls.COURIER}/{courier_id}", timeout=REQUEST_TIMEOUT)


@allure.step("Удалить курьера по логину и паролю, если он существует")
def delete_courier_by_credentials(login, password):
    response = login_courier({"login": login, "password": password})
    if response.status_code == 200:
        delete_courier(response.json()["id"])


@allure.step("Создать заказ")
def create_order(payload):
    return requests.post(Urls.ORDERS, json=payload, timeout=REQUEST_TIMEOUT)


@allure.step("Отменить заказ с треком {track}")
def cancel_order(track):
    return requests.put(Urls.ORDER_CANCEL, json={"track": track}, timeout=REQUEST_TIMEOUT)


@allure.step("Отменить заказ, созданный запросом, если заказ создан")
def cancel_order_from_response(response):
    if response.status_code == 201:
        cancel_order(response.json()["track"])


@allure.step("Получить список заказов")
def get_orders(params=None):
    return requests.get(Urls.ORDERS, params=params, timeout=ORDERS_LIST_TIMEOUT)
