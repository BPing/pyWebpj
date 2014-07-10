# __author__ = 'ming'


import web
import log

from urls import URLS


def run():
    log.log_D("app run")
    app = web.application(URLS, globals())
    application = app.wsgifunc()
