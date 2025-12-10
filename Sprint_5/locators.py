import random

from selenium.webdriver.common.by import By


class MainPageLocators: # Стартовая страница (https://qa-desk.stand.praktikum-services.ru/)
        # Кнопка "Вход и регистрация":
    LOGIN_AND_REGISTRATION_BUTTON = (By.XPATH, "html/body/div/div/div[@class='header_shell__zlCGj']/div/button[text()='Вход и регистрация']")
        # Кнопка "Разместить объявление":
    POST_AN_AD_BUTTON = (By.XPATH, 'html/body/div/div/div[@class="header_shell__zlCGj"]/div/button[@type="button"]')
        # Модальное окно "Чтобы разместить объявление, авторизуйтесь"
    MODAL_WINDOW_REQUIRING_AUTHORIZE_TEXT = (By.CLASS_NAME, "popUp_titleRow__M7tGg")
        # Кнопка "Применить" для поиска карточек на главной
    APPLY_FILTER_FOR_FIND_CARD_BUTTON = (By.XPATH, 'html/body/div/div/div[2]/form/div[2]/button')

class LoginModalWindowLocators: # Модальное окно "Войти" при клике на "Вход и регистрация"
        # Поле "Введите Email":
    ENTER_EMAIL_FIELD = (By.NAME, "email")
        # Поле "Пароль":
    ENTER_PASSWORD_FIELD = (By.NAME, "password")
        # Кнопка "Войти":
    LOGIN_BUTTON = (By.XPATH, 'html/body/div/div/div[@class="homePage_homepageStyle__WP-Y1"]/div[@class="homePage_modal__zSdUB"]/form/div[@class="popUp_buttonRow__+W8JD"]/button[@type="submit"]')
        # Кнопка "Нет аккаунта":
    NO_ACCOUNT_BUTTON = (By.XPATH, '/html/body/div/div/div[@class="homePage_homepageStyle__WP-Y1"]/div[@class="homePage_modal__zSdUB"]/form/div[@class="popUp_buttonRow__+W8JD"]/button[@type="button"]')

class RegisterModalWindowLocators: # Модальное окно "Зарегистрироваться" при клике на "Нет аккаунта" в модальном окне "Войти"
        # Поле "Введите Email":
    ENTER_EMAIL_FIELD = (By.NAME, "email")
        # Поле "Пароль":
    ENTER_PASSWORD_FIELD = (By.NAME, "password")
        # Поле "Пароль":
    ENTER_SUBMIT_PASSWORD_FIELD = (By.NAME, "submitPassword")
        # Кнопка "Создать аккаунт":
    CREATE_ACCOUNT_BUTTON = (By.XPATH, 'html/body/div/div/div[@class="homePage_homepageStyle__WP-Y1"]/div[@class="homePage_modal__zSdUB"]/form/div[@class="popUp_buttonRow__+W8JD"]/button[@type="submit"]')
        # Текст ошибки регистрации "Ошибка":
    VALIDATION_REGISTER_ERROR  = (By.XPATH, 'html/body/div/div/div[@class="homePage_homepageStyle__WP-Y1"]/div[@class="homePage_modal__zSdUB"]/form/div[@class="popUp_inputColumn__RgD8n"]/div[1]/span[text()="Ошибка"]')
        # Красные поля валидации полей почты, пароля и повтора пароля
    RED_VALIDATION_REGISTER_FIELD = (By.XPATH, 'html/body/div/div/div[@class="homePage_homepageStyle__WP-Y1"]/div[@class="homePage_modal__zSdUB"]/form/div[@class="popUp_inputColumn__RgD8n"]/div/div/div[@class="input_inputError__fLUP9"]')

class AuthorizedUserLocators: # Страница авторизованного пользователя
        # Аватарка пользователя:
    USER_AVATAR = (By.CSS_SELECTOR, ".circleSmall")
        # Имя пользователя:
    USER_NAME = (By.CSS_SELECTOR, ".profileText")
        # Кнопка "Выйти":
    EXITE_BUTTON = (By.XPATH, 'html/body/div/div/div[@class="header_shell__zlCGj"]/div/div[@class="flexRow"]/div/button[text()="Выйти"]')


