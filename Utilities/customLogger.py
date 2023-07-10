import logging

class LogGeneration:

    @staticmethod
    def loginformation():
        logging.basicConfig(filename="C:\\Users\\Sindhu\\PycharmProjects\\quickerAutomation\\Logs\\automationlogs", format='%(asctime)s:%(levelname)s:%(message)s', datefmt='%m/%d/%Y  %I:%M:%S %p', force=True)
        log = logging.getLogger()
        log.setLevel(logging.INFO)
        return log