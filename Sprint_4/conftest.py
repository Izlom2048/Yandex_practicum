import pytest


@pytest.fixture
def books_without_genre():
    books_without_genre = ['Мечта на поражение', 'Дом на болоте', 'Холодная кровь']
    return books_without_genre

@pytest.fixture
def books_with_genre():
    books_with_genre = {'Мечта на поражение':'Фантастика', 'Дом на болоте':'Фантастика', 'Холодная кровь':'Ужасы'}
    return books_with_genre