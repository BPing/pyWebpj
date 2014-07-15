# __author__ = 'ming'
# coding=utf-8

from dbctrl import *
from python.globals.Res import Res
import json


class BoardsAll():
    def GET(self):
        res = Res()
        res.code, res.msg = getBoardsAll()
        return json.dumps(res.dict())


class AddBoardBig():
    def POST(self):
        res = Res()


        return json.dumps(res.dict())