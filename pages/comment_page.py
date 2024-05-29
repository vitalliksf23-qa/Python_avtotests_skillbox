import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import Keys
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


class CommentPage(BasePage):
    PAGE_URL = "https://qajava.skillbox.ru/module04/lesson3/os.html"
    NAME_INPUT = (By.XPATH, "//input[@class='data text']")
    EMAIL_INPUT = (By.XPATH, "//input[@placeholder='E-mail']")
    MESSAGE_INPUT = (By.XPATH, "//textarea[@class='field text']")
    BUTTON_COMMENT_ACTIV = (By.XPATH, "//input[@class='comment']")
    BUTTON_COMMENT_PASSIVE = (By.XPATH, "//input[@class='comment' and @disabled='disabled']")
    TEXT_RESULT = (By.XPATH, '/html/body/main/div[2]/div[2]/div[1]')
    QUESTION_TO_THE_CLIENT = (By.XPATH, "//div[@class='header-text']")

    def test_comment_true(self, driver):
        name = 'IVAN'
        email = 'IVAN@IVAN.RU'
        message = 'Thank you'
        self.element_is_visible(CommentPage.NAME_INPUT).send_keys(name)
        self.element_is_visible(CommentPage.EMAIL_INPUT).send_keys(email)
        self.element_is_visible(CommentPage.MESSAGE_INPUT).send_keys(message)
        self.elements_is_clickable(CommentPage.BUTTON_COMMENT_ACTIV).click()
        """ Утверждение по тексту """
        result_text = driver.find_element(*CommentPage.TEXT_RESULT).text
        assert (
                'Спасибо за отзыв!'
               == result_text)

    def test_comment_false(self, driver):
        self.element_is_visible(CommentPage.NAME_INPUT).click()
        self.element_is_visible(CommentPage.EMAIL_INPUT).click()
        self.element_is_visible(CommentPage.MESSAGE_INPUT).click()
        self.element_is_visible(CommentPage.BUTTON_COMMENT_PASSIVE).is_displayed()
        self.element_is_visible(CommentPage.BUTTON_COMMENT_PASSIVE).click()
        """ Утверждение по тексту """
        result_text = driver.find_element(*CommentPage.QUESTION_TO_THE_CLIENT).text
        assert ('Довольны ли вы качеством предоставленных услуг?' == result_text)

    def test_comment_is_not_email(self, driver):
        name = 'IVAN'
        message = 'Thank you'
        self.element_is_visible(CommentPage.NAME_INPUT).send_keys(name)
        self.element_is_visible(CommentPage.EMAIL_INPUT).is_displayed()
        self.element_is_visible(CommentPage.MESSAGE_INPUT).send_keys(message)
        self.element_is_visible(CommentPage.BUTTON_COMMENT_PASSIVE).is_displayed()
        self.element_is_visible(CommentPage.BUTTON_COMMENT_PASSIVE).click()


