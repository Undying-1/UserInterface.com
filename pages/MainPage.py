from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class MainPage(BasePage):
    
    switch_page_button = "//a[@href='/game.html']" 
    
    def __init__(self, driver):
        super().__init__(driver)
        
           
        
    def click_on_switch_page_button(self):
        self.element_click(By.XPATH, self.switch_page_button)
        
        
    