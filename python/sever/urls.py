# __author__ = 'ming'
# coding=utf-8

from login import login

URLS = (
    "/", "python.sever.urls.pythonTest",
    "/login", "python.sever.login",
)


class pythonTest:
    def GET(self):
        return "this is a python web"

