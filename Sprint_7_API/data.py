BASE_URL = "https://qa-scooter.praktikum-services.ru/api/v1"
COURIER_URL = "/courier"
ORDERS_URL = "/orders"

def request_data_create_courier_valid_1():
    test_data = {
        "login": "courier_test_1_with_unicum_data",
        "password": "1234"
    }
    return test_data

def request_data_create_courier_miss_login():
    test_data = {
        "password": "1234"
    }
    return test_data
def request_data_create_courier_miss_password():
    test_data = {
        "login": "courier_test_2_with_unicum_data"
    }
    return test_data

def request_data_create_duple_courier():
    test_data = {
        "login": "courier_duple_with_unicum_data",
        "password": "1234"
    }
    return test_data

def request_data_create_courier_valid_2():
    test_data = {
        "login": "courier_test_3_with_unicum_data",
        "password": "1234"
    }
    return test_data

def request_data_create_order_1():
    test_data = {
        "color": ["BLACK"]
    }
    return test_data

def request_data_create_order_2():
    test_data = {
        "color": ["GRAY"]
    }
    return test_data

def request_data_create_courier_valid_for_orders():
    test_data = {
        "login": "courier_test_for_order_with_unicum_data",
        "password": "1234"
    }
    return test_data

def request_data_create_order_for_get_list():
    test_data = {
    "firstName": "Sonik",
    "lastName": "Begyn",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2026-02-06",
    "comment": "Faster",
    "color": [
        "BLACK"
    ]
}
    return test_data