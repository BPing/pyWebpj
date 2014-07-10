# coding=utf-8

import config
import log
import sever
import conn

# 配置文件初始化
log.log_I("read the config file:")
config.initConfig("config/config.json")
log.log_I(config.get_config())

# 日志初始化
log.log_D(config.get_config("LOG_PATH") + config.get_config("LOG_FILE_NAME"))
log.initLog(1, "web", config.get_config("LOG_PATH") + config.get_config("LOG_FILE_NAME"))

log.log_D(config.get_config("LOG_PATH") + config.get_config("LOG_FILE_NAME"))


log.log_D("init the db:")
conn.setWebConfig(dbn="mysql",db=config.get_config("DB_NAME"),user=config.get_config("DB_USER"),
                  pw=config.get_config("DB_PW"),host=config.get_config("DB_HOST"),port=config.get_config("DB_PORT"))

if __name__ == '__main__':
    sever.run()

