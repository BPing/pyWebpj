# __author__ = 'ming'
# coding=utf-8

import python.config as config

# 日志相对全路径
LogFilePath = config.get_config("LOG_PATH") + config.get_config("LOG_FILE_NAME")

# 日志文件名（包括后缀名）
LogFileName = config.get_config("LOG_FILE_NAME")



