import mock
import unittest

from mockTest.modular import Count

class TestCount(unittest.TestCase):

    """
    # 01：add方法内容为空也可以用mock测试
    def test_add(self):
        count = Count()
        count.add = mock.Mock(return_value=13)
        result = count.add(8,5)
        self.assertEqual(result,13)
    """
    """
    # 02:add方法内容有值
    """
    def test_add(self):
        count = Count()
        """
        side_effect参数和return_value是相反的。它给mock分配了可替换的结果，覆盖了return_value。
        简单的说，一个模拟工厂调用将返回side_effect值，而不是return_value。
        所以，设置side_effect参数为Count类add()方法，那么return_value的作用失效。
        """
        count.add = mock.Mock(return_value=13, side_effect=count.add)
        result = count.add(8,2)
        print(result)
        count.add.assert_called_with(8,2)
        self.assertEqual(result,10)

if __name__ == '__main__':
    unittest.main()

