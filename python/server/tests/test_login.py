# __author__ = 'ming'
# coding=utf-8


import unittest
from testHttp import TestApp as App
from testHttp import TestConn as conn
import json
from python.globals import code, gobal


class TestLoginOrOut(unittest.TestCase):
    """
     登陆和退出单元测试
    """
    # 初始化工作
    def setUp(self):
        db = conn.getWebDB()
        t = db.transaction()
        try:
            db.insert("sys_user", u_tid='99999', u_name="林杰", u_account="1106100150",
                      u_password="123456", u_level=10, u_loginNumber=10, u_lastLoginTime="2014-07-06 23:09:06")
            db.insert("sys_user", u_tid='999999', u_name="林不解", u_account="1106100150",
                      u_password="123456", u_level=10, u_loginNumber=10, u_lastLoginTime="2014-07-06 23:09:06")
            db.insert("sys_user", u_tid='9999999', u_name="林杰林林", u_account="1106100151",
                      u_password="123456", u_level=10, u_loginNumber=10, u_lastLoginTime="2014-07-07 23:09:06")

        except Exception as e:
            print(e)
            t.rollback()
        else:
            t.commit()

        self.app = App

    # 退出清理工作
    def tearDown(self):
        db = conn.getWebDB()
        db.delete("sys_user", where="u_tid in('99999','999999','9999999')")

    def testLogin(self):
        """
        登陆
        """

        # 同时存在两个
        r = self.app.request("/login", "POST", data=dict(u_account=1106100150, u_pw=123456))
        self.assertEqual(r.status, '200 OK', "request error")
        decodejson = json.loads(r.data)
        self.assertTrue(decodejson["code"] == code.AccountOrPwErrCode, "request error")

        # 不存在
        r = self.app.request("/login", "POST", data=dict(u_account=11061001501, u_pw=123456))
        self.assertEqual(r.status, '200 OK', "request error")
        decodejson = json.loads(r.data)
        self.assertTrue(decodejson["code"] == code.AccountOrPwErrCode, "request error")

        # 正确
        r = self.app.request("/login", "POST", data=dict(u_account=1106100151, u_pw=123456))
        self.assertEqual(r.status, '200 OK', "request error")
        decodejson = json.loads(r.data)
        self.assertTrue(decodejson["code"] == code.SuccessCode, "request error")

        # 正确
        gobal.TestOn = True
        r = self.app.request("/login", "POST", data=dict(u_account=1106100150, u_pw=123456))
        self.assertEqual(r.status, '200 OK', "request error")
        decodejson = json.loads(r.data)
        self.assertTrue(decodejson["code"] == code.FailCode, "request error")
        gobal.TestOn = False

        # 参数错误
        r = self.app.request("/login", "POST", data=dict(u_account="11061001516%$", u_pw=123456))
        self.assertEqual(r.status, '200 OK', "request error")
        decodejson = json.loads(r.data)
        self.assertTrue(decodejson["code"] == code.ParamErrCode, "request error")

    def testLogOut(self):
        """
        退出注销
        """
        r = self.app.request("/logout", "POST")
        self.assertEqual(r.status, '200 OK', "request error")
        decodejson = json.loads(r.data)
        self.assertTrue(decodejson["code"] == code.SuccessCode, "request error")

        # 异常测试开关
        gobal.TestOn = True
        r = self.app.request("/logout", "POST")
        self.assertEqual(r.status, '200 OK', "request error")
        decodejson = json.loads(r.data)
        self.assertTrue(decodejson["code"] == code.FailCode, "request error")
        gobal.TestOn = False

        r = self.app.request("/", "POST", data={"test": "testPOST"})
        print(r.items())