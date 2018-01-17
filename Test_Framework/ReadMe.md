Test_Rramework
    |--config (配置文件)config层，放配置文件，把所有的项目相关的配置均放到这里，用Python支持较好的配置文件格式如ini或yaml等进行配置。实现配置与代码分离。
    |--data   (数据文件)data层，放数据文件，可以把所有的testcase的参数化相关的文件放到这里，一般可采用xlsx、csv、xml等格式。实现数据与代码分离。
    |--drivers (驱动文件)drivers层，放所需的驱动，如Chromedriver、IEDriverServer等。
    |--log     (日志文件)log层，所有生成的日志均存放在这里，可将日志分类，如运行时日志test log，错误日志error log等。
    |--report  (报告文件)report层，放程序运行生成的报告，一般可有html报告、excel报告等。
    |--src test(测试用例)src源码层，放所有程序代码。其中还需要进行更进一步的分层：
        test层，放所有测试相关的文件，如case——测试用例、common——项目相关的抽象通用代码、page——页面类（Page-Object思想）、suite——组织的测试套件。
    |--Utils   (公共方法)utils层，所有的支撑代码都在这里，包括读取config的类、写log的类、读取excel、xml的类、生成报告的类（如HTMLTestRunner）、数据库连接、发送邮件等类和方法，都在这里。
    |--ReadMe  (说明文件)告诉团队成员框架需要的环境以及用法

selesium3.4.1和python3.6.1
学习网址：http://blog.csdn.net/huilan_same/article/details/76572411
1.new 多个上述的Python package，用于存放不同文件
2.单个python文件，代码部分方法，变成一个类时，就是class 类名(unittest.TestCase):
  变成方法时，就是 def 方法名（self），原本的属性要通过self.属性访问。
3.关于yml文件，需要在python的安装路径Scripts目录下，左手按住shift键，右键点击在此处打开命令窗口，输入pip install pyyaml
4.直接在名为config的python package下新建一个文件，命名为config.yml，yml文件，写法URL: http:www.baidu.com。注意冒号后面一定有个空格。
5.在utils中新建file_reader.py文件，为了读取yaml文件，封装一个yamlReader类
6.在utils中创建一个config.py文件读取配置文件。
7.config.py，from utils.file_reader import YmalReader导入不成功，百度方案：在pycharm中设置source路径file–>setting–>project–>project structure
  点击项目名，右键选择source，点击底部的ok。这样import的模块类等，就是通过这些source文件夹作为根路径来查找，也就是在这些source文件夹中查找import的东西。
8.LOG，在utils中创建log.py文件，python本身有很方便的logging库，只需简单封装。log配置过程中比较顺利。
9.修改file_reader.py。把数据放到excel中，并读取。以便实现数据分离，参数化。在python.exe目录，左手按住shilf，右键在此处打开命令窗口，输入pip install xlrd
  xlrd（读excel）表、xlwt（写excel）表、openpyxl（可读写excel表）
 10.在看生成报告时，遇到困难，看不懂，只能硬着头皮再看看，原来就是复制博主的HTMLTestRunner.py放到utils目录下，然后在用例中进行调用就可以生成html文件，在浏览器中打开就能查看报告了。
 11.如果把方法名的第一个字母大写，程序运行竟然不把它当方法，直接跳过了




