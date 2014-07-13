# __author__ = 'ming'
# coding=utf-8

from code import app

import python.config as config
import python.conn as conn

# 设置测试数据库
conn.setWebConfig(dbn="mysql",
                  db=config.get_config("TEST_DB_NAME"),
                  user=config.get_config("TEST_DB_USER"),
                  pw=config.get_config("TEST_DB_PW"),
                  host=config.get_config("TEST_DB_HOST"),
                  port=config.get_config("TEST_DB_PORT"))

TestApp = app
TestConn=conn
