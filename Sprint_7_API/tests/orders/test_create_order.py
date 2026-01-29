import json

import allure
import pytest

from Sprint_7_API.data import request_data_create_order_1, request_data_create_order_2
from Sprint_7_API.methods.order_methods import OrderMethods


class TestCreateOrder:

    @pytest.mark.parametrize("order_data", [
        request_data_create_order_1(),
        request_data_create_order_2(),
        None
    ])

    @allure.title('Тест создания заказа с различными входными данными')
    def test_create_order_success(self, order_data):
        status_code, response_data = OrderMethods().create_order(order_data)
        response_data = json.loads(response_data)
        assert 'track' in response_data and status_code == 201
        track_value = response_data['track']
        OrderMethods().delete_order(track_value)