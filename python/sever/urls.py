# __author__ = 'ming'
# coding=utf-8

from login import login

controller = "python.controllers."

URLS = (
    "/", "python.sever.urls.pythonTest",
    "/login", "python.sever.login",
    "/Forum/BoardsAll", controller + "Forum.handle.BoardsAll",
)


class pythonTest:
    def GET(self):
        return "this is a python web"

