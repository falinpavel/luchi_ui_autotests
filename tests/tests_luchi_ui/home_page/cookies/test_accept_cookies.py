import pytest

from helpers.application_manager.application_manager import luchi_app
from utils.allure_custom_marks import allure_high_level_marks, allure_mid_level_marks


@allure_high_level_marks(
    epic="Куки",
    feature="Политика использования cookies"
)
class TestAcceptCookies:

    @pytest.mark.ui
    @allure_mid_level_marks(
        story="Пользователь принимает cookies",
        testcase_id="Luchi-UI-001",
        title="Пользователь принимает cookies",
        label="WEB",
        owner="AQA Falin Pavel"
    )
    def test_accept_cookies(self):
        luchi_app.home_page \
            .open_home_page() \
            .is_opened() \
            .accept_cookies()
