import pytest

from helpers.application_manager.application_manager import luchi_app
from utils.allure_custom_marks import allure_high_level_marks, allure_mid_level_marks


@allure_high_level_marks(
    epic="Хедер",
    feature="Навигация через верхнее меню"
)
class TestNavigateHeaderMenu:

    @pytest.mark.ui
    @allure_mid_level_marks(
        story="Пользователь может навигировать по сайту через верхнее меню",
        testcase_id="Luchi-UI-001",
        title="Навигация по сайту через верхнее меню",
        label="WEB",
        owner="AQA Falin Pavel"
    )
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
