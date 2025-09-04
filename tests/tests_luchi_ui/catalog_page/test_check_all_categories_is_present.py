import pytest

from helpers.application_manager.application_manager import luchi_app
from utils.allure_custom_marks import allure_high_level_marks, allure_mid_level_marks


@allure_high_level_marks(epic="Каталог", feature="Страница каталога с категориями")
class TestNavigateHeaderMenu:

    @pytest.mark.ui
    @pytest.mark.parametrize(
        "category_name", ["Все", "Страхование", "Здоровье", "ДМС", "Забота о любимых", "Дом", "Ипотека"],
        ids=["All", "Insurance", "Health", "DMC", "Pet", "House", "Mortgage"]
    )
    @allure_mid_level_marks(
        story="Пользователь может переключаться между категориями в каталоге", testcase_id="Luchi-UI-001",
        title="Навигация по каталогу кликами по наименованиям категорий (табы)", label="WEB", owner="AQA Falin Pavel"
    )
    def test_swipe_all_category_tabs(self, category_name):
        luchi_app.home_page \
            .open_home_page() \
            .is_opened() \
            .accept_cookies()
        luchi_app.header_menu.click_catalog_button()
        luchi_app.catalog_page \
            .is_opened() \
            .swipe_categories_by(category_name=category_name)
