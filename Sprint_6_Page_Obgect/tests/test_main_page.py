import allure
import pytest

from Sprint_6_Page_Obgect.data import answers_data
from Sprint_6_Page_Obgect.urls import URL_MAIN_PAGE

class TestMainPage:

    @pytest.mark.parametrize(
        'num',
        [0, 1, 2, 3, 4, 5, 6, 7]
    )
    @allure.title('Проверка вопросов и ответов на главной странице')
    def test_questions_and_answers(self, num, main_page):
        display_num = num + 1
        @allure.step(f'Проверка вопросов и ответов на главной странице, : {display_num}')
        def check_answers():
            main_page.go_to_url(URL_MAIN_PAGE)
            assert main_page.check_question_and_answer(num) == answers_data(num)
        check_answers()
