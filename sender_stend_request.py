# Импорт настроек из модуля configuration, который содержит URL сервиса
import configuration

# Импорт библиотеки requests для выполнения HTTP-запросов
import requests

# Импорт данных запроса из data, заголовки и тело запроса
import data


def create_order(order_body):
    # Создание заказа
    response_create = requests.post(configuration.URL_ORDERS, json=order_body)
    return response_create


def get_order(track):
    # Получение информации о заказе по номеру трека
    url = configuration.URL_TRACK + str(track)
    response_get = requests.get(url)
    return response_get
