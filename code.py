# coding=utf-8

import sys
import os


# 把自定义模块放进sys.path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
pjPath = os.path.dirname(os.path.abspath(__file__))

import python.config as config
import python.log as log
import python.conn as conn
import python.server as server


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

# web.config

# web.config.session_parameters['cookie_name'] = 'webpy_session_id'
# web.config.session_parameters['cookie_domain'] = None
web.config.session_parameters['timeout'] = 20,  # in seconds
web.config.session_parameters['ignore_expiry'] = True
# web.config.session_parameters['ignore_change_ip'] = True
# web.config.session_parameters['secret_key'] = 'fLjUfxqXtfNoIldA0A0J'
# web.config.session_parameters['expired_message'] = 'Session expired'


try:

    log.log_D("app run:")
    # 应用初始
    app = web.application(server.URLS, globals(), autoreload=True)

    web.config.debug = False

    # session处理
    log.log_D("session init:")
    session = web.session.Session(app, web.session.DiskStore(os.path.join(pjPath, 'sessions')),
                                  initializer={'count': 0, "login": False,
                                               "user_id": "", "user_account": "",
                                               "user_name": ""})

    def my_processor(handler):
        """
        加个处理器(等同中间件)
        路由为/l/*,则校验是否登陆，为登录，则返回404（请查看python.globals.code）
        """
        if web.ctx.fullpath.split("/")[1].lower() == "l":
            from python.globals.Res import Res

            if web.ctx.session.get("login", False) == False:
                return Res("404").dict()

        result = handler()
        return result

    # 钩子
    def session_hook():
        web.ctx.session = session

    app.add_processor(web.loadhook(session_hook))
    app.add_processor(my_processor)


    # 启动wsgi服务
    application = app.wsgifunc()

except Exception, e:
    log.log_E(e)



