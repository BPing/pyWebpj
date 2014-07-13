# __author__ = 'ming'
# coding=utf-8


import unittest
from testHttp import TestApp as App
from testHttp import TestConn as conn
import datetime
import json


class TestHandle(unittest.TestCase):
    """
     Handle单元测试
    """
    # 初始化工作
    def setUp(self):
        db = conn.getWebDB()
        t = db.transaction()
        try:
            # 大版块数据准备
            db.insert("t_forum_boards_bigs", bb_tid=99999,
                      bb_name="运动百科", bb_imgUrl="", bb_description="运动健康生活",
                      bb_admin="1000", bb_createDate=datetime.datetime.now(), bb_vieworder=2)
            db.insert("t_forum_boards_bigs", bb_tid=999999,
                      bb_name="程序人生", bb_imgUrl="", bb_description="程序人生",
                      bb_admin="1000", bb_createDate=datetime.datetime.now(), bb_vieworder=3)


            # 小版块数据准备

            db.insert("t_forum_boards_small", bs_tid=999999,
                      bs_name="python", bs_bigID=999999, bs_imgUrl="", bs_description="python人生",
                      bs_whoCreate="1000", bs_createDate=datetime.datetime.now(),
                      bs_postCount=0, bs_replyCount=0, bs_typeId=1)

            db.insert("t_forum_boards_small", bs_tid=99999,
                      bs_name="篮球", bs_bigID=99999, bs_imgUrl="", bs_description="篮球人生",
                      bs_whoCreate="1000", bs_createDate=datetime.datetime.now(),
                      bs_postCount=0, bs_replyCount=0, bs_typeId=1)
        except Exception as e:
            print(e)
            t.rollback()
        else:
            t.commit()

        self.app = App

    # 退出清理工作
    def tearDown(self):
        db = conn.getWebDB()
        db.delete("t_forum_boards_small", where="bs_tid in('99999','999999')")
        db.delete("t_forum_boards_bigs", where="bb_tid in('99999','999999')")

    def testBoardsAll(self):
        r = self.app.request("/home/BoardsAll")
        self.assertEqual(r.status, '200 OK', "request error")
        decodejson = json.loads(r.data)
        self.assertTrue(decodejson["msg"][0]["big"]["bb_vieworder"] <= 2, "request error")



