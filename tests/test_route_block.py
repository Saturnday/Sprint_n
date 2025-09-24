import pytest
import allure
from data.data import TestData
from pages.main_page import MainPage
from locators.locators import MainPageLocators #нужны для параметризации



@allure.suite("Проверка отрисовка маршрута, блока с выбором маршрута")
class TestRoute:

    @allure.step("Две точки на карте появляются после ввода двух разных адресов")
    def test_two_different_addresses_two_markers(self, driver):

        page = MainPage(driver)
        page.open()

        from_address, to_address = TestData.PAIR_1

        page.draw_route(from_address, to_address)

        assert page.is_map_from_visible(), "Точка 'Откуда' должна отображаться на карте"
        assert page.is_map_to_visible(), "Точка 'Куда' должна отображаться на карте"



    @pytest.mark.parametrize(
        "button_locator, VEHICLE_BLOCK",
        [
            (MainPageLocators.BUTTON_MY, MainPageLocators.VEHICLE_BLOCK),
            (MainPageLocators.BUTTON_FAST, MainPageLocators.VEHICLE_BLOCK),
            (MainPageLocators.BUTTON_OPTIMAL, MainPageLocators.VEHICLE_BLOCK),
        ]
    )
    @allure.step("При вводе двух разных предустановленных адресов в поля 'Откуда' и 'Куда' под выбором адресов отображается блок с выбором маршрута")
    def test_route_block_appears(self, driver, button_locator, VEHICLE_BLOCK):
        page = MainPage(driver)
        page.open()
        from_address, to_address = TestData.PAIR_1
        page.draw_route(from_address, to_address)
        page.click_to_element_with_wait(button_locator)
        assert page.is_route_selection_block_visible(VEHICLE_BLOCK), "Блок с выбором маршрута не отображается"

    @allure.step("При вводе одинакового адреса в поля 'Откуда' и 'Куда' под выбором адресов отображается блок с выбором маршрута с текстом 'Авто Бесплатно В пути 0 мин'")
    def test_route_block_with_same_addresses(self, driver):
        page = MainPage(driver)
        page.open()
        from_address, to_address = TestData.PAIR_SAME
        page.draw_route(from_address, to_address)
        assert page.check_route_block_and_text(), "Блок с выбором маршрута или текст не отображается"
