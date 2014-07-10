# __author__ = 'ming'
# coding=utf-8

try:
    import web
except ImportError:
    raise "import web error"

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
    if len(webConfig) == 0:
        raise Exception("please set db config first")
    try:
        print(webConfig)
        webDB = web.database(webDBUrl, **webConfig)
    except Exception, err:
        print err
        raise Exception("init web db fail")
    return webDB


def setWebConfig(argUrl=None, **kwargs):
    global webConfig
    webConfig = kwargs
    global webDBUrl
    webDBUrl = argUrl


def setDbUrl(argUrl):
    global webDBUrl
    webDBUrl = argUrl
