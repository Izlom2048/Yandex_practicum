from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Sprint_5.variables import start_url, existing_username, existing_password, email, current_url
from Sprint_5. locators import (MainPageLocators,
                               LoginModalWindowLocators,
                               RegisterModalWindowLocators,
                               AuthorizedUserLocators)

class TestRegistrationUser:
    def test_registration_user(self, driver):
        driver.get(start_url)
        driver.find_element(*MainPageLocators.LOGIN_AND_REGISTRATION_BUTTON).click()
        driver.find_element(*LoginModalWindowLocators.NO_ACCOUNT_BUTTON).click()
        driver.find_element(*RegisterModalWindowLocators.ENTER_EMAIL_FIELD).send_keys(email)
        driver.find_element(*RegisterModalWindowLocators.ENTER_PASSWORD_FIELD).send_keys("01yRb0D$7pu)P_z")
        driver.find_element(*RegisterModalWindowLocators.ENTER_SUBMIT_PASSWORD_FIELD).send_keys("01yRb0D$7pu)P_z")
        driver.find_element(*RegisterModalWindowLocators.CREATE_ACCOUNT_BUTTON).click()
        assert driver.current_url == current_url
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(AuthorizedUserLocators.USER_AVATAR))
        assert driver.find_element(*AuthorizedUserLocators.USER_AVATAR).is_displayed()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(AuthorizedUserLocators.USER_NAME))
        assert driver.find_element(*AuthorizedUserLocators.USER_NAME).is_displayed()

    def test_registration_user_with_invalid_email(self, driver):
        driver.get(start_url)
        driver.find_element(*MainPageLocators.LOGIN_AND_REGISTRATION_BUTTON).click()
        driver.find_element(*LoginModalWindowLocators.NO_ACCOUNT_BUTTON).click()
        driver.find_element(*RegisterModalWindowLocators.ENTER_EMAIL_FIELD).send_keys('invalid@mail')
        driver.find_element(*RegisterModalWindowLocators.ENTER_PASSWORD_FIELD).send_keys("01yRb0D$7pu)P_z")
        driver.find_element(*RegisterModalWindowLocators.ENTER_SUBMIT_PASSWORD_FIELD).send_keys("01yRb0D$7pu)P_z")
        driver.find_element(*RegisterModalWindowLocators.CREATE_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(RegisterModalWindowLocators.RED_VALIDATION_REGISTER_FIELD))
        assert len(driver.find_elements(*RegisterModalWindowLocators.RED_VALIDATION_REGISTER_FIELD)) == 3
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(RegisterModalWindowLocators.VALIDATION_REGISTER_ERROR))
        assert driver.find_element(*RegisterModalWindowLocators.VALIDATION_REGISTER_ERROR).is_displayed()

    def test_registration_user_with_existing_credentials(self, driver):
        driver.get(start_url)
        driver.find_element(*MainPageLocators.LOGIN_AND_REGISTRATION_BUTTON).click()
        driver.find_element(*LoginModalWindowLocators.NO_ACCOUNT_BUTTON).click()
        driver.find_element(*RegisterModalWindowLocators.ENTER_EMAIL_FIELD).send_keys(existing_username)
        driver.find_element(*RegisterModalWindowLocators.ENTER_PASSWORD_FIELD).send_keys(existing_password)
        driver.find_element(*RegisterModalWindowLocators.ENTER_SUBMIT_PASSWORD_FIELD).send_keys(existing_password)
        driver.find_element(*RegisterModalWindowLocators.CREATE_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(RegisterModalWindowLocators.RED_VALIDATION_REGISTER_FIELD))
        assert len(driver.find_elements(*RegisterModalWindowLocators.RED_VALIDATION_REGISTER_FIELD)) == 3
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(RegisterModalWindowLocators.VALIDATION_REGISTER_ERROR))
        assert driver.find_element(*RegisterModalWindowLocators.VALIDATION_REGISTER_ERROR).is_displayed()
