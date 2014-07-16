# __author__ = 'ming'
# coding=utf-8

# 返回状态代码与描述
CodeMsg = {
    "0": "成功",
    "-1": "失败",
    "404": "请先登录",
    "505": "参数缺失",
    "606": "没有此操作权限",
    "1001": "参数格式错误",
    "1002": "账户或者密码错误",
    "2001": "缺少method字段，无法确定您的操作目的",
    "2002": "该版块已存在小版块",
    "2003": "删除该版块失败，请稍后重试"
}

SuccessCode = "0"
FailCode = "-1"
NoLoginCode = "404"
NohasParamCode = "505"
NoPermissionCode = "606"
ParamErrCode = "1001"
AccountOrPwErrCode = "1002"

# Boards
NoMethodErrCode = "2001"
HasSmallBoardsCode = "2002"
FailDeleteBigCode = "2003"