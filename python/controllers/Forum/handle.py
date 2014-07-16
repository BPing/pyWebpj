# __author__ = 'ming'
# coding=utf-8

from dbctrl import *
from python.globals import Res, code
import json
import web


class BoardsAll():
    def GET(self):
        res = Res()
        res.code, res.msg = get_boards_all()
        return json.dumps(res.dict())


class BoardBigDeal():
    """
    大版块的增删改

    """

    def POST(self):
        f_res = Res()
        f_put = web.input()

        for num in range(0, 1):
            if "method" not in f_put and f_put.method not in ("delete", "add", "update"):
                f_res.setCode(code.NoMethodErrCode)
                break

            # 删除
            if f_put.method == "delete":
                if "tid" not in f_put:
                    f_res.setCode(code.NohasParamCode)
                    break

                f_res.setCode(delete_big_board(f_put.tid))

                break

            # 添加
            elif f_put.method == "add":
                break

            # 更新
            elif f_put.method == "update":
                break

            break

        return json.dumps(f_res.dict())


class BoardSmallDeal():
    def POST(self):
        f_res = Res()
        f_put = web.input()

        for num in range(0, 1):
            if "method" not in f_put and f_put.method not in ("delete", "add", "update"):
                f_res.code(code.NoMethodErrCode)
                break

            if f_put.method == "delete":
                break
            elif f_put.method == "add":
                break
            elif f_put.method == "updatae":
                break

            break

        return json.dumps(f_res.dict())