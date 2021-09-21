from app.model.website import Website
from selenium.webdriver.common.by import By
import pandas as pd

class Kryptex(Website):

    def __init__(self, *args, **kwargs) -> None:
        super(Kryptex, self).__init__(*args, **kwargs)
    
    def main_page(self):
        self.go_to(self.config['Kryptex']['URL'])

    def get_hashrates(self):
        self.main_page()
        
        elements = self.get_all_elements(By.CSS_SELECTOR,self.config['Kryptex']['CSS_SELECTOR']['GPUS'])

        for element in elements:
            gpu_name = self.get_children_elements(element,By.CSS_SELECTOR,self.config['Kryptex']['CSS_SELECTOR']['GPU_NAME'])
            if gpu_name:
                print (gpu_name[0].text.upper())
            price = self.get_children_elements(element,By.CSS_SELECTOR,self.config['Kryptex']['CSS_SELECTOR']['PRICE'])
            if price:
                print(price[0].text)
            eth_hr = self.get_children_elements(element,By.CSS_SELECTOR,self.config['Kryptex']['CSS_SELECTOR']['ETH_HASHRATE'])
            if eth_hr:
                print(eth_hr[0].text)
            rvn_hr = self.get_children_elements(element,By.CSS_SELECTOR,self.config['Kryptex']['CSS_SELECTOR']['RVN_HASHRATE'])
            if rvn_hr:
                print(rvn_hr[0].text)
