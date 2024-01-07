import string
import random
from selenium.webdriver.common.by import By
from pages.BasePage import BasePage



class LoginImagePage(BasePage):
    
    untick_button = "//*[@id='app']/div[1]/div[2]/div[4]/div/div[1]/div/div[3]/div/div[21]/div/span[1]/label"
    image_upload_button = "//a[@class='avatar-and-interests__upload-button']"
    next_button = "//*[@id='app']/div[1]/div[2]/div[4]/div/div[2]/div/div/div[1]/button"
    interests_list_checkbox = "//div[@class='avatar-and-interests__interests-list']//div[{id}]//label"
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def click_untick_all(self):
        self.element_to_be_located(By.XPATH, self.untick_button)
        self.element_click(By.XPATH, self.untick_button) 
        
    def click_image_upload_button(self):
        self.element_click(By.XPATH, self.image_upload_button)
        
    def click_next_button(self):
        self.element_click(By.XPATH, self.next_button)
        
    def click_to_interests(self, interests_lenth):
        i = 0
        while i != interests_lenth:
            choice = random.randint(1, 21)
            if choice != 21 or choice != 18:
                data = self.interests_list_checkbox.format(id=choice)
                self.element_to_be_clickable(By.XPATH, data)
                self.element_click(By.XPATH, data)
                i+=1
        
    def click_image_upload_button(self):
        self.element_click(By.XPATH, self.image_upload_button)
    
    def upload_image(self):
        self.upload_gui_file('/assets/images/image.png')
        
    def wait_until_page_is_displayed(self):
        self.element_wait_until_displayed(By.XPATH, self.image_upload_button)
    
    def is_page_displayed(self):
        return self.element_is_displayed(By.XPATH, self.image_upload_button)
        
           
        