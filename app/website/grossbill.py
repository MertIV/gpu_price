from model.website import Website
from selenium.webdriver.common.by import By
from configobj import ConfigObj
import pandas as pd
from app import config

class Grossbill(Website):

    def __init__(self, *args, **kwargs) -> None:
        super(Grossbill, self).__init__(*args, **kwargs)

        self.config = config
    
    def main_page(self):
        self.go_to(self.config['Grossbill']['URL'])
