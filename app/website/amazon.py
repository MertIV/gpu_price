from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException as NoSuchElement
from selenium.common.exceptions import TimeoutException as Timeout
from selenium.common.exceptions import WebDriverException as DriverException
from functools import wraps
import sys, time, typing

class Amazon():

    def __init__(self,driver) -> None:
        self.driver = driver

    def get_mainpage(self):
        try:
            el1 = WebDriverWait(self.driver, 2).until(EC.presence_of_element_located(
                (By.XPATH, xpath['main_page'])))
            el1.get_attribute("title")
            return True
        except Timeout:
            self.driver.get('https://amazon.fr/')
            try:
                el2 = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(
                    (By.XPATH, xpath['login'])))
                print(el2.get_attribute("title"))
                return True
            except Timeout:
                self.login()
            except Exception as e:
                print('Başka bir şey yanlış : ' + e)
                return False


xpath = {
    'main_page': '/html/head/title/text()',
    'zip_code': '//*[@id="glow-ingress-line2"]',
    'message_box': '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]',
    'message_send_button': '//*[@id="main"]/footer/div[1]/div[3]/button',
    'message_tab_class': 'tSmQ1',
    'attach_image': '//*[@id="main"]/footer/div[1]/div[1]/div[2]/div/div/span',
    'attach_input': '//*[@id="main"]/footer/div[1]/div[1]/div[2]/div/span/div/div/ul/li[1]/button/input',
    'attach_text_box': '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div[1]/span/div/div[2]/div/div[3]/div[1]/div[2]',
    'attach_loaded': '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div[1]/span/div/div[1]',
    'attach_send_button': '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span/div/div/span',
}


css_selector = {
    'message_list_tab': 'div._185ho',
    'message_status': "span[data-testid*='msg-dblcheck'],span[data-testid*='msg-check']"
}