import yaml
import os
from xlrd import open_workbook

class YamlReader:
    #判断文件路径是否存在，不存在则返回None
    def __init__(self,yamlf):
        if os.path.exists(yamlf):
            self.yamlf = yamlf
        else:
            raise FloatingPointError('文件不存在!')
        self._data = None

    # @property负责把一个方法变成属性，是属性就有getter和setter方法，比如把data方法变成属性(加了@property)后，可以新建方法 @data.setter  def data(self, value):self._data = value
    @property
    def data(self):
        #如果是首次调用data，则读取yaml文件，否则返回之前读取保存的数据。
        if not self._data:
            with open(self.yamlf,'rb') as f:
                self._data = list(yaml.safe_load_all(f))  # load后是个generator，用list组织成列表
        return self._data

class SheetTypeError(Exception):
    pass

class ExcelReader:
    """
       读取excel文件中的内容。返回list。

       如：
       excel中内容为：
       | A  | B  | C  |
       | A1 | B1 | C1 |
       | A2 | B2 | C2 |

       如果 print(ExcelReader(excel, title_line=True).data)，输出结果：
       [{A: A1, B: B1, C:C1}, {A:A2, B:B2, C:C2}]

       如果 print(ExcelReader(excel, title_line=False).data)，输出结果：
       [[A,B,C], [A1,B1,C1], [A2,B2,C2]]

       可以指定sheet，通过index或者name：
       ExcelReader(excel, sheet=2)
       ExcelReader(excel, sheet='BaiDuTest')
       """
    def __init__(self, excel, sheet=0 ,title_line=True):
        if os.path.exists(excel):
            self.excel = excel
        else:
            raise FileNotFoundError("文件不存在!")
        self.sheet = sheet
        self.titile_line = title_line
        self._data = list()

    @property
    def data(self):
        if not self._data:
            workbook = open_workbook(self.excel)
            if type(self.sheet) not in [int,str]:
                raise SheetTypeError('Please pass in <type int> or <type str>,not {0}'.format(type(self.sheet)))
            elif type(self.sheet) == int:
                s = workbook.sheet_by_index(self.sheet)
            else:
                s = workbook.sheet_by_name(self.sheet)

            if self.titile_line:
                title = s.row_values(0)  #首行为title
                for column in range(1, s.nrows):
                    #依次遍历行，与首行组成dict，拼到self.data中
                    self._data.append(dict(zip(title, s.row_values(column))))
        return self._data

if __name__ == '__main__':
    #在config.yml中添加excel结构的数据
    y = 'E:\Program\pythonProject\Test_Framework\config\config.yml'
    reader = YamlReader(y)
    print(reader.data)

    #在data目录下添加excel文件
    # e = 'E:/Program/pythonProject/Test_Framework/data/baidu.xlsx'
    # reader = ExcelReader(e, title_line=True)
    # print(reader.data)