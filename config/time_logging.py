import os
import logging
import logging.handlers


def init_logging_config():
    fmt = '%(asctime)s|%(name)-12s: %(levelname)-8s %(message)s'

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    formater = logging.Formatter(fmt)

    #日志输出到控制台
    sh = logging.StreamHandler()
    sh.setFormatter(formater)
    logger.addHandler(sh)

    #日志输出到文件
    # logging_file_dir = "log"
    logging_path = r"C:\Users\Administrator\PycharmProjects\pythonProject\log\log_everyday"


    th = logging.handlers.TimedRotatingFileHandler(logging_path+ ".log", when="MIDNIGHT", interval=1, backupCount=3)
    th.setFormatter(formater)
    logger.addHandler(th)

print(os.path.abspath(".."))