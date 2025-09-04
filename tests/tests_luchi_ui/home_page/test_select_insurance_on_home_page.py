import pytest

from helpers.application_manager.application_manager import luchi_app
from utils.allure_custom_marks import allure_high_level_marks, allure_mid_level_marks


@allure_high_level_marks(
    epic="Каталог",
    feature="Подбор страхования"
)
class TestSelectInsurance:

    @pytest.mark.ui
    @allure_mid_level_marks(
        story="Пользователь при клике на 'Подобрать страховку' попадает на страницу каталога",
        testcase_id="Luchi-UI-001",
        title="Пользователь принимает cookies",
        label="WEB",
        owner="AQA Falin Pavel"
    )
    def test_navigate_to_catalog_after_click_select_insurance(self):
        luchi_app.home_page \
            .open_home_page() \
            .is_opened() \
            .accept_cookies() \
            .click_select_insurance()
