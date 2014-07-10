# coding=utf-8

import config
import log
import sever

# 配置文件初始化
log.log_I("read the config file:")
config.initConfig("config/config.json")
log.log_I(config.get_config())

# 日志初始化
log.log_D(config.get_config("LOG_PATH") + config.get_config("LOG_FILE_NAME"))
log.initLog(1, "web", config.get_config("LOG_PATH") + config.get_config("LOG_FILE_NAME"))

log.log_D(config.get_config("LOG_PATH") + config.get_config("LOG_FILE_NAME"))

if __name__ == '__main__':
    sever.run()

