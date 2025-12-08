from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Sprint_5.variables import start_url, existing_username, existing_password, card_name, card_description
from Sprint_5.locators import (MainPageLocators,
                               LoginModalWindowLocators,
                               AuthorizedUserLocators,
                               PostAnAdPageLocators,
                               assigning_a_name_to_a_locator_finding_card)

class TestCreateCard:
    def test_create_card_non_authorized_user(self, driver):
        driver.get(start_url)
        driver.find_element(*MainPageLocators.POST_AN_AD_BUTTON).click()
        WebDriverWait(driver, 2).until(expected_conditions.element_to_be_clickable(MainPageLocators.MODAL_WINDOW_REQUIRING_AUTHORIZE_TEXT))
        assert driver.find_element(*MainPageLocators.MODAL_WINDOW_REQUIRING_AUTHORIZE_TEXT).is_displayed()

    def test_create_card_authorized_user(self, driver):
        driver.get(start_url)
        driver.find_element(*MainPageLocators.LOGIN_AND_REGISTRATION_BUTTON).click()
        driver.find_element(*LoginModalWindowLocators.ENTER_EMAIL_FIELD).send_keys(existing_username)
        driver.find_element(*LoginModalWindowLocators.ENTER_PASSWORD_FIELD).send_keys(existing_password)
        driver.find_element(*LoginModalWindowLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located(AuthorizedUserLocators.USER_AVATAR))
        driver.find_element(*MainPageLocators.POST_AN_AD_BUTTON).click()
        driver.find_element(*PostAnAdPageLocators.ENTER_NAME_CARD_FIELD).send_keys(card_name)
        driver.find_element(*PostAnAdPageLocators.ENTER_PRODUCT_DESCRIPTION_CARD_FIELD).send_keys(card_description)
        driver.find_element(*PostAnAdPageLocators.ENTER_PRICE_CARD_FIELD).send_keys(10000)
        driver.find_element(*PostAnAdPageLocators.ENTER_DROPDOWN_CATEGORY_CARD_FIELD).click()
        driver.find_element(*PostAnAdPageLocators.CHOICE_VALUE_DROPDOWN_CATEGORY_CARD_FIELD).click()
        driver.find_element(*PostAnAdPageLocators.ENTER_DROPDOWN_CITY_CARD_FIELD).click()
        driver.find_element(*PostAnAdPageLocators.CHOICE_VALUE_DROPDOWN_CITY_CATEGORY_CARD_FIELD).click()
        driver.find_element(*PostAnAdPageLocators.CHOICE_NEW_RADIOBUTTON).click()
        driver.find_element(*PostAnAdPageLocators.ENTER_PUBLISH_BUTTON).click()
        WebDriverWait(driver, 2).until(expected_conditions.element_to_be_clickable(MainPageLocators.APPLY_FILTER_FOR_FIND_CARD_BUTTON))
        driver.find_element(*AuthorizedUserLocators.USER_AVATAR).click()
        WebDriverWait(driver, 2).until(expected_conditions.element_to_be_clickable(PostAnAdPageLocators.NUMBERING_OF_PAGINATION_BUTTON))
        numbering_of_pagination = driver.find_element(*PostAnAdPageLocators.NUMBERING_OF_PAGINATION_BUTTON).text.split()[-1]
        if numbering_of_pagination != '1':
            for i in range(int(numbering_of_pagination) - 1):
                WebDriverWait(driver, 2).until(expected_conditions.element_to_be_clickable(PostAnAdPageLocators.PAGINATION_BUTTON))
                pagination_button = driver.find_element(*PostAnAdPageLocators.NUMBERING_OF_PAGINATION_BUTTON)
                driver.execute_script("arguments[0].scrollIntoView();", pagination_button)
                driver.find_element(*PostAnAdPageLocators.PAGINATION_BUTTON).click()
        required_card = assigning_a_name_to_a_locator_finding_card(card_name)
        required_card_locator = (By.XPATH, required_card)
        WebDriverWait(driver, 2).until(expected_conditions.presence_of_element_located(required_card_locator))
        assert driver.find_elements(*required_card_locator)