from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Sprint_5.variables import start_url, existing_username, existing_password
from Sprint_5.locators import (MainPageLocators,
                               LoginModalWindowLocators,
                               AuthorizedUserLocators)

class TestExistingLoginUser:
    def test_existing_login_user(self, driver):
        driver.get(start_url)
        driver.find_element(*MainPageLocators.LOGIN_AND_REGISTRATION_BUTTON).click()
        driver.find_element(*LoginModalWindowLocators.ENTER_EMAIL_FIELD).send_keys(existing_username)
        driver.find_element(*LoginModalWindowLocators.ENTER_PASSWORD_FIELD).send_keys(existing_password)
        driver.find_element(*LoginModalWindowLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(AuthorizedUserLocators.USER_AVATAR))
        assert driver.find_element(*AuthorizedUserLocators.USER_AVATAR).is_displayed()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(AuthorizedUserLocators.USER_NAME))
        assert driver.find_element(*AuthorizedUserLocators.USER_NAME).is_displayed()