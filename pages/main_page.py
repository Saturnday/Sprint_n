import allure
import pytest
from data.data import TestData
from pages.base_page import BasePage
from locators.locators import MainPageLocators


class MainPage(BasePage):

    URL = 'https://ez-route.stand.praktikum-services.ru/'

    @allure.step("Открыть главную страницу")
    def open(self, url=None):
        self.open_url(url or self.URL)

    @allure.step('Проверка отображения точек на карте')
    def is_map_from_visible(self):
        return self.find_element_with_wait(MainPageLocators.MAP_FROM)

    @allure.step('Проверка отображения точки "Куда" на карте')
    def is_map_to_visible(self):
        return self.find_element_with_wait(MainPageLocators.MAP_TO)

    @allure.step("Проверка отрисовки маршрута")
    def is_route_block_visible(self):
        return self.find_element_with_wait(MainPageLocators.MAP_EVENTS_PANE)
    
    @allure.step("Проверка отображения блока выбора маршрута")
    def is_route_selection_block_visible(self, car_locator):
        return self.find_element_with_wait(car_locator)

    @allure.step("Отрисовка маршрута")
    def draw_route(self, from_address, to_address):

        self.find_element_with_wait(MainPageLocators.LABEL_FROM)
        self.find_element_with_wait(MainPageLocators.LABEL_FROM).send_keys(from_address)

        self.find_element_with_wait(MainPageLocators.LABEL_TO)
        self.find_element_with_wait(MainPageLocators.LABEL_TO).send_keys(to_address)



    @allure.step("Выбор типа маршрута")
    @pytest.mark.parametrize(
        "button_locator, car_locator",
        [
            (MainPageLocators.BUTTON_MY, MainPageLocators.CAR),
            (MainPageLocators.BUTTON_FAST, MainPageLocators.CAR),
            (MainPageLocators.BUTTON_OPTIMAL, MainPageLocators.CAR),
        ]
    )

    @allure.step("Проверка, что при клике на тип маршрута отображается соответствующий блок с типом транспорта")
    def test_route_selection_block_visible(page, button_locator, car_locator):
        page.click_to_element_with_wait(button_locator)
        assert page.find_element_with_wait(car_locator)

    @allure.step("Вызов такси с быстрым маршрутом")
    def call_a_fast_taxi(self):
        from_address, to_address = TestData.PAIR_1
        self.draw_route(from_address, to_address)
        self.click_to_element_with_wait(MainPageLocators.BUTTON_FAST)
        self.click_to_element_with_wait(MainPageLocators.CALL_TAXI_BUTTON)

    @allure.step("Проверка потока заказа")
    def check_flow_of_ordering(self):
        try:
            self.wait_until_element_is_visible(MainPageLocators.ORDER_HEADER_TITLE, timeout=10)
            self.wait_until_element_is_visible(MainPageLocators.ORDER_HEADER_TIME, timeout=10)
            self.wait_until_element_is_visible(MainPageLocators.ORDER_FORM_BLOCK, timeout=30)
            self.wait_until_element_is_visible(MainPageLocators.ORDER_BTN_CANCEL, timeout=10)
            self.wait_until_element_is_visible(MainPageLocators.ORDER_BTN_GROUP_DETAILS, timeout=10)
            return True
        except:
            return False

    @allure.step("Get price from tariff card")
    @classmethod
    def get_price_from_tariff_card(cls):
        price_elem = cls.find_element_with_wait(MainPageLocators.TCARD_PRICE)
        price_text = price_elem.text.strip()
        return price_text

    @allure.step('Настроить тариф "Рабочий"')
    def set_working_tariff(self, calculate_price=False):
        # Получаем исходную цену перед кликами
        initial_price_text = ""
        price_digits = None
        
        if calculate_price:
            price_elem = self.find_element_with_wait(MainPageLocators.TCARD_PRICE)
            if price_elem:
                initial_price_text = price_elem.text.strip()
        
        # Выбираем тариф "Рабочий"
        self.click_to_element_with_wait(MainPageLocators.TARIFF_WORK)
        self.click_to_element_with_wait(MainPageLocators.ORDER_REQUIREMENTS)
        
        # Клик по слайдеру (должен изменить цену)
        self.click_to_element_with_wait(MainPageLocators.LAPTOP_SLIDER)
        
        # Дожидаемся изменения цены
        if calculate_price and initial_price_text:
            try:
                # Пробуем дождаться изменения текста с большим таймаутом
                new_price_text = self.wait_until_text_changes(MainPageLocators.TCARD_PRICE, initial_price_text, timeout=15)

                price_digits = ''.join(filter(str.isdigit, new_price_text))
                price_elem = self.find_element_with_wait(MainPageLocators.TCARD_PRICE)
                if price_elem:
                    new_price_text = price_elem.text.strip()
                    price_digits = ''.join(filter(str.isdigit, new_price_text))
            except:
                price_digits = None
        
        # Подтверждаем заказ
        self.click_to_element_with_wait(MainPageLocators.CONFIRM_ORDER)
        
        # Возвращаем цену
        if calculate_price:
            return price_digits



    @allure.step("Ожидание подачи машины")
    def wait_for_car_coming(self):
        self.wait_until_element_is_visible(MainPageLocators.ORDER_BUTTONS, timeout=30)


    @allure.step('Проверить шапку заказа')
    def check_order_header(self):
        try:
            # Найти все группы кнопок
            btn_groups = self.find_elements_with_wait(MainPageLocators.ORDER_BTN_GROUPS)
            if not btn_groups:
                return False

            # Первая группа
            first_group = btn_groups[0]

            # Проверка рейтинга (ищем внутри первой группы)
            rating_elems = self.find_child_elements_with_wait(first_group, MainPageLocators.ORDER_BTN_RATING)
            if not rating_elems:
                return False
            rating_text = rating_elems[0].text.strip()
            rating_valid = rating_text.replace(',', '.').replace(' ', '').replace('.', '', 1).isdigit()
            if not rating_valid:
                return False

            # Проверка картинки (глобальный локатор как и было)
            car_img = self.find_element_with_wait(MainPageLocators.ORDER_CAR_IMG, timeout=30)
            if car_img is None:
                return False

            # Проверка имени (внутри первой группы)
            name_elems = self.find_child_elements_with_wait(first_group, MainPageLocators.ORDER_BTN_NAME)
            if not name_elems:
                return False
            name_text = name_elems[0].text.strip()
            if not name_text:
                return False

            return True
        except Exception:
            return False
        
    @allure.step('Проверить элементы окна заказа')
    def check_order_window_elements(self):
        try:
            self.wait_until_element_is_visible(MainPageLocators.ORDER_BUTTONS, timeout=60)
            self.find_element_with_wait(MainPageLocators.ORDER_CAR_IMG, timeout=60)
            btn_groups = self.find_elements_with_wait(MainPageLocators.ORDER_BTN_GROUPS)
            if not btn_groups:
                return False

            rating_elem = self.find_element_with_wait(MainPageLocators.ORDER_BTN_RATING)
            if rating_elem.text.strip() == "":
                return False

            if not self.find_element_with_wait(MainPageLocators.ORDER_CAR_IMG, timeout=30):
                return False

            if not self.find_element_with_wait(MainPageLocators.ORDER_BTN_NAME):
                return False

            first_group = self.find_element_with_wait(MainPageLocators.ORDER_BTN_GROUP_FIRST)
            if first_group is None:
                return False

            rating_elem = self.find_child_element_by_class(first_group, "order-btn-rating")
            if rating_elem is None:
                return False
            rating_text = rating_elem.text.strip()
            if not rating_text:
                return False
            img_elem = self.find_element_with_wait(MainPageLocators.ORDER_BTN_GROUP_FIRST_IMG)
            if img_elem is None:
                return False
            img_src = img_elem.get_attribute("src")
            if not img_src or not img_src.endswith(".svg"):
                return False
            name_elems = self.find_child_elements_with_wait(first_group, MainPageLocators.ORDER_BTN_NAME)
            if not name_elems or len(name_elems) < 1:
                return False
            if len(name_elems) < 1 or name_elems[0] is None:
                return False
            name_text = name_elems[0].text.strip()
            if not name_text:
                return False
            #Кнопки: Отменить, Детали
            if not self.find_element_with_wait(MainPageLocators.ORDER_BTN_CANCEL):
                return False
            if not self.find_element_with_wait(MainPageLocators.ORDER_BTN_GROUP_DETAILS):
                return False
            return True
        except Exception:
            return False
    
    @allure.step("Проверка переключения вкладок и перерасчета маршрута")
    def check_switch_tabs_and_recalculate(self):
        self.click_to_element_with_wait(MainPageLocators.BUTTON_FAST)
        if not self.find_element_with_wait(MainPageLocators.ACTIVE_TAB_FAST):
            return False

        old_text = self.find_element_with_wait(MainPageLocators.MAP_IN_PROGRESS).text

        self.click_to_element_with_wait(MainPageLocators.BUTTON_OPTIMAL)
        if not self.find_element_with_wait(MainPageLocators.ACTIVE_TAB_OPTIMAL):
            return False

        new_text = self.wait_until_text_changes(MainPageLocators.MAP_IN_PROGRESS, old_text)
        if old_text == new_text:
            return False

        return True
    
    @allure.step("Проверка, что при переключении на вид маршрута Свой становятся активны типы передвижения (Машина, Пешком, Такси, Велосипед, Самокат, Драйв)")
    def check_custom_tab_enables_transport_types(self):
        self.click_to_element_with_wait(MainPageLocators.BUTTON_MY)
        if not self.find_element_with_wait(MainPageLocators.ACTIVE_TAB_MY):
            return False
        if not self.find_element_with_wait(MainPageLocators.CAR):
            return False
        if not self.find_element_with_wait(MainPageLocators.WALK):
            return False
        if not self.find_element_with_wait(MainPageLocators.TAXI):
            return False
        if not self.find_element_with_wait(MainPageLocators.BIKE):
            return False
        if not self.find_element_with_wait(MainPageLocators.SAMOKAT):
            return False
        if not self.find_element_with_wait(MainPageLocators.DRIVE):
            return False
        return True
    
    @allure.step("Проверка, что при клике на тип транспорта он становится активным")
    def check_transport_type_tabs_activate(self):
        # Клик по вкладке "Свой"
        self.click_to_element_with_wait(MainPageLocators.BUTTON_MY, timeout=15)
        
        # Проверяем все вкладки кроме Drive
        for tab_locator, active_locator in MainPageLocators.TRANSPORT_TYPES:
            if 'drive' not in str(tab_locator):
                self.click_to_element_with_wait(tab_locator)
                if self.find_element_with_wait(active_locator) is None:
                    return False
    
        # Особая обработка для Drive
        drive_tab = self.find_element_with_wait(MainPageLocators.DRIVE)
        if drive_tab:
            self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", drive_tab)
            drive_tab.click()

            drive_active = self.driver.find_element(*MainPageLocators.ACTIVE_DRIVE)
            if drive_active is None:
                return False
        else:
            return False
            
        return True

    @allure.step("Проверка, что при выборе вида маршрута Быстрый активна кнопка Вызвать такси")
    def check_fast_tab_enables_call_taxi(self):
        self.click_to_element_with_wait(MainPageLocators.BUTTON_FAST)
        if not self.is_element_active(MainPageLocators.CALL_TAXI_BUTTON):
            return False
        return True

    @allure.step("Проверка, что при выборе вида маршрута Свой, типа передвижения Драйв активна кнопка Забронировать")
    def check_custom_tab_enables_book_drive(self):
        self.click_to_element_with_wait(MainPageLocators.BUTTON_MY)
        
        # Wait for tab activation
        self.wait_until_element_is_visible(MainPageLocators.ACTIVE_TAB_MY, timeout=5)
        
        # Click on Drive and ensure it's visible
        drive_tab = self.find_element_with_wait(MainPageLocators.DRIVE, timeout=10)
        if not drive_tab:
            return False
            
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", drive_tab)
        drive_tab.click()
        
        # Give UI time to update
        self.wait_until_element_is_visible(MainPageLocators.ACTIVE_DRIVE, timeout=5)
        
        # Check if booking button is active
        if not self.is_element_active(MainPageLocators.CALL_TAXI_BUTTON, timeout=10):
            return False
        return True

    @allure.step("Проверка отображения блока выбора маршрута и текста 'Маршрут строится...'")
    def check_route_block_and_text(self):
        if not self.is_route_selection_block_visible(MainPageLocators.VEHICLE_BLOCK):
            return False
        if not self.find_element_with_wait(MainPageLocators.MAP_IN_PROGRESS):
            return False
        return True
    

    @allure.step('Нажать кнопку Детали в блоке Еще про поездку')
    def check_details_button_in_trip_block(self, coast):
        # Преобразуем цену в чистые цифры для сравнения
        expected_digits = ''.join(filter(str.isdigit, str(coast)))
        
        self.wait_until_element_is_visible(MainPageLocators.ORDER_BUTTONS, timeout=60)
        
        details_buttons = self.find_elements_with_wait(MainPageLocators.ORDER_BTN_GROUP_DETAILS)
        if not details_buttons:
            return False
        
        btn = details_buttons[-1]
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", btn)
        self.driver.execute_script("arguments[0].click();", btn)
        
        page_source = self.driver.page_source
        return expected_digits in page_source

    @allure.step('Нажать кнопку Отмена - Окно закрывается')
    def check_cancel_button_closes_window(self):
        self.click_to_element_with_wait(MainPageLocators.BUTTON_CANCEL)
        if not self.is_element_not_visible(MainPageLocators.VEHICLE_BLOCK):
            return False
        return True
    
    #Методы для теста test_taxi_full_flow.py
    @allure.step("Нажать на кнопку Быстрый")
    def click_fast_button(self):
        self.click_to_element_with_wait(MainPageLocators.BUTTON_FAST)

    @allure.step("Нажать на кнопку Вызвать такси")
    def click_call_taxi_button(self):
        self.click_to_element_with_wait(MainPageLocators.CALL_TAXI_BUTTON)

    @allure.step("Получить все тарифные карточки")
    def get_all_tariffs(self):
        return self.find_elements_with_wait(MainPageLocators.TARIFFS)

    @allure.step("Получить активные тарифные карточки")
    def get_active_tariffs(self):
        return self.find_elements_with_wait(MainPageLocators.TARIFF_ACTIVE)

    @allure.step("Получить локаторы тарифов")
    def get_tariff_locators(self):
        return MainPageLocators.TARIFF_LOCATORS

    @allure.step("Найти тарифную карточку по локатору")
    def find_tariff_by_locator(self, tariff_locator):
        return self.find_element_with_wait(tariff_locator)

    @allure.step("Прокрутить к элементу и кликнуть")
    def scroll_and_click(self, element):
        self.scroll_to_element(element)
        element.click()

    @allure.step("Получить информационную кнопку тарифа по индексу")
    def get_tariff_info_button(self, index):
        return self.find_element_with_wait(MainPageLocators.i_button_by_index(index))

    @allure.step("Навести курсор на информационную кнопку")
    def hover_on_info_button(self, i_button):
        self.scroll_to_element(i_button)
        self.wait_until_element_is_visible(MainPageLocators.i_button_by_index(0))
        self.hover_to_element(i_button)

    @allure.step("Получить заголовок тултипа")
    def get_tooltip_title(self):
        self.wait_until_element_has_text(MainPageLocators.TOOLTIP_TITLE)
        return self.find_element_with_wait(MainPageLocators.TOOLTIP_TITLE)

    @allure.step("Получить описание тултипа")
    def get_tooltip_description(self):
        return self.find_element_with_wait(MainPageLocators.TOOLTIP_DESC)

    @allure.step("Навести курсор на body для скрытия тултипа")
    def move_cursor_to_body(self):
        self.hover_to_element(self.find_element_with_wait(("tag name", "body")))
        self.wait_until_element_disappears(MainPageLocators.TOOLTIP_TITLE)

    @allure.step("Получить блок формы заказа")
    def get_order_form_block(self):
        return self.find_element_with_wait(MainPageLocators.ORDER_FORM_BLOCK)