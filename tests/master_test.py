import time
from pages.master_page import MasterPage
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import pytest


class TestMaster:
    """ Вызов мастера с валидными данными """
    def test(self, driver):
        master_page = MasterPage(driver, "https://qajava.skillbox.ru/module04/lesson3/index.html")
        master_page.open()
        master_page.test_call_the_wizard_with_valid_data(driver)



