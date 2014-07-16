# __author__ = 'ming'
# coding=utf-8

import python.log as log
import web
import json
import datetime
import python.conn as conn
from  python.globals import code, Res, reg, paramOfSql, gobal


class Login():
    """
    登陆处理
    """

    def POST(self):
        log.log_I("into login:")

        f_res = Res()
        try:
            if gobal.TestOn == True:
                raise Exception("test exception")
            for num in range(0, 1):

                f_input = web.input()
                # 参数校验
                if reg.EngAndNum.match(f_input.u_account) is None or reg.EngAndNumAndOt.match(f_input.u_pw) is None:
                    f_res.setCode(code.ParamErrCode)
                    break

                # 数据库查询
                f_db = conn.getWebDB()
                var = dict(u_account=f_input.u_account, u_pw=f_input.u_pw)
                result = f_db.select("sys_user", vars=var,
                                     what="u_tid,u_account,u_password,u_name,u_level,u_loginNumber,u_lastLoginTime",
                                     where=" u_account=$u_account and u_password=$u_pw")

                if (len(result) != 1):
                    f_res.setCode(code.AccountOrPwErrCode)
                    break

                # 保存session
                for one in result:
                    log.log_D(one.u_password)
                    web.ctx.session.user_id = one.u_tid
                    web.ctx.session.user_account = one.u_account
                    web.ctx.session.user_password = one.u_password
                    web.ctx.session.user_name = one.u_name
                    web.ctx.session.user_level = one.u_level
                    web.ctx.session.user_loginNumber = one.u_loginNumber
                    web.ctx.session.user_lastLoginTime = one.u_lastLoginTime
                    web.ctx.session.login = True

                    f_res.setMsg(dict(u_id=one.u_tid,
                                      u_account=one.u_account,
                                      u_level=one.u_level,
                                      u_loginNumber=one.u_loginNumber,
                                      u_lastLoginTime=paramOfSql.strftime(one.u_lastLoginTime, paramOfSql.DateFormat),
                                      u_name=one.u_name))

                    log.log_D(datetime.datetime.now().strftime(paramOfSql.DateFormat))

                    # 更新登陆信息
                    f_db.query(
                        "update sys_user set sys_user.u_lastLoginTime=$time,sys_user.u_loginNumber=sys_user.u_loginNumber+1 where u_tid=$u_tid",
                        dict(time=datetime.datetime.now().strftime(paramOfSql.DateFormat), u_tid=one.u_tid))

                break


        except Exception as e:
            log.log_E(e)
            f_res.setCode("-1")

        return json.dumps(f_res.dict())


class LogOut():
    """
    退出注销处理
    """

    def POST(self):
        f_res = Res()
        try:
            if gobal.TestOn == True:
                raise Exception("test exception")
            web.ctx.session.user_id = ""
            web.ctx.session.user_account = ""
            web.ctx.session.user_password = ""
            web.ctx.session.user_name = ""
            web.ctx.session.user_level = ""
            web.ctx.session.user_loginNumber = ""
            web.ctx.session.user_lastLoginTime = ""
            web.ctx.session.login = False
        except Exception as e:
            log.log_E(e)
            f_res.setCode("-1")

        return json.dumps(f_res.dict())