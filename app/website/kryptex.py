from app.helper.checker import similarity_check
from app.model.website import Website
from selenium.webdriver.common.by import By
from app.model.db import Hashrate, Income,GPU,create_session
import pandas as pd

class Kryptex(Website):

    def __init__(self, *args, **kwargs) -> None:
        super(Kryptex, self).__init__(*args, **kwargs)
    
    def main_page(self):
        self.go_to(self.config['Kryptex']['URL'])

    def get_hashrates(self):
        self.main_page()
        session = create_session()
        
        elements = self.get_all_elements(By.CSS_SELECTOR,self.config['Kryptex']['CSS_SELECTOR']['GPUS'])

        for element in elements:
            gpu_name = self.get_children_elements(element,By.CSS_SELECTOR,self.config['Kryptex']['CSS_SELECTOR']['GPU_NAME'])
            eth_hr = self.get_children_elements(element,By.CSS_SELECTOR,self.config['Kryptex']['CSS_SELECTOR']['ETH_HASHRATE'])
            etc_hr = self.get_children_elements(element,By.CSS_SELECTOR,self.config['Kryptex']['CSS_SELECTOR']['ETC_HASHRATE'])
            exp_hr = self.get_children_elements(element,By.CSS_SELECTOR,self.config['Kryptex']['CSS_SELECTOR']['EXP_HASHRATE'])
            ubq_hr = self.get_children_elements(element,By.CSS_SELECTOR,self.config['Kryptex']['CSS_SELECTOR']['UBQ_HASHRATE'])
            rvn_hr = self.get_children_elements(element,By.CSS_SELECTOR,self.config['Kryptex']['CSS_SELECTOR']['RVN_HASHRATE'])
            beam_hr = self.get_children_elements(element,By.CSS_SELECTOR,self.config['Kryptex']['CSS_SELECTOR']['BEAM_HASHRATE'])

            if not gpu_name:
                continue

            coins = [eth_hr,eth_hr,etc_hr,exp_hr,ubq_hr,rvn_hr,beam_hr]

            #similarity_check and contains
            gpus = session.query(GPU).all()
            for gpu in gpus:
                gpu.name
            if session.query(GPU).filter_by(name=gpu_name[0].text.upper()).count() > 0:
                card = session.query(GPU).filter_by(name=gpu_name[0].text.upper()).first()
            else:
                card = GPU(name=gpu_name[0].text.upper())
                session.add(card)
                session.commit()

            for coin in coins:
                coinname = coin[0].get_attribute('data-head')
                hashrate = coin[0].text

                hash = Hashrate()

            if session.query(GPU).filter_by(name=gpu_name[0].text.upper()).count() > 0:
                card = session.query(GPU).filter_by(name=gpu_name[0].text.upper()).first()
            else:
                card = GPU(name=gpu_name[0].text.upper())
                session.add(card)
                session.commit()
            
        