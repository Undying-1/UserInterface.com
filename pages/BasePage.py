import os
import pyautogui
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        
    def element_click(self, by, locator_value):
        element = self.get_element(by, locator_value)
        element.click() 
        
    def element_send_keys(self, by, locator_value, text):
        element = self.get_element(by, locator_value)
        element.clear()
        element.send_keys(text)
       
    def get_element(self, by, locator_value):
        element = None
        element = self.driver.find_element(by=by, value=locator_value)
        return element
    
    def get_elements(self, by, locator_value):
        elements = None
        elements = self.driver.find_elements(by=by, value=locator_value)
        return elements
    
    def element_wait_until_is_not_displayed(self, by, locator_value):
        element = self.wait.until(EC.invisibility_of_element((by, locator_value)))

    def element_wait_until_displayed(self, by, locator_value):
        element = self.wait.until(EC.element_to_be_clickable((by,locator_value)))
    
    def element_is_displayed(self, by, locator_value):
        element = self.get_element(by, locator_value)
        return element.is_displayed()
    
    def element_is_not_displayed(self, by,locator_value):
        element = self.wait.until(EC.invisibility_of_element((by, locator_value)))
        return element
    
    def element_to_be_clickable(self, by, locator_value):
        element = self.wait.until(EC.element_to_be_clickable((by, locator_value)))
    
    def element_to_be_located(self, by, locator_value):
        element = self.wait.until(EC.presence_of_element_located((by, locator_value)))
        time.sleep(2)
        
    def upload_gui_file(self, path):
        time.sleep(1)
        pyautogui.write(os.getcwd() + path, interval=0.05) 
        pyautogui.press('return')
        time.sleep(15)