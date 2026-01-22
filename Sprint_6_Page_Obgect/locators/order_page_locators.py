from selenium.webdriver.common.by import By

class OrderPageFirstScreenLocators:
    COOKIE_BUTTON = (By. CLASS_NAME, "App_CookieButton__3cvqF")
    FIRST_ORDER_BUTTON = (By.CLASS_NAME, "Button_Button__ra12g")
    SECOND_ORDER_BUTTON = (By.CLASS_NAME, "Button_UltraBig__UU3Lp")
    ENTER_ORDER_DATA_FIELD = (By.XPATH, '//input[@placeholder="{}"]')
    METRO_STATION_SELECTION = (By.XPATH, "//button[@value='{}']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

class OrderPageSecondScreenLocators:
    ORDER_DATE_FIELD = (By.XPATH, '//input[@placeholder="* Когда привезти самокат"]')
    ENTER_RENTAL_PERIOD_FIELD = (By.CLASS_NAME, "Dropdown-control")
    TITLE_PAGE = (By.CLASS_NAME, "Order_Header__BZXOb")
    ENTER_PERIOD_SELECTION = (By.XPATH, "//div[@class='Dropdown-option' and text()='{}']")
    ENTER_COLOR_CHECKBOX = (By.ID, "{}")
    ENTER_COMMENT_FOR_THE_COURIER_FIELD = (By.XPATH, '//input[@placeholder="Комментарий для курьера"]')
    ORDER_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Заказать']")
    YES_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Да']")
    ORDER_CONFIRMATION = (By.XPATH, "//div[@class='Order_ModalHeader__3FDaJ' and text()='Заказ оформлен']")
    SEE_STATE_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Посмотреть статус']")
    IMAGE_SCOOTER_LINK = (By.XPATH, "//img[@alt='Scooter']")
    IMAGE_YANDEX_LINK = (By.XPATH, "//img[@alt='Yandex']")
