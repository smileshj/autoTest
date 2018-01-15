import yaml
import os


class YamlReader:
    #判断文件路径是否存在，不存在则返回None
    def __init__(self,yamlf):
        if os.path.exists(yamlf):
            self.yamlf = yamlf
        else:
            raise FloatingPointError('文件不存在!')
        self._data = None

    @property
    def data(self):
        #如果是首次调用data，则读取yaml文件，否则返回之前读取保存的数据。
        if not self._data:
            with open(self.yamlf,'rb') as f:
                self._data = list(yaml.safe_load_all(f))  # load后是个generator，用list组织成列表
        return self._data

