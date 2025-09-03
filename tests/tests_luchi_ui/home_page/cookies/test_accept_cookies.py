import pytest

from helpers.application_manager.application_manager import luchi_app
from utils.allure_custom_marks import allure_class_mark, allure_func_mark


@allure_class_mark(epic="Куки", feature="Политика использования cookies")
class TestAcceptCookies:

    @pytest.mark.ui
    @allure_func_mark(story="Пользователь принимает cookies", testcase_id="Luchi-UI-001",
                      title="Пользователь принимает cookies", label="WEB", owner="AQA Falin Pavel")
    def test_accept_cookies(self):
        luchi_app.home_page \
            .open_home_page() \
            .is_opened() \
            .accept_cookies()
