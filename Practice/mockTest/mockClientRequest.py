import unittest
import mock
from mockTest import clientRequest

class TestClient(unittest.TestCase):

    # def test_success_request(self):
    #     clientRequest.send_request = mock.Mock(return_value='200')
    #     self.assertEqual(clientRequest.visit_taobao(),'200')

    def test_call_send_request_with_right_arguments(self):
        clientRequest.send_request = mock.Mock()
        clientRequest.visit_taobao()
        self.assertEqual(clientRequest.send_request.called, True)
        call_args = clientRequest.send_request.call_args
        self.assertIsInstance(call_args[0][0], str)

    def test_fail_request(self):
        status_code = '200'
        fail_send = mock.Mock(return_value=status_code)
        with mock.patch('clientRequest.send_request',fail_send):
            self.assertEqual(str(clientRequest.visit_taobao()), str(status_code))

if __name__ == '__main__':
    unittest.main()
