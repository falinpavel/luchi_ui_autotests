from pages.components.header_menu.luchi_header_menu import LuchiHeaderMenu
from pages.home_page.luchi_home_page import LuchiHomePage


class LuchiApplicationManager:

    def __init__(self):
        self.home_page = LuchiHomePage()
        self.header_menu = LuchiHeaderMenu()


luchi_app = LuchiApplicationManager()
