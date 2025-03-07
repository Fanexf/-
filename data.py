# заголовки для HTTP-запроса, указывающие на то, что тело запроса будет в формате JSON
headers = {"Content-Type": "application/json"}

# данные для создания заказа
order_body = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Saske, come back to Konoha",
    "color": ["BLACK"],
}
