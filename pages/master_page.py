import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import Keys
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


class MasterPage(BasePage):
    PAGE_URL = "https://qajava.skillbox.ru/module04/lesson3/index.html"
    FULL_NAME = (By.XPATH, "//input[@class='form-input fio']")
    STREET_NUMBER = (By.XPATH, '//input[@class="data form-input street"]')
    HOUSE_NUMBER = (By.XPATH, "//input[@class='form-input house']")
    FLAT_NUMBER = (By.XPATH, "//input[@class='form-input flat']")
    DAY_OF_VISIT = (By.XPATH, "//input[@class='form-input date']")
    BUTTON_MASTER = (By.XPATH, "//button[@class='form-submit']")
    RESULT_ELEMENT = (By.XPATH, "//div[@class='form-result result']")
    RESULT_FULL_NAME = (By.XPATH, "/html/body/main/div[2]/div/div/div/table/tbody/tr[1]/td[2]")

    def test_call_the_wizard_with_valid_data(self, driver):
        full_name = "IVAN JOVANOVICH IVANOV"
        street_name = 'Lenina'
        house_number = '3'
        flat_number = '56'
        day_of_visit = 'Понедельник'
        self.element_is_visible(MasterPage.FULL_NAME).send_keys(full_name)
        self.element_is_visible(MasterPage.STREET_NUMBER).send_keys(street_name)
        self.element_is_visible(MasterPage.HOUSE_NUMBER).send_keys(house_number)
        self.element_is_visible(MasterPage.FLAT_NUMBER).send_keys(flat_number)
        self.element_is_visible(MasterPage.DAY_OF_VISIT).send_keys(day_of_visit)
        self.elements_is_clickable(MasterPage.BUTTON_MASTER).click()
        self.wait.until(EC.visibility_of_element_located(MasterPage.RESULT_FULL_NAME))


