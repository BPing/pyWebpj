# __author__ = 'ming'
# coding=utf-8

import types
from code import CodeMsg


class Res():
    """
      数据返回结构体
    """

    def __init__(self, argCode=0, argMsg=None, argDescribe=""):
        # 返回代码
        if type(argCode) is types.IntType:
            self.code = argCode

        # 返回数据
        self.msg = argMsg

        # 返回描述
        self.describe = argDescribe

    def setMsg(self, arg_Msg):
        self.msg = arg_Msg

    def setCode(self, arg_Code):
        if type(arg_Code) is types.IntType:
            self.code = arg_Code

    def setDescribe(self, arg_describe):
        self.describe = arg_describe

    def setAll(self, **kwargs):
        if 'code' in kwargs.keys():
            self.code = kwargs['code']
        if 'msg' in kwargs.keys():
            self.msg = kwargs['msg']
        if 'describe' in kwargs.keys():
            self.describe = kwargs['describe']

    def getCode(self):
        return self.code

    def getMsg(self):
        return self.msg

    def getDescribe(self):
        return self.describe

    def dict(self):
        if self.code in CodeMsg:
            self.describe = CodeMsg[self.code]
        return {"code": self.code, "msg": self.msg, "describe": self.describe}