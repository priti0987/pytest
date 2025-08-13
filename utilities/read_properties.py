import configparser

config = configparser.RawConfigParser()
config.read(".\\configurations\\config.ini")

class read_Config:
    @staticmethod
    def get_admin_page_url():
       url =  config.get('admin login info',"admin_Page_Url")
       return url

    @staticmethod
    def get_admin_username():
       username =  config.get('admin login info',"username")
       return username

    @staticmethod
    def get_admin_password():
       password =  config.get('admin login info',"password")
       return password
    
    @staticmethod
    def get_admin_invalid_username():
        invalid_username =  config.get('admin login info',"invalid_username")
        return invalid_username