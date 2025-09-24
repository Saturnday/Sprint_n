import pytest
import allure
from pages.main_page import MainPage


@allure.suite("Заказ Такси. Ввести два разных предустановленных адреса в поля 'Откуда' и 'Куда', выбрать вид маршрута Быстрый, нажать кнопку 'Вызвать такси'")
class TestDrive:
    @allure.step("Выбираем тариф Рабочий, включаем чекбокс Столик для ноутбука, нажимаем кнопку Ввести номер и заказать - Появляется окно ожидания машины")
    def test_drive_booking(self, driver):
        page = MainPage(driver)
        page.open()
        
        page.call_a_fast_taxi()
        page.set_working_tariff()

        assert page.check_flow_of_ordering()

    @allure.step("Дождаться окончания таймера поиска машины - Отображается окно совершенного заказа")
    def test_waiting_for_car_success(self, driver):
        page = MainPage(driver)
        page.open()
        
        page.call_a_fast_taxi()
        page.set_working_tariff()

        assert page.check_order_window_elements()

    
    @allure.step("Проверить, что цена такая же, как на тарифе")
    def test_tariff_price(self, driver):
        page = MainPage(driver)
        page.open()

        page.call_a_fast_taxi()
        price = page.set_working_tariff(calculate_price=True)
        assert page.check_details_button_in_trip_block(price)

    @pytest.mark.xfail(reason="Баг в приложении: кнопка Отмена не закрывает окно заказа")
    def test_cancel_button_closes_window(self, driver):
        page = MainPage(driver)
        page.open()
        
        page.call_a_fast_taxi()
        page.set_working_tariff()

        assert page.check_cancel_button_closes_window()