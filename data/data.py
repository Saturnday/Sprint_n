import allure
from locators.locators import MainPageLocators

@allure.epic("Тестовые данные для тестов")
class TestData:

    BASE_URL = "https://ez-route.stand.praktikum-services.ru/"

    PHONE = "+7 9999999999"

    FROM_1 = "Хамовнический вал, 34"
    TO_1   = "Зубовский бульвар, 37"

    PAIR_1 = (FROM_1, TO_1)
    PAIR_SAME = (FROM_1, FROM_1)

    TARIFFS = ["Рабочий", "Сонный", "Отпускной", "Разговорчивый", "Утешительный", "Глянцевый"]
    TARIFFS_DESCRIPTIONS = {
        "Рабочий": "Для деловых особ, которых отвлекают",
        "Сонный": "Для тех, кто не выспался",
        "Отпускной": "Если пришла пора отдохнуть",
        "Разговорчивый": "Если мысли не выходят из головы",
        "Утешительный": "Если хочется свернуться калачиком",
        "Глянцевый": "Если нужно блистать",
    }

    ORDER_FIELDS = [
            "Телефон",
            "Способ оплаты",
            "Комментарий водителю",
            "Требования к заказу",
        ]
    
    TARIFF_LOCATORS = [
    (MainPageLocators.TARIFF_WORK,      "Рабочий"),
    (MainPageLocators.TARIFF_SLEEPY,    "Сонный"),
    (MainPageLocators.TARIFF_HOLIDAY,   "Отпускной"),
    (MainPageLocators.TARIFF_TALKATIVE, "Разговорчивый"),
    (MainPageLocators.TARIFF_COMFORT,   "Утешительный"),
    (MainPageLocators.TARIFF_GLOSSY,    "Глянцевый"),
]
