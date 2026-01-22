import allure
import pytest

from Sprint_6_Page_Obgect import urls, data


class TestOrderPage:

    @pytest.mark.parametrize(
        'num',
        [1, 2]
    )
    @allure.title('Тест создания заказа, набор тестовых данных: {num}')
    def test_create_order(self, num, order_page):
        order_page.go_to_url(urls.URL_MAIN_PAGE)
        order_page.fill_data_and_go_next_page_order(num)
        order_page.fill_data_in_second_screen_order(num)
        assert data.order_state() in order_page.check_state_of_the_order()
        order_page.close_overlay_order_page()
        assert urls.URL_MAIN_PAGE == order_page.check_scooter_redirect()
        assert urls.URL_YA_DZEN == order_page.check_yandex_redirect_page_in_new_tab()
