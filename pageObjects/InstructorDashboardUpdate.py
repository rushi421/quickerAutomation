from selenium.webdriver.common.by import By

class instructorUpdate:
    link_instructorDashboard_xpath = "//a[contains(.,'Instructor Dashboard')]"
    button_createCourse_xpath = "//a[contains(.,'Create Course')]"
    text_enterCourseName_id = "course_name"
    text_enterCourseTag_id = "tag_line"
    text_metaTitle_id = "course_meta_title"
    text_metaDescription_id = "course_meta_desc"
    button_save_xpath = "(//button[contains(.,'Save')])[1]"

    def __init__(self, driver):
        self.driver = driver

    def ClickOnInstructorDashboard(self):
        self.driver.find_element(By.XPATH, self.link_instructorDashboard_xpath).click()

    def ClickOnCreateCourse(self):
        self.driver.find_element(By.XPATH, self.button_createCourse_xpath).click()

    def EnterCourseName(self, course):
        self.driver.find_element(By.ID, self.text_enterCourseName_id).send_keys(course)

    def EnterCouserTag(self, coursetag):
        self.driver.find_element(By.ID, self.text_enterCourseTag_id).send_keys(coursetag)

    def EnterMetaTitle(self, metatitle):
        self.driver.find_element(By.ID, self.text_metaTitle_id).send_keys(metatitle)

    def EnterMetaDesc(self, metadesc):
        self.driver.find_element(By.ID, self.text_metaDescription_id).send_keys(metadesc)

    def ClickOnSaveInsDashboard(self):
        self.driver.find_element(By.XPATH, self.button_save_xpath).click()