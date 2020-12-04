import logging

class Logger():

    @classmethod
    def getLogger(self, name, level=logging.DEBUG):
        logger = logging.getLogger(name)
        logger.setLevel(level)
        ch = logging.StreamHandler()
        ch.setLevel(level)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        logger.addHandler(ch)

        return logger
