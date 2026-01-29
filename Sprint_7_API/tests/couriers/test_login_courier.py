import allure

from Sprint_7_API.data import request_data_create_courier_valid_1, request_data_create_courier_miss_login, request_data_create_courier_valid_2
from Sprint_7_API.methods.courier_methods import CourierMethods


class TestLoginCourier:

    @allure.title('Тест валидной авторизации курьера')
    def test_auth_courier_success(self):
        data = request_data_create_courier_valid_1()
        CourierMethods().create_courier(data)
        response_login_courier, status_code = CourierMethods().authorize_courier(data)
        assert 'id' in response_login_courier and status_code == 200
        id_courier = response_login_courier.get("id")
        CourierMethods().delete_courier(id_courier)

    @allure.title('Тест невозможности авторизоваться при отсутствии ввода пароля')
    def test_auth_courier_missing_login(self):
        data = request_data_create_courier_miss_login()
        CourierMethods().create_courier(data)
        response_login_courier, status_code = CourierMethods().authorize_courier(data)
        assert response_login_courier['message'] == 'Недостаточно данных для входа' and status_code == 400

    @allure.title('Тест невозможности авторизоваться курьером с некорректным паролем')
    def test_auth_courier_with_invalid_password(self):
        data = request_data_create_courier_valid_2()
        CourierMethods().create_courier(data)
        data_login_with_invalid_password = data.copy()
        data_login_with_invalid_password['password']='invalid_password'
        response_login_courier, status_code = CourierMethods().authorize_courier(data_login_with_invalid_password)
        assert response_login_courier['message'] == 'Учетная запись не найдена' and status_code == 404
        response_data, status_code = CourierMethods().authorize_courier(data)
        id_courier = response_data.get("id")
        CourierMethods().delete_courier(id_courier)