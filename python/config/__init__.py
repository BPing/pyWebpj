# __author__ = 'ming'
# coding=utf-8

from config import Config

rootconfig = Config()


def initConfig(arg_config_file):
    global rootconfig
    rootconfig = Config(arg_config_file)
    print(rootconfig.get_config())


def get_config(arg_key=None):
    if rootconfig is not None:
        return rootconfig.get_config(arg_key)
    return ""


def set_config(arg_key, arg_values):
    if rootconfig is not None:
        return rootconfig.set_config(arg_key, arg_values)
    return ""
