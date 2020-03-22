from selenium import webdriver

class FacebookBot():
    def __init__(self):
         self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('https://facebook.com')
        
        fb_login_username = self.driver.find_element_by_xpath('//*[@id="email"]')
        fb_login_username.send_keys('6462023324')