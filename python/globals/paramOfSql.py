# __author__ = 'ming'
# coding=utf-8


import datetime
import decimal


DateFormat = '%Y-%m-%d %H:%M:%S'


def strftime(arg_datetime, format):
    """
     时间处理
    """
    if arg_datetime is None or isinstance(arg_datetime, datetime.datetime) == False:
        return ""
    return arg_datetime.strftime(format)


def decimal_deal(arg_decimal):
    """
     数字处理
    """
    if arg_decimal is None or arg_decimal == "" or isinstance(arg_decimal, decimal.Decimal) == False:
        return 0
    return str(arg_decimal)