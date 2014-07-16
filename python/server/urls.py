# __author__ = 'ming'
# coding=utf-8

import web
import python.log as log

controller = "python.controllers."
server = "python.server."

URLS = (
    "/", server + "urls.pythonTest",
    "/login", server + "login.Login",
    "/logout", server + "login.LogOut",
    "/Forum/BoardsAll", controller + "Forum.handle.BoardsAll",
)


class pythonTest:
    def GET(self):
        web.ctx.session.count += 1
        log.log_D(web.ctx.session.get("count"))
        return "this is a python web"

    def POST(self):
        f_input = web.input()
        log.log_D(f_input.test)
        return "this is a python web"

