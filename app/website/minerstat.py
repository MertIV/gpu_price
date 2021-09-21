from app.model.website import Website
from selenium.webdriver.support import expected_conditions as EC
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



    