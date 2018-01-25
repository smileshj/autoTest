import unittest
import mock
from mock import patch
from mockTest import function


class MyTestCase(unittest.TestCase):
    # 将mock的multiply()函数（对象）重命名为mock_multiply对象。
    def test_call_multiply_with_right_arguments(self):
        x = 3
        y = 5
        function.multiply = mock.Mock(return_value=15)
        addition, multiple = function.add_and_multiply(x, y)
        print(addition, multiple)
        self.assertEqual(function.multiply.called, True)
        call_args = function.multiply.call_args
        self.assertIsInstance(call_args[0][0],int)
        function.multiply.assert_called_once_with(3, 5)
        self.assertEqual(8, addition)
        self.assertEqual(15, multiple)

    """
    # 无效
    @patch("function.multiply")
    def test_add_and_multiply2(self, mock_multiply):
        x = 3
        y = 5
        mock_multiply.return_value = 15
        addition, multiple = function.add_and_multiply(x, y)
        mock_multiply.assert_called_once_with(3, 5)
        self.assertEqual(8, addition)
        self.assertEqual(15, multiple)

    # 无效
    def test_add_and_multiply(self):
        x,y = 3,5
        success_mul = mock.Mock(return_value=15)
        with mock.patch('function.multiply',success_mul):
            addition, multiple = function.add_and_multiply(x, y)
            success_mul.assert_called_once_with(3, 5)
            print(addition, multiple)
            self.assertEqual(8, addition)
            self.assertEqual(15, multiple)
"""

if __name__ == "__main__":
    unittest.main()
