# __author__ = 'ming'
# coding=utf-8

import python.conn as conn
import python.log  as log
import datetime
import decimal
from python.globals import code as Code
from python.globals import reg

from f_sql import *

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
            "bb_who": arg_res.bb_who,
            "bb_postCount": decimal_deal(arg_res.bb_postCount),
            "bb_replyCount": decimal_deal(arg_res.bb_replyCount),
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


def get_boards_all():
    """
    获取大版块和大版块下的一级版块
    """
    log.log_D("into get_boards_all :")

    data = []
    code = Code.SuccessCode
    try:
        db = conn.getWebDB()
        result = db.query(SBig_sql)
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
        code = Code.FailCode

    return code, data


def delete_big_board(arg_tid):
    """
     大版块删除操作
     如果不存在附属的小版块，则可以删除

     Args:
       arg_tid：大版块数据标识 tid

    """
    log.log_D("into delete_big_board :")
    code = Code.SuccessCode

    db = conn.getWebDB()
    t = db.transaction()
    try:

        for num in range(0, 1):
            n = db.select("t_forum_boards_small", dict(tid=arg_tid), what="bs_tid", where="bs_bigID=$tid")

            if len(n) > 0:
                code = Code.HasSmallBoardsCode
                break

            m = db.delete("t_forum_boards_bigs", dict(tid=arg_tid), where="bb_tid=$tid")

            if m < 0:
                code = Code.FailDeleteBigCode
                break

            break

    except Exception as e:
        log.log_E("delete_big_board:" + e.message)
        code = Code.FailCode
        t.rollback()
    else:
        t.commit()

    return code


def add_big_board(arg_input, arg_who):
    """
     大版块添加操作

     Args:
       arg_input：需要数据
                  字典
                  {
                  bb_name
                  bb_imgUrl
                  bb_description
                  }
        arg_who:操作人id，用来判断权限

     Return:
        如果 code 为  Code.SuccessCode 则是操作成功，
        否则是失败（具体查看globals.code）

    """
    log.log_D("into add_big_board :")
    code = Code.SuccessCode
    db = conn.getWebDB()
    t = db.transaction()
    try:

        for num in range(0, 1):
            if ("bb_name" not in arg_input or
                        "bb_imgUrl" not in arg_input or
                        "bb_description" not in arg_input or
                        reg.NumOnly.match(arg_who) is None):
                code = Code.NohasParamCode
                break

            n = db.select("t_forum_boards_permission", dict(tid=arg_who), what="bp_tid",
                          where="bp_uid=$tid and bp_btype=1000")

            if len(n) != 1:
                code = Code.NoPermissionCode
                break

            count = db.insert("t_forum_boards_bigs", bb_name=arg_input.bb_name, bb_imgUrl=arg_input.bb_imgUrl,
                              bb_description=arg_input.bb_description, bb_admin=arg_who,
                              bb_createDate=datetime.datetime.now())  # , bb_vieworder=4

            if count is None or count <= 0:
                code = Code.FailDeleteBigCode
                break


    except Exception as e:
        log.log_E("add_big_board:" + e.message)
        code = Code.FailCode
        t.rollback()
    else:
        t.commit()

    return code