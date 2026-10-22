# Автотесты API «Яндекс Самокат»

https://qa-scooter.praktikum-services.ru

## Структура

| Файл | Класс | Ручка |
|---|---|---|
| `tests/test_create_courier.py` | `TestCreateCourier` | `POST /api/v1/courier` |
| `tests/test_login_courier.py` | `TestLoginCourier` | `POST /api/v1/courier/login` |
| `tests/test_create_order.py` | `TestCreateOrder` | `POST /api/v1/orders` |
| `tests/test_orders_list.py` | `TestOrdersList` | `GET /api/v1/orders` |

- `data.py` — URL, тексты ошибок, тестовые данные заказа.
- `helpers.py` — запросы к API и генерация данных.
- `conftest.py` — фикстуры


## Запуск

```bash
pip install -r requirements.txt
pytest --alluredir=allure_results
```

## Отчёт Allure

```bash
allure serve allure_results
```

В репозиторий пушится папка `allure_results` с результатами прогона.
