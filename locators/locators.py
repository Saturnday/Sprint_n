from selenium.webdriver.common.by import By


class MainPageLocators:
    
    LABEL_FROM = (By.ID, 'from') 
    LABEL_TO = (By.ID, 'to')

    # Кнопки выбора типа маршрута
    BUTTON_MY = (By.XPATH, "//div[text()='Свой']")
    BUTTON_FAST = (By.XPATH, "//div[text()='Быстрый']")
    BUTTON_OPTIMAL = (By.XPATH, "//div[text()='Оптимальный']")

    # Табы выбора вида маршрута (Свой)
    VEHICLE_BLOCK   = (By.XPATH, "//div[@class='types-container']/div")

    CAR      = (By.XPATH, "//div[@class='types-container']/div[contains(@class, 'type')][1]")
    WALK     = (By.XPATH, "//div[@class='types-container']/div[contains(@class, 'type')][2]")
    TAXI     = (By.XPATH, "//div[@class='types-container']/div[contains(@class, 'type')][3]")
    BIKE     = (By.XPATH, "//div[@class='types-container']/div[contains(@class, 'type')][4]")
    SAMOKAT  = (By.XPATH, "//div[@class='types-container']/div[contains(@class, 'type')][5]")
    DRIVE    = (By.XPATH, "//div[@class='types-container']/div[contains(@class, 'type drive')]")

    # Индикаторы видов маршрута
    INDICATOR_CAR      = (By.XPATH, "//div[contains(text(), 'Авто')]")
    INDICATOR_WALK     = (By.XPATH, "//div[contains(text(), 'Пешком')]")
    INDICATOR_TAXI     = (By.XPATH, "//div[contains(text(), 'Такси')]")
    INDICATOR_BIKE     = (By.XPATH, "//div[contains(text(), 'Велосипед')]")
    INDICATOR_SAMOKAT  = (By.XPATH, "//div[contains(text(), 'Самокат')]")
    INDICATOR_DRIVE    = (By.XPATH, "//div[contains(text(), 'Драйв')]")

    # Проверка отрисовки маршрута и точек на карте
    MAP_EVENTS_PANE = (By.CSS_SELECTOR, "ymaps.ymaps-2-1-79-events-pane.ymaps-2-1-79-user-selection-none")
    MAP_TO = (By.XPATH, "//div[contains(text(), 'Зубовский')]")
    MAP_FROM = (By.XPATH, "//div[contains(text(), 'Хамовнический')]")

    # Проверка минут
    MAP_IN_PROGRESS = (By.XPATH, "//div[contains(text(), 'В пути')]")
    MAP_IN_PROGRESS_0 = (By.XPATH, "//div[contains(text(), 'В пути 0 мин.')]")
    MAP_AUTO_FREE = (By.XPATH, "//div[contains(text(), 'Авто Бесплатно')]")

    # Активные табы
    ACTIVE_TAB_MY = (By.XPATH, "//div[@class='mode active' and text()='Свой']")
    ACTIVE_TAB_FAST = (By.XPATH, "//div[@class='mode active' and text()='Быстрый']")
    ACTIVE_TAB_OPTIMAL = (By.XPATH, "//div[@class='mode active' and text()='Оптимальный']")

    # Активные типы транспорта
    CAR_ACTIVE     = (By.XPATH, "//div[@class='type active']//img[contains(@src, 'car-active')]")
    WALK_ACTIVE    = (By.XPATH, "//div[@class='type active']//img[contains(@src, 'walk-active')]")
    TAXI_ACTIVE    = (By.XPATH, "//div[@class='type active']//img[contains(@src, 'taxi-active')]")
    BIKE_ACTIVE    = (By.XPATH, "//div[@class='type active']//img[contains(@src, 'bike-active')]")
    SAMOKAT_ACTIVE = (By.XPATH, "//div[@class='type active']//img[contains(@src, 'scooter-active')]")
    DRIVE_ACTIVE   = (By.XPATH, "//div[@class='type active']//img[contains(@src, 'drive-active')]")

    TRANSPORT_TYPES = [
        (CAR, CAR_ACTIVE),
        (WALK, WALK_ACTIVE),
        (TAXI, TAXI_ACTIVE),
        (BIKE, BIKE_ACTIVE),
        (SAMOKAT, SAMOKAT_ACTIVE),
        (DRIVE, DRIVE_ACTIVE),
    ]
    # Кнопка Вызвать такси
    CALL_TAXI_BUTTON = (By.XPATH, "//button[contains(text(), 'Вызвать такси')]")
    BOOK_BUTTON = (By.XPATH, "//button[contains(text(), 'Забронировать')]")

    # Локаторы тарифов
    TARIFF_WORK      = (By.XPATH, "//div[@class='tcard-title' and text()='Рабочий']")
    TARIFF_SLEEPY    = (By.XPATH, "//div[@class='tcard-title' and text()='Сонный']")
    TARIFF_HOLIDAY   = (By.XPATH, "//div[@class='tcard-title' and text()='Отпускной']")
    TARIFF_TALKATIVE = (By.XPATH, "//div[@class='tcard-title' and text()='Разговорчивый']")
    TARIFF_COMFORT   = (By.XPATH, "//div[@class='tcard-title' and text()='Утешительный']")
    TARIFF_GLOSSY    = (By.XPATH, "//div[@class='tcard-title' and text()='Глянцевый']")

    TARIFFS = [TARIFF_WORK, TARIFF_SLEEPY, TARIFF_HOLIDAY, TARIFF_TALKATIVE, TARIFF_COMFORT, TARIFF_GLOSSY]

    TARIFF_LOCATORS = [
    (TARIFF_WORK,      "Рабочий"),
    (TARIFF_SLEEPY,    "Сонный"),
    (TARIFF_HOLIDAY,   "Отпускной"),
    (TARIFF_TALKATIVE, "Разговорчивый"),
    (TARIFF_COMFORT,   "Утешительный"),
    (TARIFF_GLOSSY,    "Глянцевый"),
]

    TARIFFS = (By.XPATH, "//button[contains(@class, 'tcard')]")

    TARIFF_ACTIVE = (By.XPATH, "//div[(@class = 'tcard active')]")

    # Локаторы для i-кнопок тарифов (индексация с 1)
    I_BUTTON_WORK      = (By.XPATH, "(//button[contains(@class, 'i-button')])[1]")
    I_BUTTON_SLEEPY    = (By.XPATH, "(//button[contains(@class, 'i-button')])[2]")
    I_BUTTON_HOLIDAY   = (By.XPATH, "(//button[contains(@class, 'i-button')])[3]")
    I_BUTTON_TALKATIVE = (By.XPATH, "(//button[contains(@class, 'i-button')])[4]")
    I_BUTTON_COMFORT   = (By.XPATH, "(//button[contains(@class, 'i-button')])[5]")
    I_BUTTON_GLOSSY    = (By.XPATH, "(//button[contains(@class, 'i-button')])[6]")

    @staticmethod
    def i_button_by_index(index):
        return (By.XPATH, f"(//button[contains(@class, 'i-button')])[{index+1}]")
    
    TOOLTIP_TITLE = (By.CSS_SELECTOR, ".i-floating .i-title")
    TOOLTIP_DESC  = (By.CSS_SELECTOR, ".i-floating .i-dPrefix")

    @staticmethod
    def tariff_card_by_index(idx):
        # Только прямые потомки .tariff-cards
        return (By.XPATH, f"(//div[contains(@class, 'tariff-cards')]/div[contains(@class, 'tcard')])[{idx + 1}]")


    I_BUTTON_ACTIVE = (By.XPATH, "(//div[contains(@class, 'tariff-cards')]/div[contains(@class, 'tcard active')])[1]")

    ORDER_FORM_BLOCK = (By.CLASS_NAME, "form")

    #Вызов такси - рабочий тариф
    LAPTOP_SLIDER = (By.CSS_SELECTOR, ".slider.round")
    ORDER_REQUIREMENTS = (By.XPATH, "//div[contains(text(), 'Требования к заказу')]")
    PAYMENT_METHOD = (By.XPATH, "//div[contains(@class, 'payment-method')]")
    PHONE_INPUT = (By.XPATH, "//div[contains(@class, 'np-text') and text()='Телефон']")
    SMS_CODE_INPUT = (By.ID, "code")
    ACCEPT_CODE = (By.XPATH, "//button[contains(text(), 'Подтвердить')]")
    CONFIRM_ORDER = (By.XPATH, "//span[contains(text(), 'Ввести номер и заказать')]")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "order-header-title")

    # Локаторы для проверки заказа
    ORDER_BTN_GROUP_DETAILS = (By.XPATH,"//div[contains(@class, 'order-btn-group')]//div[(text())='Детали']")
    ORDER_BTN_CANCEL = (By.XPATH, "//div[contains(@class, 'order-btn-group')]//div[(text())='Отменить']")
    ORDER_HEADER_TIME = (By.XPATH, "//div[contains(@class, 'order-header-time')]")
    ORDER_HEADER_TITLE = (By.XPATH, "//div[contains(text(), 'Поиск машины')]")

    #Окно совершенного заказа Такси: 
    #Заголовок: n мин. и приедет >
    MIN_ARRIVE = (By.CLASS_NAME, 'order-header-title')
    #Номер автомобиля и картинка тарифа в правом верхнем углу
    ORDER_NUMBER = (By.CSS_SELECTOR, ".number")
    ORDER_CAR_IMG = (By.XPATH, "//img[contains(@src, '.svg') and @alt='Car']")
    #Блок с информацией о водителе: Имя, фото, рейтинг в правом верхнем углу фото
    ORDER_BUTTONS = (By.CSS_SELECTOR, ".order-buttons")
    ORDER_BTN_GROUPS = (By.CSS_SELECTOR, ".order-buttons .order-btn-group")
    ORDER_BTN_RATING = (By.CSS_SELECTOR, ".order-btn-rating")
    ORDER_BTN_GROUP_FIRST = (By.CSS_SELECTOR, ".order-buttons .order-btn-group:nth-child(1)")
    ORDER_BTN_NAME = (By.CSS_SELECTOR, ".order-btn-group > div:not([class])")
    ORDER_BTN_GROUP_FIRST_IMG = (By.CSS_SELECTOR, ".order-buttons .order-btn-group:nth-child(1) img")

    # Cтоимость поездки
    ORDER_DETAILS_CONTENT_4 = (By.XPATH, "//*[contains(text(), 'Стоимость')]")
    ORDER_DETAILS_PRICE_ANY = (By.XPATH, "//*[contains(text(), 'Стоимость')]")
    TCARD_PRICE = (By.CSS_SELECTOR, ".tcard-price")
    BUTTON_CANCEL = (By.XPATH, "//div[normalize-space(text())='Отменить']")
    BUTTON_DETAILS = (By.XPATH, "//div[contains(@class, 'order-btn-group')][3]//div[normalize-space(text())='Детали']")
    #(By.XPATH, "//div[normalize-space(text())='Детали']")

    TCARD_PRICE_AFTER_CLICK = (By.XPATH, "//*[contains(text(),'Стоимость')]")

    ACTIVE_DRIVE = (By.XPATH, "//div[contains(@class,'type') and contains(@class,'active')]//img[contains(@src,'drive')]/..")

    ORDER_DETAILS_TRIP_PRICE = (
    By.XPATH,
    "//div[contains(@class,'order-details-content')][.//div[contains(@class,'o-d-h') and contains(normalize-space(),'Еще про поездку')]]"
    "//div[contains(@class,'o-d-sh')]"
)