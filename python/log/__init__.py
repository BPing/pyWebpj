# __author__ = 'ming'
# coding=utf-8

from log import Logger

rootLog = Logger(1, "rootLog")


def initLog(arg_level, arg_loggerName, arg_filename=None):
    global rootLog
    rootLog = Logger(arg_level, arg_loggerName, arg_filename)


def log_D(msg, *args, **kwargs):
    if rootLog is not None:
        rootLog.log_D(msg, *args, **kwargs)


def log_I(msg, *args, **kwargs):
    if rootLog is not None:
        rootLog.log_I(msg, *args, **kwargs)


def log_E(msg, *args, **kwargs):
    if rootLog is not None:
        rootLog.log_E(msg, *args, **kwargs)


def log_W(msg, *args, **kwargs):
    if rootLog is not None:
        rootLog.log_W(msg, *args, **kwargs)