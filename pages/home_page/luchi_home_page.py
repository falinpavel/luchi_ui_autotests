import allure

from helpers.data.all_links import AllLinks

from selene import browser, be, have
from selene.core.conditions import Condition as EC


class LuchiHomePage:

    def __init__(self):
        self.url = AllLinks.HOME_PAGE

    @allure.step("Открытие главной страницы")
    def open_home_page(self) -> "LuchiHomePage":
        with allure.step(f'Открыть главную страницу по ссылке {self.url}'):
            browser.open(self.url)
        return self

    @allure.step("Проверка открытия страницы")
    def is_opened(self) -> "LuchiHomePage":
        with allure.step('Проверка открытия страницы (проверяем наличие текста в заголовке)'):
            browser.element("""//span[contains(text(),'Онлайн-страховая')]""").should(
                EC.by_and(be.visible, have.text("ОНЛАЙН-СТРАХОВАЯ, С КОТОРОЙ ЛЕГКО")))
        return self

    @allure.step("Принятие cookies")
    def accept_cookies(self) -> "LuchiHomePage":
        with allure.step('Принятие cookies нажатием на плашке кнопки "Хорошо"'):
            browser.element("""//span[@title="Хорошо"]""").should(
                EC.by_and(be.clickable, have.text("Хорошо"))).hover().click()
        return self

    @allure.step("Переход на страницу каталога")
    def click_select_insurance(self) -> "LuchiHomePage":
        with allure.step('Переход на страницу каталога нажатием на кнопку "Подобрать страховку"'):
            browser.element("""//span[@title="Подобрать страховку"]""").should(EC.by_and(
                be.clickable, have.text('Подобрать страховку'))).hover().click()
        return self
