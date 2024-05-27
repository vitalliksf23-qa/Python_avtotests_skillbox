import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import Keys
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.action_chains import ActionChains


class ComputerPage(BasePage)
    PAGE_URL = "https://qajava.skillbox.ru/module04/lesson3/os.html"
