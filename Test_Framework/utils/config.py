"""
读取配置。这里配置文件用的yaml，也可用其他如XML,INI等，需在file_reader中添加相应的Reader进行处理。
"""
import os
from utils.file_reader import YamlReader


# 通过当前文件的绝对路径，其父级目录一定是框架的base目录，然后确定各层的绝对路径。
#路径+'\\xxx\\ss'这样不支持跨平台。os.path.split()和os.path.join()，可以支持linux和windows等不同的平台。
#dirname：E:\Program\pythonProject\Test_Framework\src\，文件split以\分割，分割结果是索引为[0]:'E:\Program\pythonProject\Test_Framework'，索引为[1]'src'
BASE_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
CONFIG_FILE = os.path.join(BASE_PATH,'config','config.yml')
DATA_PATH = os.path.join(BASE_PATH,'data')
DRIVER_PATH = os.path.join(BASE_PATH,'drivers')
LOG_PATH = os.path.join(BASE_PATH,'log')
REPORT_PATH = os.path.join(BASE_PATH,'report')

class Config:

    def __init__(self, config=CONFIG_FILE):
        self.config = YamlReader(config).data


    """
    yaml可以通过‘---’分节。用YamlReader读取返回的是一个list，第一项是默认的节，如果有多个节，可以传入index获取。
    我们可以把框架相关的配置放在默认节点，其它的关于项目的配置放在其它节点中。可以在框架中实现多个项目的测试。
    """
    def getInfo(self,element,index=0):
        return self.config[index].get(element)


if __name__ == '__main__':
    c=Config()
    c.getInfo('URL')
