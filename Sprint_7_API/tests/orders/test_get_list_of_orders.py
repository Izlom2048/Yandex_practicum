import json

import allure

from Sprint_7_API.data import request_data_create_courier_valid_for_orders, request_data_create_order_for_get_list
from Sprint_7_API.methods.courier_methods import CourierMethods
from Sprint_7_API.methods.order_methods import OrderMethods


class TestGetListOfOrders:

    @allure.title('Тест получения списка заказов курьера')
    def test_get_list_of_orders(self):
        data = request_data_create_courier_valid_for_orders()
        CourierMethods().create_courier(data)
        response_data, status_code = CourierMethods().authorize_courier(data)
        id_courier = response_data.get("id")
        order_data = request_data_create_order_for_get_list()
        status_code, response_data = OrderMethods().create_order(order_data)
        response_data = json.loads(response_data)
        track_value = response_data['track']
        status_code, response_data = OrderMethods().get_order_info(track_value)
        order_id = response_data['order']['id']
        OrderMethods().accept_the_order_by_courier(order_id, id_courier)
        status_code, response_data = OrderMethods().get_a_list_of_courier_orders(id_courier)
        orders = response_data['orders']
        assert orders != [] and status_code == 200
        CourierMethods().delete_courier(id_courier)