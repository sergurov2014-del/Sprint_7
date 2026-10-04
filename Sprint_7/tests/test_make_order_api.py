import allure
import pytest
import Sprint_7_test.tests.helpers_shit as helpers_shit
from locators import start_page_locators  as spl , order_page_locators as opl, for_all_pages_locators as apl

class TestMakeOrderAPI:

   @allure.title(
            'Проверка создания заказа'
            )         

   def test_check_make_order_via_API(self, driver, order_button, metro_station, bring_date, scooter_color):
      pass