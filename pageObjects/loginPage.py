from selenium import webdriver
from selenium.webdriver.common.by import By

class Login:
    button_loginTutorialPoint_xpath = "//a[contains(.,'Login')]"
    textbox_emailId_xpath = "//input[@id='user_email']"
    textbox_password_xpath = "//input[@name='user_password']"
    button_login_xpath = "//button[@name='user_login']"

    def __init__(self, driver):
        self.driver = driver

    def clickLoginTutorialPoint(self):
        self.driver.find_element(By.XPATH, self.button_loginTutorialPoint_xpath).click()

    def enterUsername(self, username):
        self.driver.find_element(By.XPATH, self.textbox_emailId_xpath).send_keys(username)

    def enterPassword(self, password):
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

