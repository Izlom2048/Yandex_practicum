import pytest


from task_1 import BooksCollector


class TestBooksCollector:

    def test_add_new_book_valid_length_name_book_true(self):
        books_collector = BooksCollector()
        name_book = 'Мечта на поражение'
        books_collector.add_new_book(name_book)
        assert name_book in books_collector.books_genre

    @pytest.mark.parametrize('name_book', ['', 'Странная история доктора Джекила и мистера Хайда'])
    def test_add_new_book_invalid_length_name_book_false(self, name_book):
        books_collector = BooksCollector()
        books_collector.add_new_book(name_book)
        assert name_book not in books_collector.books_genre

    def test_set_book_genre_valid_genre_true(self):
        books_collector = BooksCollector()
        name_book = 'Мечта на поражение'
        genre = 'Фантастика'
        books_collector.add_new_book(name_book)
        books_collector.set_book_genre(name_book, genre)
        assert books_collector.books_genre.get(name_book) == genre

    def test_set_book_genre_invalid_genre_false(self):
        books_collector = BooksCollector()
        name_book = 'Мастер и Маргарита'
        genre = 'Мистика'
        books_collector.add_new_book(name_book)
        books_collector.set_book_genre(name_book, genre)
        assert books_collector.books_genre.get(name_book) == ''

    def test_get_book_genre_valid_genre_true(self):
        books_collector = BooksCollector()
        name_book = 'Мечта на поражение'
        genre = 'Фантастика'
        books_collector.add_new_book(name_book)
        books_collector.set_book_genre(name_book, genre)
        assert books_collector.get_book_genre(name_book) == genre

    def test_get_books_with_specific_genre_valid_genre_true(self, books_with_genre):
        books_collector = BooksCollector()
        for name, book_genre in books_with_genre.items():
            books_collector.add_new_book(name)
            books_collector.set_book_genre(name, book_genre)
        assert books_collector.get_books_with_specific_genre('Фантастика') == ['Мечта на поражение', 'Дом на болоте']

    def test_get_books_with_specific_genre_invalid_genre_false(self, books_with_genre):
        books_collector = BooksCollector()
        for name, book_genre in books_with_genre.items():
            books_collector.add_new_book(name)
            books_collector.set_book_genre(name, book_genre)
        assert books_collector.get_books_with_specific_genre('Мистика') == []

    def test_get_books_genre_added_book_true(self, books_without_genre):
        books_collector = BooksCollector()
        for book in books_without_genre:
            books_collector.add_new_book(book)
        assert books_collector.get_books_genre() == {'Дом на болоте': '', 'Мечта на поражение': '', 'Холодная кровь': ''}

    def test_get_books_for_children_added_book_true(self, books_with_genre):
        books_collector = BooksCollector()
        for name, book_genre in books_with_genre.items():
            books_collector.add_new_book(name)
            books_collector.set_book_genre(name, book_genre)
        assert books_collector.get_books_for_children() == ['Мечта на поражение', 'Дом на болоте']

    def test_add_book_in_favorites_added_book_true(self, books_without_genre):
        books_collector = BooksCollector()
        for name in books_without_genre:
            books_collector.add_new_book(name)
        books_collector.add_book_in_favorites(books_without_genre[0])
        assert books_collector.favorites == ['Мечта на поражение']


    def test_add_book_in_favorites_added_another_book_false(self, books_without_genre):
        books_collector = BooksCollector()
        for name in books_without_genre:
            books_collector.add_new_book(name)
        books_collector.add_book_in_favorites('Тени Чернобыля')
        assert books_collector.favorites == []

    def test_delete_book_from_favorites_deleted_book_true(self, books_without_genre):
        books_collector = BooksCollector()
        for name in books_without_genre:
            books_collector.add_new_book(name)
        books_collector.add_book_in_favorites(books_without_genre[0])
        books_collector.delete_book_from_favorites(books_without_genre[0])
        assert books_collector.favorites == []

    def test_delete_book_from_favorites_another_book_deleted_false(self, books_without_genre):
        books_collector = BooksCollector()
        for name in books_without_genre:
            books_collector.add_new_book(name)
        books_collector.add_book_in_favorites(books_without_genre[0])
        books_collector.delete_book_from_favorites('Тени Чернобыля')
        assert books_collector.favorites == ['Мечта на поражение']

    def test_get_list_of_favorites_books(self, books_without_genre):
        books_collector = BooksCollector()
        for name in books_without_genre:
            books_collector.add_new_book(name)
            books_collector.add_book_in_favorites(name)
        assert books_collector.get_list_of_favorites_books() == books_without_genre
