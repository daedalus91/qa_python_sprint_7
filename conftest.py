import pytest

from data import ORDER_BASE_PAYLOAD
from helpers import (
    cancel_order_from_response,
    create_courier,
    create_order,
    delete_courier_by_credentials,
    generate_courier_payload,
)


@pytest.fixture
def courier_payload():
    payload = generate_courier_payload()
    yield payload
    delete_courier_by_credentials(payload["login"], payload["password"])


@pytest.fixture
def registered_courier(courier_payload):
    create_courier(courier_payload)
    return courier_payload


@pytest.fixture
def order_responses():
    responses = []
    yield responses
    for response in responses:
        cancel_order_from_response(response)


@pytest.fixture
def created_order():
    response = create_order(dict(ORDER_BASE_PAYLOAD))
    yield response
    cancel_order_from_response(response)
