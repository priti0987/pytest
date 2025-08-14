import time
from utilities.read_properties import read_Config
import pytest
from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities.custom_logger import Log_Maker
from base_pages.Login_Admin_Page import Login_Admin_Page


class Test_01_Admin_Login:
    admin_Page_Url = read_Config.get_admin_page_url()
    username = read_Config.get_admin_username()
    password = read_Config.get_admin_password()
    invalid_username = read_Config.get_admin_invalid_username()
    logger = Log_Maker.log_gen()

    def test_title_verification(self,setup):
        self.logger.info("*********** Test_01_Admin_Login ************")
        self.logger.info("*********** verification of admin login page ************")
        self.driver = setup
        self.driver.get(self.admin_Page_Url)
        self.driver.maximize_window()
        act_title = self.driver.title
        exp_title = "Swag Labs"
        if act_title == exp_title:
            self.logger.info("*********** title matched  ************")
            assert True
            self.driver.close()
        else:
            self.logger.info("*********** title not matched ************")
            self.driver.close()
            assert False

    def test_valid_admin_login(self,setup):
        self.logger.info("*********** Valid Login  ************")
        self.driver = setup
        self.driver.get(self.admin_Page_Url)
        self.driver.maximize_window()
        self.admin_login = Login_Admin_Page(self.driver)
        self.admin_login.enter_username(self.username)
        self.admin_login.enter_password(self.password)
        self.admin_login.click_login()
        time.sleep(5)
        act_dashboard_text = self.driver.find_element(By.XPATH,"//span[@class='title']").text
        if act_dashboard_text == "Products":
            assert True
            self.driver.close()
        else:
            self.driver.close()
            assert False

    def test_invalid_admin_login(self,setup):
        self.logger.info("*********** InValid Login  ************")
        self.driver = setup
        self.driver.get(self.admin_Page_Url)
        self.driver.maximize_window()
        self.admin_login = Login_Admin_Page(self.driver)
        self.admin_login.enter_username(self.invalid_username)
        self.admin_login.enter_password(self.password)
        self.admin_login.click_login()
        time.sleep(10)
        error_message = "Please enter a valid email address."
        act_dashboard_text = self.driver.find_element(By.XPATH,"//*[@data-test='error']").is_displayed()
        if act_dashboard_text :
            assert True
            self.driver.close()
        else:
            self.driver.close()
            assert False

