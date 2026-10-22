import random
import string

import allure
import requests

from data import (
    COURIER_LOGIN_URL,
    COURIER_URL,
    ORDER_CANCEL_URL,
    ORDERS_LIST_TIMEOUT,
    ORDERS_URL,
    REQUEST_TIMEOUT,
)


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
    return requests.post(COURIER_URL, json=payload, timeout=REQUEST_TIMEOUT)


@allure.step("Залогинить курьера")
def login_courier(payload):
    return requests.post(COURIER_LOGIN_URL, json=payload, timeout=REQUEST_TIMEOUT)


@allure.step("Удалить курьера с id {courier_id}")
def delete_courier(courier_id):
    return requests.delete(f"{COURIER_URL}/{courier_id}", timeout=REQUEST_TIMEOUT)


@allure.step("Удалить курьера по логину и паролю, если он существует")
def delete_courier_by_credentials(login, password):
    response = login_courier({"login": login, "password": password})
    if response.status_code == 200 and "id" in response.json():
        delete_courier(response.json()["id"])


@allure.step("Создать заказ")
def create_order(payload):
    return requests.post(ORDERS_URL, json=payload, timeout=REQUEST_TIMEOUT)


@allure.step("Отменить заказ с треком {track}")
def cancel_order(track):
    return requests.put(ORDER_CANCEL_URL, json={"track": track}, timeout=REQUEST_TIMEOUT)


@allure.step("Получить список заказов")
def get_orders(params=None):
    return requests.get(ORDERS_URL, params=params, timeout=ORDERS_LIST_TIMEOUT)
