import time
import keyboard
from pageObjects.loginPage import Login
from pageObjects.copyPythonContent import PythonContent
from pageObjects.UserProfileUpdate import ProfileUpdate
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGeneration


class Test_UpdateUserProfile:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    des = ReadConfig.getDescription()
    tag = ReadConfig.getTagLine()
    linkedinurl = ReadConfig.getLinkedInURL()

    loginfo = LogGeneration.loginformation()

    def test_profileUpdate(self, setup):
        self.driver = setup
        self.driver.implicitly_wait(5)
        self.loginfo.info("*******************Profile Update TC Started*******************")
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)  # This is an object for Login class
        self.lp.clickLoginTutorialPoint()
        self.lp.enterUsername(self.username)
        self.lp.enterPassword(self.password)
        self.lp.clickLogin()
        self.pc = PythonContent(self.driver)  # This is an object for PythonContent class
        self.pc.clickTutorialPointLogo()
        self.pu = ProfileUpdate(self.driver)  # This is an object for ProfileUpdate class
        self.pu.ClickUserProfileMenu()
        self.pu.ClickEditProfile()
        self.pu.ClickOnEditButton()
        time.sleep(4)
        #self.pu.EnterDescription(self.des)
        self.pu.EnterTagLine(self.tag)
        time.sleep(3)
        self.pu.PasteLinkedInURL(self.linkedinurl)
        time.sleep(2)
        keyboard.send("control+-")
        keyboard.send("control+-")
        time.sleep(2)
        self.pu.clickonSave()
        self.loginfo.info("*******************Profile Update TC Passed*******************")
        act_title = self.driver.title
        if act_title == "Edit Profile description | Tutorialspoint":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot("C:\\Users\\Sindhu\\PycharmProjects\\quickerAutomation\\Screenshots\\homePageTitle.png")
            assert False
