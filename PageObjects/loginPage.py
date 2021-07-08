from selenium import webdriver

class Login:
    textbox_username_id = "Email"
    textbox_username_xpath = "//*[@id = 'Email']"
    textbox_password_id = "Password"
    button_login_xpath = "//*[@class = 'button-1 login-button']"
    link_logout_linktext = "Logout"

    def __init__(self,driver):
        self.driver = driver

    def setUsername(self,username):
        self.driver.find_element_by_id(self.textbox_username_id).clear()
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def setLogin(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()

    def setLogout(self):
        self.driver.find_element_by_linktext(self.link_logout_linktext).click()




