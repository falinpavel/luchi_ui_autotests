import pytest

from helpers.application_manager.application_manager import luchi_app
from utils.allure_custom_marks import allure_class_mark, allure_func_mark


@allure_class_mark(epic="Хедер", feature="Навигация через верхнее меню")
class TestNavigateHeaderMenu:

    @pytest.mark.ui
    @allure_func_mark(story="Пользователь может навигировать по сайту через верхнее меню", testcase_id="Luchi-UI-001",
                      title="Навигация по сайту через верхнее меню", label="WEB", owner="AQA Falin Pavel")
    def test_navigate_all_links_in_header_menu(self):
        luchi_app.home_page \
            .open_home_page() \
            .is_opened() \
            .accept_cookies()
        luchi_app.header_menu \
            .click_catalog_button() \
            .click_home_icon() \
            .click_about_us_button() \
            .click_home_icon() \
            .click_insurance_case_button() \
            .click_home_icon() \
            .click_personal_account_icon() \
            .click_home_icon()
