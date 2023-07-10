import time

import pytest
from selenium import webdriver
from pageObjects.copyPythonContent import PythonContent
from pageObjects.loginPage import Login
from Utilities.customLogger import LogGeneration
from Utilities.readProperties import ReadConfig


class Test_CopyPythonContent:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    search = ReadConfig.getSearchText()

    loginfo = LogGeneration.loginformation()

    @pytest.mark.order(3)
    def test_copyPythonContent(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.lp.clickLoginTutorialPoint()
        time.sleep(3)
        self.lp.enterUsername(self.username)
        time.sleep(2)
        self.lp.enterPassword(self.password)
        self.lp.clickLogin()
        time.sleep(2)
        self.PC = PythonContent(self.driver)
        self.PC.clickTutorialPointLogo()
        time.sleep(4)
        self.PC.clickCategoryMenu()
        time.sleep(2)
        self.PC.selectITUnderCategory()
        time.sleep(5)
        self.PC.searchWithPython(self.search)
        time.sleep(2)
        self.PC.clickPythonBabySteps()