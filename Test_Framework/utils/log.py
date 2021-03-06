"""
日志类。通过读取配置文件，定义日志级别、日志文件名、日志格式等。
一般直接把logger import进去
from utils.log import logger
logger.info('test log')
"""
import os
import logging
from logging.handlers import TimedRotatingFileHandler
from utils.config import Config,LOG_PATH

class Logger(object):
    def __init__(self,logger_name='framework'):
        self.logger = logging.getLogger(logger_name)
        logging.root.setLevel(logging.NOTSET)
        c = Config().get('log') #读取config.yml文件下的log目录下的内容
        self.log_file_name = c.get('file_name') if c and c.get('file_name') else 'test.log'  #保留的日志
        self.backup_count = c.get('backup') if c and c.get('backup') else 5                     #保留的日志数量
        #日志输出级别
        self.console_output_level = c.get('console_level') if c and c.get('file_level') else 'DEBUG'
        self.file_output_level = c.get('file_level') if c and c.get('file_level') else 'DEBUG'
        #日志输出格式
        pattern = c.get('pattern') if c and c.get('pattern') else '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        self.formatter = logging.Formatter(pattern)

        """
        self.log_file_name = 'test.log'
        self.backup_count = 5
        #日志输出级别
        self.console_output_level = 'WARRING'
        self.console_output_level = 'DEBUG'
        #日志输出格式
        self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        """

    def get_logger(self):
        #在logger中添加句柄并返回，如果logger已有句柄，则直接返回。避免重复日志
        #在此处添加两个句柄，一个输出日志到控制台，一个输出日志到文件。
        if not self.logger.handlers:
            #输出到控制台的句柄
            console_handler=logging.StreamHandler()
            console_handler.setFormatter(self.formatter)
            console_handler.setLevel(self.console_output_level)
            self.logger.addHandler(console_handler) #添加控制台句柄到logger

            # 输出到文件的句柄，每天重新创建一个日志文件，最多保留backup_count份
            file_handler = TimedRotatingFileHandler(filename=os.path.join(LOG_PATH + self.log_file_name),
                                                    when='D',
                                                    interval=1,
                                                    backupCount=self.backup_count,
                                                    delay=True,
                                                    encoding='utf-8'
                                                    )
            file_handler.setFormatter(self.formatter)
            file_handler.setLevel(self.file_output_level)
            self.logger.addHandler(file_handler)  #添加文件句柄到logger
        return self.logger

logger = Logger().get_logger()