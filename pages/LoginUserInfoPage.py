from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class LoginUserInfoPage(BasePage):
    
    personal_details_label = "//div[@class='personal-details__form']//h3"
    
    def __init__(self, driver):
        super().__init__(driver)
        
    def is_personal_details_label_displayed(self):
        return self.element_is_displayed(By.XPATH, self.personal_details_label) 
        
    def wait_until_personal_ditailes_display(self):
        self.element_wait_until_displayed(By.XPATH, self.personal_details_label)
        
        
    