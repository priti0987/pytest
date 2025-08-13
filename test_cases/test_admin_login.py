import time
from utilities.read_properties import read_Config
import pytest
from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By

from base_pages.Login_Admin_Page import Login_Admin_Page


class Test_01_Admin_Login:
    admin_Page_Url = read_Config.get_admin_page_url()
    username = read_Config.get_admin_username()
    password = read_Config.get_admin_password()
    invalid_username = read_Config.get_admin_invalid_username()

    def test_title_verification(self,setup):
        self.driver = setup
        self.driver.get(self.admin_Page_Url)
        self.driver.maximize_window()
        act_title = self.driver.title
        exp_title = "Swag Labs"
        if act_title == exp_title:
            assert True
            self.driver.close()
        else:
            self.driver.close()
            assert False

    def test_valid_admin_login(self,setup):
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



