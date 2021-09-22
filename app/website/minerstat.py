from app.model.website import Website
from app.model.db import Income,GPU,create_session
from selenium.webdriver.common.by import By
import pandas as pd

class Minerstat(Website):

    def __init__(self, *args, **kwargs) -> None:
        super(Minerstat, self).__init__(*args, **kwargs)
    
    def main_page(self):
        self.go_to(self.config['Minerstat']['URL'])

    def get_daily_returns(self):
        self.main_page()
        
        elements = self.selenium.driver.find_elements_by_class_name('tr')

        elements = self.get_all_elements(By.CLASS_NAME,self.config['Minerstat']['CLASS_NAME']['GPULIST'])

        cards = {}
        all_card = []
        for element in elements:
            order = self.get_children_elements(element,By.CLASS_NAME,self.config['Minerstat']['CLASS_NAME']['ORDER'])
            name = self.get_children_elements(element,By.CLASS_NAME,self.config['Minerstat']['CLASS_NAME']['GPU_NAME'])
            coins = self.get_children_elements(element,By.CLASS_NAME,self.config['Minerstat']['CLASS_NAME']['COIN'])
            if len(coins)==0:
                continue

            profits = []
            for coin in coins:
                voc = coin.text.split()
                daily_amount = voc[0]
                poolname = " ".join(voc[2:])
                pool = {'poolname' : poolname, 'daily_amount' : daily_amount}
                profits.append(pool)

            card = {
                    'order': order[0].text,
                    'name' : name[0].text.upper() }

            card['profits'] = profits
            all_card.append(card)
        cards['GPUs'] = all_card

        df = pd.json_normalize(cards["GPUs"], record_path='profits',meta=['order','name'])

        fields = ['order','name','poolname','daily_amount']

        return df[fields]

    def get_daily_income(self):

        self.main_page()
        
        session = create_session()
        
        elements = self.selenium.driver.find_elements_by_class_name('tr')

        elements = self.get_all_elements(By.CLASS_NAME,self.config['Minerstat']['CLASS_NAME']['GPULIST'])

        for element in elements:

            name = self.get_children_elements(element,By.CLASS_NAME,self.config['Minerstat']['CLASS_NAME']['GPU_NAME'])
            coins = self.get_children_elements(element,By.CLASS_NAME,self.config['Minerstat']['CLASS_NAME']['COIN'])

            if len(coins)==0:
                continue

            if session.query(GPU).filter_by(name=name[0].text.upper()).count() > 0:
                card = session.query(GPU).filter_by(name=name[0].text.upper()).first()
            else:
                card = GPU(name=name[0].text.upper())
                session.add(card)
                session.commit()

            for coin in coins:
                voc = coin.text.split()
                daily_amount = voc[0]
                poolname = " ".join(voc[2:])

                income = Income(gpu_id = card.id,pool=poolname,amount=daily_amount)
                session.add(income)
                session.commit()

        # session.commit()









    