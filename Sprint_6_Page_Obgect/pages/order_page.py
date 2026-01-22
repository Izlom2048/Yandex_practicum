import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Sprint_6_Page_Obgect.data import first_data_for_order, second_data_for_order, order_data_of_field, \
    first_data_for_order_second_page, second_data_for_order_second_page
from Sprint_6_Page_Obgect.locators.order_page_locators import OrderPageFirstScreenLocators, \
    OrderPageSecondScreenLocators
from Sprint_6_Page_Obgect.pages.base_page import BasePage
from Sprint_6_Page_Obgect.urls import URL_YA_DZEN


class OrderPage(BasePage):

    @allure.step('Клик по кнопке заказа, тип: {num}')
    def click_to_order_button(self, num):
        if num == 1:
            locator = OrderPageFirstScreenLocators.FIRST_ORDER_BUTTON
            self.scroll_to_element(locator)
        else:
            locator = OrderPageFirstScreenLocators.SECOND_ORDER_BUTTON
            self.click_element(OrderPageFirstScreenLocators.COOKIE_BUTTON)
        self.click_element(locator)


    @allure.step('Заполнение данных на первом экране заказа, набор тестовых данных: {num}')
    def fill_data_in_first_screen_order(self, num):
        if num == 1:
            data_source = first_data_for_order
        else:
            data_source = second_data_for_order
        field_indexes = [0, 1, 2, 3]
        for i in field_indexes:
            locator_q_formatted = self.format_locators(
                OrderPageFirstScreenLocators.ENTER_ORDER_DATA_FIELD, order_data_of_field(i))
            self.click_element(locator_q_formatted)
            self.add_text_to_element(locator_q_formatted, data_source(i))
        locator_q_formatted = self.format_locators(
            OrderPageFirstScreenLocators.ENTER_ORDER_DATA_FIELD, order_data_of_field(4))
        self.click_element(locator_q_formatted)
        locator_q_formatted = self.format_locators(
            OrderPageFirstScreenLocators.METRO_STATION_SELECTION, num)
        self.click_element(locator_q_formatted)


    @allure.step('Переход ко второму экрану заказа')
    def go_second_screen_order(self):
        self.click_element(OrderPageFirstScreenLocators.NEXT_BUTTON)

    @allure.step('Заполнение данных и переход ко второму экрану заказа')
    def fill_data_and_go_next_page_order(self, num):
        self.click_to_order_button(num)
        self.fill_data_in_first_screen_order(num)
        self.go_second_screen_order()

    @allure.step('Заполнение данных на втором экране заказа')
    def fill_data_in_second_screen_order(self, num):
        if num == 1:
            data_source = first_data_for_order_second_page
        else:
            data_source = second_data_for_order_second_page
        self.click_element(OrderPageSecondScreenLocators.ORDER_DATE_FIELD)
        self.add_text_to_element(OrderPageSecondScreenLocators.ORDER_DATE_FIELD, data_source(0))
        self.click_element(OrderPageSecondScreenLocators.TITLE_PAGE)
        self.click_element(OrderPageSecondScreenLocators.ENTER_RENTAL_PERIOD_FIELD)
        locator_q_formatted = self.format_locators(
            OrderPageSecondScreenLocators.ENTER_PERIOD_SELECTION, data_source(1))
        self.scroll_to_element(locator_q_formatted)
        self.click_element(locator_q_formatted)
        locator_q_formatted = self.format_locators(
            OrderPageSecondScreenLocators.ENTER_COLOR_CHECKBOX, data_source(2))
        self.click_element(locator_q_formatted)
        self.click_element(OrderPageSecondScreenLocators.ENTER_COMMENT_FOR_THE_COURIER_FIELD)
        self.add_text_to_element(OrderPageSecondScreenLocators.ENTER_COMMENT_FOR_THE_COURIER_FIELD, data_source(3))
        self.click_element(OrderPageSecondScreenLocators.ORDER_BUTTON)
        self.click_element(OrderPageSecondScreenLocators.YES_BUTTON)

    @allure.step('Проверка состояния заказа')
    def check_state_of_the_order(self):
        return self.get_text_from_element(OrderPageSecondScreenLocators.ORDER_CONFIRMATION)

    @allure.step('Закрытие оверлея на странице заказа')
    def close_overlay_order_page(self):
        self.click_element(OrderPageSecondScreenLocators.SEE_STATE_BUTTON)


    @allure.step('Проверка редиректа на главную страницу')
    def check_scooter_redirect(self):
        self.click_element(OrderPageSecondScreenLocators.IMAGE_SCOOTER_LINK)
        return self.get_current_url()

    @allure.step('Проверка редиректа на страницу Яндекса в новой вкладке')
    def check_yandex_redirect_page_in_new_tab(self):
        self.click_element(OrderPageSecondScreenLocators.IMAGE_YANDEX_LINK)
        self.switch_to_another_tab()
        WebDriverWait(self.driver, self.timeout).until(
            expected_conditions.url_contains(URL_YA_DZEN))
        return self.get_current_url()
