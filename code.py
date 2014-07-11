# coding=utf-8

import sys
import os


# 把自定义模块放进sys.path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
pjPath = os.path.dirname(os.path.abspath(__file__))

import python.config as config
import python.log as log
import python.conn as conn
import python.sever as server


# 配置文件初始化
log.log_I("read the config file:")
config.initConfig(os.path.abspath(pjPath + "/config/config.json"))
log.log_I(config.get_config())

# 日志初始化
log.log_D(config.get_config("LOG_PATH") + config.get_config("LOG_FILE_NAME"))
log.initLog(1, "web",
            os.path.abspath(pjPath + "/" + config.get_config("LOG_PATH") + config.get_config("LOG_FILE_NAME")))
log.log_D(config.get_config("LOG_PATH") + config.get_config("LOG_FILE_NAME"))

# 数据库初始
log.log_D("init the db:")
conn.setWebConfig(dbn="mysql",
                  db=config.get_config("DB_NAME"),
                  user=config.get_config("DB_USER"),
                  pw=config.get_config("DB_PW"),
                  host=config.get_config("DB_HOST"),
                  port=config.get_config("DB_PORT"))

# if __name__ == '__main__':

import web

# 启动wsgi服务
try:

    log.log_D("app run:")
    app = web.application(server.URLS, globals())
    application = app.wsgifunc()

except Exception, e:
    log.log_E(e)


