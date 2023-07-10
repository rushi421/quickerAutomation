from selenium import webdriver
from selenium.webdriver.common.by import By

class ProfileUpdate:
    menu_UserProfile_xpath = "(//div[@id='profileImage'])[1]"
    link_EditProfile_xpath = "//a[contains(.,'Edit Profile')]"
    button_Edit_xpath = "(//a[contains(.,'Edit')])[2]"
    text_Description_xpath = "//div[@class='fr-element fr-view']"
    text_Tag_xpath = "//input[@id='user_tag_line']"
    text_LinkedInUrl_name = "user_linkedin"
    button_Save_xpath = "//button[contains(.,'Save')]"
    #button_Save_name = "cancel_button"

    def __init__(self, driver):
        self.driver = driver

    def ClickUserProfileMenu(self):
        self.driver.find_element(By.XPATH, self.menu_UserProfile_xpath).click()

    def ClickEditProfile(self):
        self.driver.find_element(By.XPATH, self.link_EditProfile_xpath).click()

    def ClickOnEditButton(self):
        self.driver.find_element(By.XPATH, self.button_Edit_xpath).click()

    def EnterDescription(self, Description):
        self.driver.find_element(By.XPATH, self.text_Description_xpath).send_keys(Description)

    def EnterTagLine(self, tag):
        self.driver.find_element(By.XPATH, self.text_Tag_xpath).send_keys(tag)

    def PasteLinkedInURL(self, LinkedInURL):
        self.driver.find_element(By.NAME, self.text_LinkedInUrl_name).send_keys(LinkedInURL)

    def clickonSave(self):
        self.driver.find_element(By.XPATH, self.button_Save_xpath).click()
