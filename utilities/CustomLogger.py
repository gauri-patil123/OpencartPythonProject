import logging
import os.path


class LogGen():
    @staticmethod
    def loggen():
        """
        path = os.path.abspath(os.curdir) + '\\logs\\automation.log'
        logging.basicConfig(filename=path, format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%s %p')
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        return logger
        """

        logging.basicConfig(
        filename = os.path.abspath(os.curdir) + '\\logs\\' +'automation.log',  # Log file name
        level = logging.INFO,  # Log level
        format = '%(asctime)s - %(levelname)s - %(message)s'  # Log format
        )
        logger = logging.getLogger()
        return logger


