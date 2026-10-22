import pytest

from helpers import (
    cancel_order,
    create_courier,
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
    response = create_courier(courier_payload)
    assert response.status_code == 201, f"Не удалось создать курьера: {response.status_code} {response.text}"
    return courier_payload


@pytest.fixture
def created_order_tracks():
    tracks = []
    yield tracks
    for track in tracks:
        cancel_order(track)
