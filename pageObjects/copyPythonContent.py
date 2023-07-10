from selenium import webdriver
from selenium.webdriver.common.by import By

class PythonContent:
    logo_tutorialPoint_xpath = "(//img[@class='navbar-brand-item'])[1]"
    menu_category_xpath = "//span[text()='Category ']"
    button_ITNetworking_xpath = "//a[text()='  IT and Networking']"
    search_courses_xpath = "//input[@name='key']"
    menu_pythonBabySteps_xpath = "//a[contains(.,'Baby steps')]"

    def __init__(self, driver):
        self.driver = driver

    def clickTutorialPointLogo(self):
        self.driver.find_element(By.XPATH, self.logo_tutorialPoint_xpath).click()

    def clickCategoryMenu(self):
        self.driver.find_element(By.XPATH, self.menu_category_xpath).click()

    def selectITUnderCategory(self):
        self.driver.find_element(By.XPATH, self.button_ITNetworking_xpath).click()

    def searchWithPython(self, search):
        self.driver.find_element(By.XPATH, self.search_courses_xpath).send_keys(search)

    def clickPythonBabySteps(self):
        self.driver.find_element(By.XPATH, self.menu_pythonBabySteps_xpath).click()