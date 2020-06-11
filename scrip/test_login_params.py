import unittest, logging

from parameterized import parameterized

import app
from api.login_api import LoginApi
from utils import read_login_data


class TestIHRMLoginParams(unittest.TestCase):
    # 进行初始化
    def setUp(self):
        self.login_api = LoginApi()

    def tearDown(self):
        pass

    # 定义登录数据文件的路径
    filepath = app.BASE_DIR + "/data/login_data.json"

    @parameterized.expand(read_login_data(filepath))
    # 编写登录成功函数
    def test01_login_success(self, case_name, request_body, success, code, message, http_code):
        response = self.login_api.login(request_body,
                                        {"Content-Type": "application/json"})
        # 打印响应数据
        logging.info("登录成功的结果为：{}".format(response.json()))
        # assert_common(self,200,True,10000,"操作成功",response)
        # 断言
        self.assertEqual(http_code, response.status_code)
        self.assertEqual(success, response.json().get("success"))
        self.assertEqual(code, response.json().get("code"))
        self.assertIn(message, response.json().get("message"))
