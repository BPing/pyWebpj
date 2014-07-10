# __author__ = 'ming'
# coding=utf-8


import logging
import os


format_dict = {
    1: logging.Formatter('%(asctime)s "%(name)s" [%(levelname)s] :%(message)s'),
    2: logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'),
    3: logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'),
    4: logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'),
    5: logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
}


class Logger():
    # 日志开关
    LogOn = True

    def __init__(self, arg_level, arg_loggerName, arg_filename=None):
        """"
           指定保存日志的文件路径，日志级别，以及调用文件
           将日志存入到指定的文件中
       """

        # 创建一个logger
        self.logger = logging.getLogger(arg_loggerName)
        self.logger.setLevel(logging.DEBUG)

        # 定义handler的输出格式
        # formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        formatter = format_dict[int(arg_level)]

        # 再创建一个handler，用于输出到控制台
        f_console_handler = logging.StreamHandler()
        f_console_handler.setLevel(logging.DEBUG)
        # 定义handler的输出格式
        f_console_handler.setFormatter(formatter)
        # 给logger添加handler
        self.logger.addHandler(f_console_handler)

        # 如果文件路径不为空
        if arg_filename is not None:
            # 路径不存在则创建
            f_dir = os.path.dirname(arg_filename)
            if os.path.isdir(f_dir) == False and f_dir is not None and f_dir != "": os.mkdir(f_dir)

            # 创建一个handler，用于写入日志文件
            f_file_handler = logging.FileHandler(arg_filename)
            f_file_handler.setLevel(logging.DEBUG)
            # 定义handler的输出格式
            f_file_handler.setFormatter(formatter)
            self.fileHandler = f_file_handler
            # 给logger添加handler
            self.logger.addHandler(f_file_handler)

    def getlog(self):
        return self

    def log_D(self, msg, *args, **kwargs):
        if Logger.LogOn:
            self.logger.debug(msg, *args, **kwargs)

    def log_I(self, msg, *args, **kwargs):
        if Logger.LogOn:
            self.logger.info(msg, *args, **kwargs)

    def log_E(self, msg, *args, **kwargs):
        if Logger.LogOn:
            self.logger.error(msg, *args, **kwargs)

    def log_W(self, msg, *args, **kwargs):
        if Logger.LogOn:
            self.logger.warn(msg, *args, **kwargs)

    def openLog(self):
        Logger.LogOn = True

    def closeLpg(self):
        Logger.LogOn = False

    def log_file_close(self):
        if self.fileHandler is not None:
            self.logger.removeHandler(self.fileHandler)
            self.fileHandler.close()





