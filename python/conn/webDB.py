# __author__ = 'ming'
# coding=utf-8

import web

webDB = None

webConfig = {}

webDBUrl = None


def getWebDB():
    '''
      获取web数据库句柄
    '''
    global webDB

    if webDB is not None:
        return webDB
    if webConfig is None:
        raise "please set db config first"
    #try:
    print(webConfig)
    webDB = web.database(webConfig)
    # except:
    #     raise "init web db fail"
    return webDB


def setWebConfig(argUrl=None, **kwargs):
    global webConfig
    webConfig = kwargs
    global webDBUrl
    webDBUrl = argUrl


def setDbUrl(argUrl):
    global webDBUrl
    webDBUrl = argUrl
