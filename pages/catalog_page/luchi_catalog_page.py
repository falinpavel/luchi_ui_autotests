import allure

from helpers.data.all_links import AllLinks

from selene import browser, be, have
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
            browser.element(f"""//span[contains(text(),'{category_name}')]""").should(EC.by_and(
                be.clickable, have.text(category_name))).hover().click()
        return self
