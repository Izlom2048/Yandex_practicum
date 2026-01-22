import allure

from Sprint_6_Page_Obgect.locators.main_page_locators import MainPageLocators
from Sprint_6_Page_Obgect.pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Клик по вопросу')
    def click_to_question(self, num):
        locator_q_formatted = self.format_locators(
            MainPageLocators.QUESTIONS_ON_THE_MAIN_BUTTON, num)
        self.scroll_to_element(MainPageLocators.QUESTIONS_ON_THE_MAIN_TO_SCROLL_BUTTON)
        self.click_element(locator_q_formatted)

    @allure.step('Получение текста ответа для вопроса')
    def get_answer_text(self, num):
        locator_a_formatted = self.format_locators(
            MainPageLocators.ANSWER_ON_THE_MAIN_BUTTON, num)
        return self.get_text_from_element(locator_a_formatted)

    @allure.step('Проверка вопроса и ответа')
    def check_question_and_answer(self, num):
        self.click_to_question(num)
        return self.get_answer_text(num)