class PostAnAdPageLocators: # Страница "Разместить объявление"
    category_list = ['Авто', 'Книги', 'Садоводство', 'Хобби', 'Технологии']
    xpath_category_variable = f'html/body/div/div/div[@class="createListingPage_createListingPageStyle__U-MJJ"]/div/form/div[@class="createListing_inputRow__fmwXw"]/div[@class="dropDownMenu_dropMenu__sBxhz"]/div[@class="dropDownMenu_options__CmHmm"]/button/span[text()="{random.choice(category_list)}"]'
    city_list = ['Москва', 'Санкт-Петербург', 'Новосибирск', 'Екатеринбург', 'Нижний Новгород', 'Казань']
    xpath_city_variable = f'html/body/div/div/div[@class="createListingPage_createListingPageStyle__U-MJJ"]/div/form/div[@class="dropDownMenu_dropMenu__sBxhz"]/div[@class="dropDownMenu_options__CmHmm"]/button/span[text()="{random.choice(city_list)}"]'
        # radioUnput_inputRegular__FbVbr - Новый
        # radioUnput_inputActive__eC-HY - Б/У
    radiobutton_list = ['radioUnput_inputRegular__FbVbr', 'radioUnput_inputActive__eC-HY']
        # Поле "Название"
    ENTER_NAME_CARD_FIELD = (By.NAME, "name")
        # Поле "Описание товара"
    ENTER_PRODUCT_DESCRIPTION_CARD_FIELD = (By.CSS_SELECTOR, ".textarea_inputStandart__IoNxq.spanGlobal")
        # Поле "Стоимость"
    ENTER_PRICE_CARD_FIELD = (By.NAME, "price")
        # Дропдаун "Категория"
    ENTER_DROPDOWN_CATEGORY_CARD_FIELD = (By.XPATH, 'html/body/div/div/div[@class="createListingPage_createListingPageStyle__U-MJJ"]/div/form/div[@class="createListing_inputRow__fmwXw"]/div[@class="dropDownMenu_dropMenu__sBxhz"]/div[@class="dropDownMenu_input__itKtw"]/button')
        # Выбор случайного значения подкатегории "Категория"
    CHOICE_VALUE_DROPDOWN_CATEGORY_CARD_FIELD = (By.XPATH, xpath_category_variable)
        # Дропдаун "Город"
    ENTER_DROPDOWN_CITY_CARD_FIELD = (By.XPATH, 'html/body/div/div/div[@class="createListingPage_createListingPageStyle__U-MJJ"]/div/form/div[@class="dropDownMenu_dropMenu__sBxhz"]/div[@class="dropDownMenu_input__itKtw"]/button')
        # Выбор случайного значения подкатегории "Город"
    CHOICE_VALUE_DROPDOWN_CITY_CATEGORY_CARD_FIELD = (By.XPATH, xpath_city_variable)
        # Выбор случайного значения радиокнопки "Новый" или "Б/У"
    CHOICE_NEW_RADIOBUTTON = (By.CLASS_NAME, random.choice(radiobutton_list))
        # Кнопка "Опубликовать"
    ENTER_PUBLISH_BUTTON = (By.CSS_SELECTOR, '[type="submit"]')
        # Кнопка пагинации далее (вправо)
    PAGINATION_BUTTON = (By.XPATH, 'html/body/div/div/div[@class="profilePage_shell__8JYbq"]/div[@class="profilePage_listningBlock__Fi6E5"]/div/div[@class="pagination_shell__c6Llq"]/button[@class="arrowButton arrowButton--right undefined"]')
        # Счетчик пагинации (второе число)
    NUMBERING_OF_PAGINATION_BUTTON = (By.XPATH, 'html/body/div/div/div[@class="profilePage_shell__8JYbq"]/div[@class="profilePage_listningBlock__Fi6E5"]/div/div[@class="pagination_shell__c6Llq"]/p')

def assigning_a_name_to_a_locator_finding_card(card_name): # функция присвоения для сгенерированного имени карточки в локатор
    return f'//h2[text()="{card_name}"]'
