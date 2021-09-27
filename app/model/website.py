from selenium.webdriver.common.by import By
from app.helper.logger import Logger
from app.model.driver import Selenium
from app import config

class Website():

    def __init__(self) -> None:
        self.url = ''
        self.logger = Logger()
        self.selenium = Selenium()
        self.config = config

    def current_url(self) -> None:
        self.selenium.driver.current_url

    def refresh(self) -> None:
        self.selenium.driver.refresh()

    def get_html(self):
        self.selenium.driver.page_source

    def get_attribute(self,element,attribute):
        try:
            at = element.get_attribute(attribute)
        except Exception as e:
            self.logger.log('Could not find the attribute : ' + e)
        return None
    
    def get_element(self,by,element_path):
        try:
            element = self.selenium.driver.find_element(by,element_path)

            return element
        except Exception as e:
            self.logger.log('Could not get the element because : ' + e)
        
    def get_text_excluding_children(self, element):
        text = element.text
        children = element.find_elements_by_xpath('./*')
        for child in children:
            if element.text == child.text:
                continue
            text = text.replace(child.text,'')
        return text

    def get_children_elements(self,element,by=By.XPATH,path='.//*'):
        try:
            all_children_by_xpath = element.find_elements(by,path)

            return all_children_by_xpath
        except Exception as e:
            self.logger.log('Could not get the child elements because : ' + e)

    def get_child_element(self,element,by=By.XPATH,path='.//*'):
        try:
            all_children_by_xpath = element.find_element(by,path)

            return all_children_by_xpath
        except Exception as e:
            self.logger.log('Could not get the child elements because : ' + e)    

    def get_all_elements(self,by,element_path):
        try:
            elements = self.selenium.driver.find_elements(by,element_path)
        except Exception as e:
            self.logger.log('Could not get the elements because : ' + e)
        return elements

    def go_to(self,url):
        try:
            self.selenium.driver.get(url)
        except Exception as e: 
            self.logger.log('Could not get the page because : ' + e)
        return None
    
    def write(self,element,content):
        try:
            element.send_keys(content)
        except Exception as e:
            self.logger.log('Could not write to element because : ' + e)
        return None
    
    def click(self,element):
        try:
            element.click()
        except Exception as e:
            self.logger.log('Could not click the element : ' + e)
        return None
    
    def get_all_attributes(self,element):
        attrs=[]

        for attr in element.get_property('attributes'):
            attrs.append([attr['name'], attr['value']])

        return attrs