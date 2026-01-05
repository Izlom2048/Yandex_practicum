from selenium.webdriver.common.by import By

class MainPageLocators:
    QUESTIONS_ON_THE_MAIN_BUTTON = (By.XPATH, '//*[@id="accordion__heading-{}"]')
    ANSWER_ON_THE_MAIN_BUTTON = (By.XPATH, '//*[@id="accordion__panel-{}"]//p')
    QUESTIONS_ON_THE_MAIN_TO_SCROLL_BUTTON = (By.XPATH, '//*[@id="accordion__heading-7"]')
