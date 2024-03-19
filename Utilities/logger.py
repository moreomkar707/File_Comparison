import inspect
import logging


class logGenerator:

    @staticmethod
    def loggen():
        logger = logging.getLogger()

        file = logging.FileHandler("C:\\Users\\admin\\PycharmProjects\\File_Operations\\mylog.log",mode='w')
        formating = logging.Formatter('%(asctime)s : %(name)s : %(lineno)s : %(process)s : %(message)s')
        file.setFormatter(formating)
        logger.addHandler(file)
        logger.setLevel(logging.DEBUG)
        return logger



