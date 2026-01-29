import json
import string
import random

import allure
import requests
from Sprint_7_API.data import BASE_URL, COURIER_URL


class CourierMethods:

    @allure.step('Создание курьера')
    def create_courier(self, params=None):
        if params is None:
            params = self.generating_credentials()
        response = requests.post(f'{BASE_URL}{COURIER_URL}', json=params)
        try:
            return response.json(), response.status_code
        except json.decoder.JSONDecodeError:
            return response

    @allure.step('Авторизация курьера')
    def authorize_courier(self, params):
        response = requests.post(f'{BASE_URL}{COURIER_URL}/login', json=params)
        return response.json(), response.status_code

    @allure.step('Удаление курьера')
    def delete_courier(self, id_courier):
        response = requests.delete(f'{BASE_URL}{COURIER_URL}/{id_courier}')
        return response.json()

    @allure.step('Генерация случайных логина, пароля и именя для авторизации курьера')
    def generating_credentials(self):
        def generate_random_string(length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string
        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        return payload
