from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Sprint_5.variables import start_url, existing_username, existing_password
from Sprint_5.locators import (MainPageLocators,
                               LoginModalWindowLocators,
                               AuthorizedUserLocators)

class TestLogoutUser:
    def test_logout_user(self, driver):
        driver.get(start_url)
        driver.find_element(*MainPageLocators.LOGIN_AND_REGISTRATION_BUTTON).click()
        driver.find_element(*LoginModalWindowLocators.ENTER_EMAIL_FIELD).send_keys(existing_username)
        driver.find_element(*LoginModalWindowLocators.ENTER_PASSWORD_FIELD).send_keys(existing_password)
        driver.find_element(*LoginModalWindowLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 2).until(expected_conditions.element_to_be_clickable(AuthorizedUserLocators.EXITE_BUTTON))
        driver.find_element(*AuthorizedUserLocators.EXITE_BUTTON).click()
        WebDriverWait(driver, 2).until(expected_conditions.element_to_be_clickable(MainPageLocators.LOGIN_AND_REGISTRATION_BUTTON))
        assert driver.find_element(*MainPageLocators.LOGIN_AND_REGISTRATION_BUTTON).is_displayed()
        assert len(driver.find_elements(*AuthorizedUserLocators.USER_AVATAR)) == 0
        assert len(driver.find_elements(*AuthorizedUserLocators.USER_NAME)) == 0