# __author__ = 'ming'
# coding=utf-8

import unittest
import log
import os

logfile = "logfile/log.log"


class log_test(unittest.TestCase):
    # 初始化工作
    def setUp(self):
        self.log = log.Logger(1, "testLog", logfile)
        self.log.openLog()

    # 退出清理工作
    def tearDown(self):
        if os.path.isfile(logfile) == True:
            try:
                os.remove(logfile)
            except:
                print("remove file fail")

    def test_Log(self):

        self.assertTrue(os.path.isfile(logfile) == True, "未能正确创建日志文件")
        self.log.log_D("Debug")
        self.log.log_I("Info")
        self.log.log_W("Warn")
        self.log.log_E("Error")
        self.log.closeLpg()
        self.log.log_D("close Debug")
        self.log.log_I("close Info")
        self.log.log_W("close Warn")
        self.log.log_E("close Error")
        self.log.log_file_close()


if __name__ == '__main__':
    unittest.main()