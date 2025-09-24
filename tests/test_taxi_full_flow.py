import pytest
import allure
from data.data import TestData
from pages.main_page import MainPage

@allure.suite("Заказ тарифа Такси. Ввести два разных предустановленных адреса в поля 'Откуда' и 'Куда', выбрать вид маршрута Быстрый, нажать кнопку 'Вызвать такси'")
class TestTaxiFlow:
    
    @allure.step("Открывается форма заказа со всеми 6 тарифами по ТЗ, один из них активный")
    def test_open_taxi_form_has_6_tariffs_and_one_active(self, driver):
        page = MainPage(driver)
        page.open()
        from_address, to_address = TestData.PAIR_1
        page.draw_route(from_address, to_address)
        page.click_fast_button()
        page.click_call_taxi_button()

        # Проверяем, что на форме ровно 6 тарифных кнопок
        tariffs = page.get_all_tariffs()
        assert len(tariffs) == 6, "Должно быть 6 тарифов"

        # Проверяем, что только один из них активен
        active_tariffs = page.get_active_tariffs()
        assert len(active_tariffs) == 1, "Должен быть ровно один активный тариф"

    @pytest.mark.parametrize(
        "tariff_index, xfail",
        [
            (i, tariff_name != "Рабочий")  # xfail=True для всех, кроме "Рабочий"
            for i, (_, tariff_name) in enumerate(MainPage(None).get_tariff_locators())
        ]
    )
    def test_tariff_tooltips_match_spec(self, driver, tariff_index, xfail):
        page = MainPage(driver)
        tariff_locators = page.get_tariff_locators()
        tariff_locator, tariff_name = tariff_locators[tariff_index]
        
        if xfail:
            pytest.xfail(f"Баг: описание тарифа '{tariff_name}' не совпадает с ТЗ")
            
        page.open()
        from_address, to_address = TestData.PAIR_1
        page.draw_route(from_address, to_address)
        page.click_fast_button()
        page.click_call_taxi_button()

        expected_desc = TestData.TARIFFS_DESCRIPTIONS[tariff_name]
        button = page.find_tariff_by_locator(tariff_locator)
        assert button is not None, f"Тарифная кнопка не найдена"
        card = button.find_element("xpath", "..")
        page.scroll_and_click(card)

        i_button = page.get_tariff_info_button(tariff_index)
        page.hover_on_info_button(i_button)

        tooltip_title = page.get_tooltip_title()
        tooltip_desc = page.get_tooltip_description()
        assert tariff_name in tooltip_title.text, f"Заголовок тултипа не совпадает для '{tariff_name}'"
        assert expected_desc in tooltip_desc.text, f"Описание тултипа не совпадает для '{tariff_name}'"

        page.move_cursor_to_body()

    @allure.step("Под тарифами отображается блок с полями Телефон, Способ оплаты, Комментарий водителю, Требования к заказу Заказ тарифа Такси.")
    @pytest.mark.parametrize("field_text", [
        "Телефон",
        "Способ оплаты",
        "Комментарий водителю",
        "Требования к заказу",
    ])
    def test_order_form_field_present(self, driver, field_text):
        page = MainPage(driver)
        page.open()
        from_address, to_address = TestData.PAIR_1
        page.draw_route(from_address, to_address)
        page.click_fast_button()
        page.click_call_taxi_button()

        order_block = page.get_order_form_block()
        block_text = order_block.get_attribute("innerText")
        assert field_text in block_text, f"Текст '{field_text}' не найден в блоке заказа"
