from tests.BaseTest import BaseTest
from pages.MainPage import MainPage
from pages.LoginEmailPage import LoginEmailPage
from pages.LoginImagePage import LoginImagePage
from pages.LoginUserInfoPage import LoginUserInfoPage

class TestMain(BaseTest):
    
    def test_first_page(self):
        main_page = MainPage(self.driver)
        main_page.click_on_switch_page_button()
        
        login_email_page = LoginEmailPage(self.driver)
        login_email_page.wait_until_page_is_displayed()
        
        assert login_email_page.is_page_displayed() == True
        login_email_page.clear_and_fill_password()
        login_email_page.clear_and_fill_email()
        login_email_page.clear_and_fill_domain()
        login_email_page.click_drop_down_button()
        login_email_page.click_account_type()
        login_email_page.click_term_checkbox()
        login_email_page.click_next_button()
        
        login_image_page = LoginImagePage(self.driver)
        login_image_page.wait_until_page_is_displayed()
        assert login_image_page.is_page_displayed()
        login_image_page.click_image_upload_button()
        login_image_page.upload_image()
        login_image_page.click_untick_all()
        login_image_page.click_to_interests(3)
        login_image_page.click_next_button()
        
        login_user_info_page = LoginUserInfoPage(self.driver)
        login_user_info_page.wait_until_personal_ditailes_display()
        assert login_user_info_page.is_personal_details_label_displayed()
        
    def test_cookie_button_close(self):
        main_page = MainPage(self.driver)
        main_page.click_on_switch_page_button()
        
        login_email_page = LoginEmailPage(self.driver)
        login_email_page.wait_unti_cookie_button_visable()
        login_email_page.click_cookie_button()
        assert login_email_page.is_cookie_displayed()
        
    
    def test_help_button_close(self):
        main_page = MainPage(self.driver)
        main_page.click_on_switch_page_button()
        
        login_email_page = LoginEmailPage(self.driver)
        login_email_page.wait_unti_cookie_button_visable()
        login_email_page.click_close_help_button()
        login_email_page.wait_until_to_close_help_button()
        assert login_email_page.is_close_help_button_displayed()
        

        
        