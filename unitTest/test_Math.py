from calculator import Math
import unittest

class TestMath(unittest.TestCase):
    #前置条件
    def setUp(self):
        print("test start")

    #添加方法，调用culculator.py中Math Class中的方法
    def test_add(self):
        j=Math(5,10)
        self.assertEqual(j.add(),15)
        # self.assertEqual(j.add(), 12)

    def test_minus(self):
        j = Math(20, 10)
        self.assertEqual(j.minus(),1)#相减正确结果10，这里写个错误结果

    #测试结束，数据还原，后置条件
    def tearDown(self):
        print("test end")

#运行方法:选中main这行，然后右键run
if __name__=='__main__':
    #构造测试集
    unittest.main()
    suite=unittest.TestSuite()
    suite.addTest(TestMath("test_add"))
    suite.addTest(TestMath("test_minus"))

    #执行测试
    runner=unittest.TextTestRunner()
    runner.run(suite)