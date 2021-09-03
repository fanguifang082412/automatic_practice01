import os
import logging
import logging.handlers

# print(os.getcwd())#获得当前文件的绝对路径
# print(os.path.abspath("."))#获得当前位置的绝对路径
# print(os.sep)
import time

logging_dir = "logging_day"
logging_path = os.getcwd() + os.sep + logging_dir

if not os.path.exists(logging_path):
    os.makedirs(logging_path)


# 初始化日志器
logging.basicConfig(level=logging.DEBUG)

myapp = logging.getLogger("ceshi_logging")
myapp.setLevel(logging.DEBUG)

timefilehandler = logging.handlers.TimedRotatingFileHandler(logging_path + os.sep + "time_logging.log", when="M", interval=1, backupCount=3)
timefilehandler.suffix = "%Y-%m-%d.log"

formatter = logging.Formatter('%(asctime)s|%(name)-12s: %(levelname)-8s %(message)s')
timefilehandler.setFormatter(formatter)
myapp.addHandler(timefilehandler)

while True:
    time.sleep(6)
    myapp.info("test")






