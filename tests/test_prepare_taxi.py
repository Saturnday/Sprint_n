import pytest
import allure
from pages.main_page import MainPage
from data.data import TestData


@allure.suite("Подготовка к заказу такси. Ввести два разных предустановленных адреса в поля 'Откуда' и 'Куда'")
class TestPrepareTaxi:

    @allure.title("При переключении между видами маршрута (Оптимальный\Быстрый) происходит смена активного таба и пересчет времени и стоимости маршрута")
    def test_switch_tabs_changes_active_and_recalculate(self, driver):
        page = MainPage(driver)
        page.open()
        from_address, to_address = TestData.PAIR_1
        page.draw_route(from_address, to_address)
        assert page.check_switch_tabs_and_recalculate(), "Табы не переключились или маршрут не пересчитан"
    
    @allure.title("При переключении на вид маршрута Свой происходит смена активного таба и становятся активны типы передвижения (Машина, Пешком, Такси, Велосипед, Самокат, Драйв)")
    def test_custom_tab_enables_transport_types(self, driver):
        page = MainPage(driver)
        page.open()
        from_address, to_address = TestData.PAIR_1
        page.draw_route(from_address, to_address)
        assert page.check_custom_tab_enables_transport_types(), "Табы или типы передвижения не активны"

    @allure.title("Проверка, что при клике на тип транспорта он становится активным")
    def test_transport_type_tabs_activate(self, driver):
        page = MainPage(driver)
        page.open()
        from_address, to_address = TestData.PAIR_1
        page.draw_route(from_address, to_address)
        assert page.check_transport_type_tabs_activate(), "Тип транспорта не стал активным"

    @allure.title("При выборе вида маршрута Быстрый активна кнопка Вызвать такси")
    def test_fast_tab_enables_call_taxi(self, driver):
        page = MainPage(driver)
        page.open()
        from_address, to_address = TestData.PAIR_1
        page.draw_route(from_address, to_address)
        assert page.check_fast_tab_enables_call_taxi(), "Кнопка 'Вызвать такси' не активна"

    @allure.title("При выборе вида маршрута Свой, типа передвижения Драйв активна кнопка Забронировать")
    def test_custom_tab_enables_book_drive(self, driver):
        page = MainPage(driver)
        page.open()
        from_address, to_address = TestData.PAIR_1
        page.draw_route(from_address, to_address)
        assert page.check_custom_tab_enables_book_drive(), "Кнопка 'Забронировать' не активна"