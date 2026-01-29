import json

import allure
import requests

from Sprint_7_API.data import BASE_URL, ORDERS_URL


class OrderMethods:

    @allure.step('Создание заказа')
    def create_order(self, params):
        response = requests.post(url=f'{BASE_URL}{ORDERS_URL}', json=params)
        return response.status_code, response.text

    @allure.step('Удаление заказа')
    def delete_order(self, params):
        response = requests.put(f'{BASE_URL}{ORDERS_URL}/cancel?track={str(params)}')
        return response.status_code, response.json()

    @allure.step('Получить заказ по его номеру')
    def get_order_info (self, params):
        response = requests.get(f'{BASE_URL}{ORDERS_URL}/track?t={str(params)}')
        return response.status_code, response.json()

    @allure.step('Принять заказ курьером')
    def accept_the_order_by_courier (self, order_id, courier_id):
        response = requests.put(f'{BASE_URL}{ORDERS_URL}/accept/{order_id}?courierId={str(courier_id)}')
        return response.status_code, response.json()

    @allure.step('Получить список заказов курьера')
    def get_a_list_of_courier_orders (self, params):
        response = requests.get(f'{BASE_URL}{ORDERS_URL}?courierId={str(params)}')
        return response.status_code, response.json()