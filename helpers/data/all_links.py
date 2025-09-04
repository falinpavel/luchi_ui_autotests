import os

from dotenv import load_dotenv

load_dotenv()


class AllLinks:

    HOME_PAGE = os.getenv("BASE_URL")

    CATALOG_PAGE = "{home_page}/catalog".format(home_page=HOME_PAGE)
