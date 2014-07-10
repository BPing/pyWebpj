# __author__ = 'ming'
# coding=utf-8

import json


class Config():
    """
      配置文件的读取并转化为字典，然后通过读取字典获取配置值
    """

    def __init__(self, arg_filename=None):
        if arg_filename is not None:
            print(arg_filename)
            try:
                f_file = file(arg_filename)
                self.__config = json.load(f_file)
                f_file.close
            except:
                self.__config = {}
        else:
            self.__config = {}

    def get_config(self, arg_key=None):
        if arg_key is None:
            return self.__config
        if arg_key in self.__config.keys():
            return self.__config[arg_key]
        else:
            return ""

    def set_config(self, arg_key, arg_values):
        self.__config[arg_key] = arg_values
