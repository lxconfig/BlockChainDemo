import logging


# basicConfig(等级, 日志文件名, 文件打开方式, 日志格式)
logging.basicConfig(
    level=logging.DEBUG,
    filename='./log.txt',
    filemode='w',
    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s'
)

# 使用log功能
logging.info("这是 logging info message")
logging.debug("这是 logging debug message")
logging.warning("这是 logging warning message")
logging.error("这是 logging error message")
logging.critical("这是 logging critical message")