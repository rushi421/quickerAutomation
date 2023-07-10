import configparser
config = configparser.RawConfigParser()
config.read("C:\\Users\\Sindhu\\PycharmProjects\\quickerAutomation\\Configurations\\config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        URL = config.get('common user info', 'baseURL')
        return URL

    @staticmethod
    def getUsername():
        Username = config.get('common user info', 'username')
        return Username

    @staticmethod
    def getPassword():
        Password = config.get('common user info', 'password')
        return Password

    @staticmethod
    def getSearchText():
        Search = config.get('common user info', 'search')
        return Search

    @staticmethod
    def getDescription():
        des = config.get('common user info', 'Description')
        return des

    @staticmethod
    def getTagLine():
        tag = config.get('common user info', 'tag')
        return tag

    @staticmethod
    def getLinkedInURL():
        LinkedInURL = config.get('common user info', 'LinkedInURL')
        return LinkedInURL

    @staticmethod
    def getCourseName():
        coursename = config.get('common user info', 'courseName')
        return coursename

    @staticmethod
    def getCourseTag():
        cousertag = config.get('common user info', 'courseTag')
        return cousertag

    @staticmethod
    def getMetaTitle():
        metatitle = config.get('common user info', 'metaTitle')
        return metatitle

    @staticmethod
    def getMetaDesc():
        metadesc = config.get('common user info', 'metaDescription')
        return metadesc