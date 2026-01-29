import allure

from Sprint_7_API.data import request_data_create_courier_valid_1, request_data_create_duple_courier, request_data_create_courier_miss_password
from Sprint_7_API.methods.courier_methods import CourierMethods


class TestCreateCourier:

    @allure.title('Тест успешного создания курьера')
    def test_create_courier_success(self):
        data = request_data_create_courier_valid_1()
        response_data, status_code = CourierMethods().create_courier(data)
        assert response_data == {"ok": True} and status_code == 201
        CourierMethods().authorize_courier(data)
        id_courier = response_data.get("id")
        CourierMethods().delete_courier(id_courier)

    @allure.title('Тест невозможности создать курьера с отсутствующим паролем в запросе')
    def test_create_courier_failure(self):
        data = request_data_create_courier_miss_password()
        response_data, status_code = CourierMethods().create_courier(data)
        assert response_data['message'] == "Недостаточно данных для создания учетной записи" and status_code == 400

    @allure.title('Тест невозможности создать дубль курьера')
    def test_create_duple_courier(self ):
        data = request_data_create_duple_courier()
        CourierMethods().create_courier(data)
        response_data, status_code = CourierMethods().create_courier(data)
        assert response_data['message'] == "Этот логин уже используется. Попробуйте другой." and status_code == 409
        CourierMethods().authorize_courier(data)
        id_courier = response_data.get("id")
        CourierMethods().delete_courier(id_courier)


