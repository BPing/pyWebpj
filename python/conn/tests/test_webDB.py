# __author__ = 'ming'
#coding=utf-8

import unittest
from conn import webDB
import web


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
        db=web.database(dbn="mysql",db="test",user="ping",pw="123456",host="172.22.71.113",port="3306")
        print db.select("rcp_competence")





