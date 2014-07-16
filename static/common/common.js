/**
 * Created by ming on 2014/7/13.
 */

//document.write(" <script language='javascript' src='jquery-extend.js ' ><\/script>");

function checkData(arg_data) {
    if (!arg_data || arg_data == null)
        return false
    if (arg_data.hasOwnProperty("code") && arg_data.code != 0) {
        if (arg_data.hasOwnProperty("describe"))
            alert(arg_data.describe);
        else
            alert("网路异常，请稍后重试！")
        return false
    }

    return true
}