import allure

from helpers.data.all_links import AllLinks

from selene import browser, be, have
from selene.core.conditions import Condition as EC


class LuchiHeaderMenu:

    @allure.step("Переход на главную страницу по клику на логотип")
    def click_home_icon(self) -> "LuchiHeaderMenu":
        with allure.step('Переход на главную страницу нажатием на логотип в хедере'):
            browser.element("""//div[@class="Header css-136jwq3"]//a[@href="/"]""").should(
                EC.by_and(be.clickable)).hover().click()
        return self

    @allure.step("Переход на страницу каталога")
    def click_catalog_button(self) -> "LuchiHeaderMenu":
        with allure.step('Переход на страницу каталога нажатием на кнопку "Каталог" в хедере'):
            browser.element("""//span[text()="Каталог"]""").should(EC.by_and(
                be.clickable, have.text("Каталог"))).hover().click()
        return self

    @allure.step("Переход на страницу 'О нас'")
    def click_about_us_button(self) -> "LuchiHeaderMenu":
        with allure.step('Переход на страницу "О нас" нажатием на кнопку "О нас" в хедере'):
            browser.element("""//div[@class="Header css-136jwq3"]//span[text()="О нас"]""").should(EC.by_and(
                be.clickable, have.text("О нас"))).hover().click()
        return self

    @allure.step("Переход на страницу 'Страховой случай'")
    def click_insurance_case_button(self) -> "LuchiHeaderMenu":
        with allure.step('Переход на страницу "Страховой случай" нажатием на кнопку "Страховой случай" в хедере'):
            browser.element("""//span[@title="Страховой случай"]""").should(EC.by_and(
                be.clickable, have.text("Страховой случай"))).hover().click()
        return self

    @allure.step("Нажатие на кнопку личного кабинета")
    def click_personal_account_icon(self):
        with allure.step('Нажать на иконку входа в личный кабинет'):
            browser.element("""//button[@aria-label="Профиль пользователя"]""").should(
                EC.by_and(be.clickable)).hover().click()
        return self
