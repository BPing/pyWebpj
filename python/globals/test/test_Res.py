# __author__ = 'ming'
# coding=utf-8

import unittest
from python.globals import Res

testMsg = {'Size': 2, 'List': [{'name': 1, 'code': 2}, {}]}


class TestRes(unittest.TestCase):
    """
      返回数据结构Res测试
    """
    # 初始化工作
    def setUp(self):
        pass

    # 退出清理工作
    def tearDown(self):
        pass

    def testInit(self):
        print("testInit:")
        res = Res()
        self.assertEqual(res.code, 0, "thd code of init 'res' is not 0 ")

    def testDo(self):
        print("testDo:")
        res = Res()
        res.setCode(-1)
        self.assertEqual(res.code, -1, "set code error")

        res.setCode('123')
        self.assertEqual(res.getCode(), -1, "can't type str to type int ")

        res.setMsg(testMsg)
        self.assertEqual(res.getMsg(), testMsg, "set the msg error")

        res.setDescribe("test")
        self.assertEqual(res.getDescribe(), "test", "set the msg error")

        res.setAll(code=2, msg="test", describe="test")
        self.assertEqual(res.getCode(), 2, "set the msg error")
        self.assertEqual(res.getMsg(), "test", "set the msg error")

        ds=res.dict()
        self.assertEqual(ds["msg"], "test", "set the msg error")
