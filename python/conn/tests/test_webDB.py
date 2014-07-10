# __author__ = 'ming'
# coding=utf-8

import unittest
from conn import webDB


ErrMsg = (
    "please set db config first",
    "init web db fail"
)


class TestWebDB(unittest.TestCase):
    """
      web数据库句柄单元测试
    """
    # 初始化工作
    def setUp(self):
        pass

    # 退出清理工作
    def tearDown(self):
        pass

    def testDB(self):

        self.assertRaises(Exception, webDB.getWebDB)
        try:
            webDB.getWebDB()
        except Exception, err:
            # print(err.message)
            self.assertEqual(err.message, ErrMsg[0], "")

        try:
            webDB.setWebConfig(db="mysql")
            webDB.getWebDB()
        except Exception, err:
            # print(err.message)
            self.assertEqual(err.message, ErrMsg[1], "")

        self.assertRaises(Exception, webDB.getWebDB)

        webDB.setDbUrl(None)

        webDB.webDB = 1

        self.assertNotEqual(webDB.getWebDB(), None, "should not be None")






