# -*-coding:utf-8-*-

import logging
from time import strftime

def write_log(level, message):

    now = strftime("%Y-%m-%d")  #获取当前时间
    logname = './output/log/' + now + "log.log" 

    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s : %(levelname)s  %(message)s',
        datefmt='%H:%M:%S',
        filename=logname,
        filemode='a')
    
    # Print information              # 输出日志级别
    if level == 'debug':
        logging.debug(message)
    elif level == 'info':
        logging.info(message)
    elif level == 'warning':
        logging.warning(message)
    elif level == 'error':
        logging.error(message)
    elif level == 'critical':
        logging.critical(message)