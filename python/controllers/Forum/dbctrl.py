# __author__ = 'ming'
# coding=utf-8

import python.conn as conn
import python.log  as log
import datetime


DateFormat = '%Y-%m-%d %H:%M:%S'


def strftime(arg_datetime, format):
    """
     时间处理
    """
    if arg_datetime is None and isinstance(arg_datetime, datetime.datetime) == False:
        return ""
    return arg_datetime.strftime(format)


def boards_bigs_dict(arg_res):
    """
     大版块数据转化成字典
    """
    if "bb_tid" not in arg_res:
        return {}
    return {"bb_tid": arg_res.bb_tid,
            "bb_name": arg_res.bb_name,
            "bb_imgUrl": arg_res.bb_imgUrl,
            "bb_description": arg_res.bb_description,
            "bb_admin": arg_res.bb_admin,
            "bb_createDate": strftime(arg_res.bb_createDate, DateFormat),
            "bb_vieworder": arg_res.bb_vieworder}


def boards_smalls_dict(arg_res):
    """
     小版块数据转化成字典
    """
    if "bs_tid" not in arg_res:
        return {}
    return {
        "bs_tid": arg_res.bs_tid,
        "bs_name": arg_res.bs_name,
        "bs_bigID": arg_res.bs_bigID,
        "bs_imgUrl": arg_res.bs_imgUrl,
        "bs_description": arg_res.bs_description,
        "bs_lastpostID": arg_res.bs_lastpostID,
        "bs_lastpostDate": strftime(arg_res.bs_lastpostDate, DateFormat),
        "bs_whoCreate": arg_res.bs_whoCreate,
        "bs_createDate": arg_res.bs_createDate.strftime(DateFormat),
        "bs_postCount": arg_res.bs_postCount,
        "bs_replyCount": arg_res.bs_replyCount,
        "bs_typeId": arg_res.bs_typeId}


def getBoardsAll():
    """
    获取大版块和大版块下的一级版块
    """
    data = []
    code = "0"
    try:
        db = conn.getWebDB()
        result = db.select("t_forum_boards_bigs", order=" bb_vieworder ", _test=False)
        for res in result:
            # log.log_D(res.bb_createDate)
            var = dict(bb_tid=res.bb_tid)
            f_sbs = db.select("t_forum_boards_small", var, where="bs_bigID=$bb_tid and bs_typeId=1", _test=False)
            f_sbdata = []
            for f_sb in f_sbs:
                f_sbdata.append(boards_smalls_dict(f_sb))

            data.append({"big": boards_bigs_dict(res), "small": f_sbdata})

    except Exception as e:
        log.log_E("getBoardsAll:" + e.message)
        code = "-1"

    return code, data




