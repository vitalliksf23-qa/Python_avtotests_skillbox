import time
from pages.comment_page import CommentPage
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


class TestComment:
    """ Отправка коментария с валидными данными """
    def test(self, driver):
        comment_page = CommentPage(driver, "https://qajava.skillbox.ru/module04/lesson3/os.html")
        comment_page.open()
        comment_page.test_comment_true(driver)

    """ Отправка коментария с пустыми полями, комент не отправляется"""
    def test1(self, driver):
        comment_page = CommentPage(driver, "https://qajava.skillbox.ru/module04/lesson3/os.html")
        comment_page.open()
        comment_page.test_comment_false(driver)

    # """ 'Баг' Отправка коментария без email, комент не должен отправляться, но кнопка активна"""
    # def test2(self, driver):
    #     computer_page = CommentPage(driver, "https://qajava.skillbox.ru/module04/lesson3/os.html")
    #     computer_page.open()
    #     computer_page.test_comment_is_not_email(driver)

