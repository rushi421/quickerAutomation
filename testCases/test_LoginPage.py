import time
import pytest
from selenium import webdriver
from pageObjects.loginPage import Login
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGeneration


class Test_001_LoginAccess:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    loginfo = LogGeneration.loginformation()


    def test_homePageTitle(self, setup):
        self.driver = setup
        self.loginfo.info("##############Test Case Started################")
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        #self.driver.close()
        if act_title == "Online Courses and eBooks Library":
            assert True
            self.loginfo.info("##############Test Case Passed################")
        else:
            self.driver.save_screenshot("C:\\Users\\Sindhu\\PycharmProjects\\quickerAutomation\\Screenshots\\homePageTitle.png")
            self.loginfo.info("##############Test Case Failed################")
            assert False

    @pytest.mark.parametrize("username, password",
        [("bathulabhavani123@gmail.com","Vani123"),
         ("naresh.kn1811@gmail.com","Naresh@123"),
         ("rushendrakumar12@gmail.com", "rushi123")])
    def test_login(self, setup, username, password):
        self.driver = setup
        self.loginfo.info("##############Test Login TC Started################")
        self.driver.get(self.baseURL)
        time.sleep(3)
        self.lp = Login(self.driver)
        self.lp.clickLoginTutorialPoint()
        time.sleep(3)
        self.lp.enterUsername(username)
        time.sleep(2)
        self.lp.enterPassword(password)
        self.lp.clickLogin()
        time.sleep(5)
        act_title = self.driver.title
        if act_title == "Instructor Dashboard | Tutorialspoint":
            assert True
            self.loginfo.info("##############Test Login TC Passed################")
        else:
            self.driver.save_screenshot("C:\\Users\\Sindhu\\PycharmProjects\\quickerAutomation\\Screenshots\\homePageTitle1.png")
            assert False