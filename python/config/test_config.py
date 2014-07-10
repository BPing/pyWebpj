# __author__ = 'ming'
# coding=utf-8
import unittest
import config
import os


config_file = "config/testconfig.json"


class config_test(unittest.TestCase):
    """
     配置文件测试
    """

    # 初始化工作
    def setUp(self):
        self.c_config = config.Config(config_file)

    # 退出清理工作
    def tearDown(self):
        pass

    @unittest.skipIf(os.path.isfile(config_file) != True, "can't find config file")
    def test_config(self):
        print(self.c_config.get_config())
        self.assertEqual(self.c_config.get_config("LOG_PATH"), "logTXT/")
        self.assertEqual(self.c_config.get_config("LOG_FILE_NAME"), "web.log")
        self.c_config.set_config("ROOT", "Root")
        self.assertEqual(self.c_config.get_config("ROOT"), "Root")
        self.assertEqual(self.c_config.get_config("None"), "")
        self.assertEqual(config.Config().get_config(),{})
        self.assertEqual(config.Config("None/log.log").get_config(),{})



if __name__ == '__main__':
    unittest.main()