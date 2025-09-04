import pytest

from helpers.application_manager.application_manager import luchi_app
from utils.allure_custom_marks import allure_high_level_marks, allure_mid_level_marks


@allure_high_level_marks(
    epic="Каталог",
    feature="Страница каталога с категориями"
)
class TestSpecificCategoryContains:

    @pytest.mark.ui
    @pytest.mark.smoke
    @pytest.mark.parametrize(
        "category_name, expected_services",
        [
            pytest.param(
                "Все",
                ["ДМС для бизнеса любого масштаба", "Страхование квартиры",
                 "Ипотечное страхование", "Лапки под", "Ассистент здоровья",
                 "Виртуальная клиника", "физических лиц", "Чекапы", "сотрудников"],
                id="All"
            ),
            pytest.param(
                "Страхование",
                ["ДМС для бизнеса любого масштаба", "Страхование квартиры",
                 "Ипотечное страхование", "Лапки под", "физических лиц", "сотрудников"],
                id="Insurance"
            ),
            pytest.param(
                "Здоровье",
                ["ДМС для бизнеса любого масштаба", "Ассистент здоровья",
                 "Виртуальная клиника", "физических лиц", "Чекапы", "сотрудников"],
                id="Health"
            ),
            pytest.param(
                "ДМС",
                ["ДМС для бизнеса любого масштаба", "сотрудников"],
                id="DMC"
            ),
            pytest.param(
                "Забота о любимых",
                ["Лапки под", "Ассистент здоровья", "Чекапы"],
                id="Lovely",
                marks=[pytest.mark.slow]
            ),
            pytest.param(
                "Дом",
                ["Страхование квартиры", "Ипотечное страхование"],
                id="House"
            ),
            pytest.param(
                "Ипотека",
                ["Ипотечное страхование"],
                id="Mortgage"
            )
        ]
    )
    @allure_mid_level_marks(
        story="Пользователь может переключится на конкретную категорию и смотреть ее услуги",
        testcase_id="Luchi-UI-001",
        title="Пользователь может переключится на конкретный таб и работать с ним",
        label="WEB",
        owner="AQA Falin Pavel"
    )
    def test_specific_category_contains_mandatory_services(self, category_name, expected_services):
        luchi_app.home_page \
            .open_home_page() \
            .is_opened() \
            .accept_cookies()
        luchi_app.header_menu.click_catalog_button()
        luchi_app.catalog_page \
            .is_opened() \
            .swipe_categories_by(category_name=category_name) \
            .check_that_category_contains_all_mandatory_services(category_name=category_name,
                                                                 services=expected_services)
