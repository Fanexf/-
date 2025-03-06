# Импортируем данные заказа
from data import order_body
# Импортируем функции создания заказа и получение информации о заказе по номеру
from sender_stend_request import create_order, get_order


def test_order_creation_and_retrieval():
    # Создаём заказ
    response_create = create_order(order_body)
    # Сохраняем номер заказа
    order_track = response_create.json()["track"]
    # Получаем информацию о заказе по номеру
    response_get = get_order(order_track)
    # Проверяем, что код ответа равен 200
    assert response_get.status_code == 200