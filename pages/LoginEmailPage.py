import string
import random
from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class LoginEmailPage(BasePage):
    
    password_text_box = "//div[@class='login-form__field-row']/input"
    email_text_box = "//div[@class='align__cell']/input[@placeholder='Your email']"
    domain_text_box = "//div[@class='align__cell']/input[@placeholder='Domain']"
    term_check_box = "//span[@class='checkbox']"
    drop_down_button = "//div[@class='dropdown__opener']"
    drop_down_items_button = "//div[@class='dropdown__list-item']"
    account_type_button = "//div[@class='dropdown__list']/div[{id}]"
    close_help_button = "//div[@class='help-form__container']//span[@class='discrete']"
    cookie_button = "//div[@class='cookies']//div[@class='align__cell'][1]//button"
    time_label = "//div[@class='view__row']//div[contains(@class, 'timer')]"
    next_button = "//a[@class='button--secondary']"
    
    
    def __init__(self, driver):
        super().__init__(driver)
            
    def clear_and_fill_password(self):
        letters = string.ascii_lowercase + string.digits + string.ascii_uppercase
        text =  ''.join(random.choice(letters) for i in range(25))
        self.element_send_keys(By.XPATH, self.password_text_box, text)
        
    def clear_and_fill_email(self):
        letters = string.ascii_lowercase
        text =  ''.join(random.choice(letters) for i in range(5))
        self.element_send_keys(By.XPATH, self.email_text_box, text)
        
    def clear_and_fill_domain(self):
        letters = string.ascii_lowercase
        text =  ''.join(random.choice(letters) for i in range(5))
        self.element_send_keys(By.XPATH, self.domain_text_box, text)
        
    def click_drop_down_button(self):
        self.element_click(By.XPATH, self.drop_down_button)

    def click_account_type(self):
        elements = self.get_elements(By.XPATH, self.drop_down_items_button)
        choice = random.randint(1, len(elements))
        self.account_type_button = self.account_type_button.format(id=choice)
        self.element_click(By.XPATH, self.account_type_button)

    def click_term_checkbox(self):
        self.element_click(By.XPATH, self.term_check_box)
        
    def click_cookie_button(self):
        self.element_click(By.XPATH, self.cookie_button)
        
    def click_next_button(self):
        self.element_click(By.XPATH, self.next_button)
    
    def click_close_help_button(self):
        self.element_click(By.XPATH, self.close_help_button)
        
    def is_page_displayed(self):
        return self.element_is_displayed(By.XPATH, self.next_button)
    
    def is_close_help_button_displayed(self):
        return self.element_is_not_displayed(By.XPATH, self.close_help_button)
    
    def is_cookie_displayed(self):
        return self.element_is_not_displayed(By.XPATH, self.cookie_button)
    
    def wait_until_page_is_displayed(self):
        self.element_wait_until_displayed(By.XPATH, self.next_button)


    def wait_until_to_close_help_button(self):
        self.element_wait_until_is_not_displayed(By.XPATH, self.close_help_button)
        
    def wait_unti_cookie_button_visable(self):
        self.element_to_be_located(By.XPATH, self.cookie_button)
    
    