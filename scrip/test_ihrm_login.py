import logging
import unittest

from api.login_api import LoginApi


# from utils import assert_common


class TestIHRMLogin(unittest.TestCase):
    def setUp(self):
        self.login_api = LoginApi()

    def tearDown(self):
        pass

    # 使用封装的接口调用登录接口，并接收返回的响应数据
    def test01_login_success(self):
        response = self.login_api.login({"mobile": "13800000002", "password": "123456"},
                                        {"Content-Type": "application/json"})
        # 打印响应数据
        logging.info("登录成功的结果为：{}".format(response.json()))
        # assert_common(self,200,True,10000,"操作成功",response)
        # 断言
        self.assertEqual(200, response.status_code)
        self.assertEqual(True, response.json().get("success"))
        self.assertEqual(10000, response.json().get("code"))
        self.assertIn("操作成功", response.json().get("message"))

    def test02_mobile_is_empty(self):
        response = self.login_api.login({"mobile": "", "password": "error"},
                                        {"Content-Type": "application/json"})
        # 打印响应数据
        logging.info("手机号为空的结果为：{}".format(response.json()))
        # 断言
        self.assertEqual(200, response.status_code)
        self.assertEqual(False, response.json().get("success"))
        self.assertEqual(20001, response.json().get("code"))
        self.assertIn("用户名或密码错误", response.json().get("message"))

    def test03_mobile_is_not_exists(self):
        response = self.login_api.login({"mobile": "15500000000", "password": "123456"},
                                        {"Content-Type": "application/json"})
        # 打印响应数据
        logging.info("手机号不存在的结果为：{}".format(response.json()))
        # 断言
        self.assertEqual(200, response.status_code)
        self.assertEqual(False, response.json().get("success"))
        self.assertEqual(20001, response.json().get("code"))
        self.assertIn("用户名或密码错误", response.json().get("message"))

    def test04_password_is_error(self):
        response = self.login_api.login({"mobile": "13800000002", "password": "12345"},
                                        {"Content-Type": "application/json"})
        # 打印响应数据
        logging.info("手机号为空的结果为：{}".format(response.json()))
        # 断言
        self.assertEqual(200, response.status_code)
        self.assertEqual(False, response.json().get("success"))
        self.assertEqual(20001, response.json().get("code"))
        self.assertIn("用户名或密码错误", response.json().get("message"))

    # 参数错误
    def test05_parameter_is_error(self):
        response = self.login_api.login({"mobiile": "13800000002", "password": "12345"},
                                        {"Content-Type": "application/json"})
        # 打印响应数据
        logging.info("参数错误的结果为：{}".format(response.json()))
        # 断言
        self.assertEqual(200, response.status_code)
        self.assertEqual(False, response.json().get("success"))
        self.assertEqual(20001, response.json().get("code"))
        self.assertIn("用户名或密码错误", response.json().get("message"))

    # 少参
    def test06_params_is_less(self):
        response = self.login_api.login({"password": "12345"},
                                        {"Content-Type": "application/json"})
        # 打印响应数据
        logging.info("少参的结果为：{}".format(response.json()))
        # 断言
        self.assertEqual(200, response.status_code)
        self.assertEqual(False, response.json().get("success"))
        self.assertEqual(20001, response.json().get("code"))
        self.assertIn("用户名或密码错误", response.json().get("message"))

    # 多参
    def test07_params_is_more(self):
        response = self.login_api.login({"mobile": "13800000002", "password": "123456", "extras_params": "1"},
                                        {"Content-Type": "application/json"})
        # 打印响应数据
        logging.info("多参结果为：{}".format(response.json()))
        # 断言
        self.assertEqual(200, response.status_code)
        self.assertEqual(True, response.json().get("success"))
        self.assertEqual(10000, response.json().get("code"))
        self.assertIn("操作成功", response.json().get("message"))

    # 传入null
    def test08_params_is_null(self):
        response = self.login_api.login(None, {"Content-Type": "application/json"})
        # 打印响应数据
        logging.info("传入null的结果为：{}".format(response.json()))
        # 断言
        self.assertEqual(200, response.status_code)
        self.assertEqual(False, response.json().get("success"))
        self.assertEqual(99999, response.json().get("code"))
        self.assertIn("抱歉，系统繁忙，请稍后重试！", response.json().get("message"))

    #    密码为空
    def test09_password_is_empty(self):
        response = self.login_api.login({"mobile": "13800000002", "password": ""},
                                        {"Content-Type": "application/json"})
        # 打印响应数据
        logging.info("密码为空的结果为：{}".format(response.json()))
        # 断言
        self.assertEqual(200, response.status_code)
        self.assertEqual(False, response.json().get("success"))
        self.assertEqual(20001, response.json().get("code"))
        self.assertIn("用户名或密码错误", response.json().get("message"))
    # 无参
    def test10_param_is_none(self):
        response = self.login_api.login({},
                                        {"Content-Type": "application/json"})
        # 打印响应数据
        logging.info("无参的结果为：{}".format(response.json()))
        # 断言
        self.assertEqual(200, response.status_code)
        self.assertEqual(False, response.json().get("success"))
        self.assertEqual(20001, response.json().get("code"))
        self.assertIn("用户名或密码错误", response.json().get("message"))
