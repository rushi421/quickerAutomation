import pytest
from pageObjects.loginPage import Login
from pageObjects.copyPythonContent import PythonContent
from pageObjects.UserProfileUpdate import ProfileUpdate
from pageObjects.InstructorDashboardUpdate import instructorUpdate
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGeneration

class Test_InstructorDashboard:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    courseName = ReadConfig.getCourseName()
    courseTag = ReadConfig.getCourseTag()
    metaTitle = ReadConfig.getMetaTitle()
    metaDesc = ReadConfig.getMetaDesc()

    logInfo = LogGeneration.loginformation()

    @pytest.mark.sanity
    @pytest.mark.regression
    @pytest.mark.rushi
    def test_instructorDashboardUpdate(self, setup):
        self.driver = setup
        self.logInfo.info("#################InstructorDashboard Test case started####################")
        self.driver.implicitly_wait(5)
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
        self.ID = instructorUpdate(self.driver)  # This is an object for InstructorDashboard class
        self.ID.ClickOnInstructorDashboard()
        self.ID.ClickOnCreateCourse()
        self.ID.EnterCourseName(self.courseName)
        self.ID.EnterCouserTag(self.courseTag)
        self.ID.EnterMetaTitle(self.metaTitle)
        self.ID.EnterMetaDesc(self.metaDesc)
        self.ID.ClickOnSaveInsDashboard()
        self.logInfo.info("#################InstructorDashboard Test case Completed####################")
        act_title = self.driver.title
        if act_title == "Create Video Course - Tutorialspoint1":
            assert True
        else:
            self.driver.save_screenshot("C:\\Users\\Sindhu\\PycharmProjects\\quickerAutomation\\Screenshots\\homePageTitle.png")
            assert False