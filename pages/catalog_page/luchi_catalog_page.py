import allure

from helpers.data.all_links import AllLinks

from selene import browser, be, have, command
from selene.core.conditions import Condition as EC


class LuchiCatalogPage:

    def __init__(self):
        self.catalog_page = AllLinks.CATALOG_PAGE

    @allure.step("Открытие страницы каталога")
    def open_catalog_page(self) -> "LuchiCatalogPage":
        with allure.step(f'Открыть страницу каталога по ссылке {self.catalog_page}'):
            browser.open(self.catalog_page)
        return self

    @allure.step("Проверка открытия страницы каталога")
    def is_opened(self) -> "LuchiCatalogPage":
        with allure.step('Проверка что страница каталога открыта'):
            browser.element("""//span[contains(text(),'Сервисы для вашей жизни')]""").should(
                EC.by_and(be.visible, have.text('Сервисы для вашей жизни')))
        return self

    @allure.step("Проверка что все категории отображены и можно переключаться между ними")
    def swipe_categories_by(self, category_name: str) -> "LuchiCatalogPage":
        with allure.step(f'Проверка отображени категорий {category_name} и переключение на этот таб'):
            browser.element(f"""//span[contains(text(),'{category_name}')]""").with_(
                timeout=browser.config.timeout * 2
            ).should(EC.by_and(be.clickable, have.text(category_name))).hover().click()
        return self

    @allure.step('Проверка что в табе отображены все обязательные услуги')
    def check_that_category_contains_all_mandatory_services(self, category_name: str,
                                                            services: list) -> "LuchiCatalogPage":
        with allure.step(f'Проверка что в табе {category_name} отображены все обязательные услуги {str(services)}'):
            if category_name == "Все":
                for service in services:
                    browser.element(f"""(//div[@role="tabpanel"])[1]//span[contains(text(), '{service}')]""") \
                        .perform(command.js.scroll_into_view).should(EC.by_and(be.visible))
            elif category_name == "Страхование":
                for service in services:
                    browser.element(f"""(//div[@role="tabpanel"])[2]//span[contains(text(), '{service}')]""") \
                        .perform(command.js.scroll_into_view).should(EC.by_and(be.visible, have.text(service)))
            elif category_name == "Здоровье":
                for service in services:
                    browser.element(f"""(//div[@role="tabpanel"])[3]//span[contains(text(), '{service}')]""") \
                        .perform(command.js.scroll_into_view).should(EC.by_and(be.visible))
            elif category_name == "ДМС":
                for service in services:
                    browser.element(f"""(//div[@role="tabpanel"])[4]//span[contains(text(), '{service}')]""") \
                        .perform(command.js.scroll_into_view).should(EC.by_and(be.visible))
            elif category_name == "Забота о любимых":
                for service in services:
                    browser.element(f"""(//div[@role="tabpanel"])[5]//span[contains(text(), '{service}')]""") \
                        .perform(command.js.scroll_into_view).should(EC.by_and(be.visible))
            elif category_name == "Дом":
                for service in services:
                    browser.element(f"""(//div[@role="tabpanel"])[6]//span[contains(text(), '{service}')]""") \
                        .perform(command.js.scroll_into_view).should(EC.by_and(be.visible))
            elif category_name == "Ипотека":
                for service in services:
                    browser.element(f"""(//div[@role="tabpanel"])[7]//span[contains(text(), '{service}')]""") \
                        .perform(command.js.scroll_into_view).should(EC.by_and(be.visible))
        return self
