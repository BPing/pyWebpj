$.sendRequest = function (arg_method, arg_url, arg_data, arg_callBack, arg_error) {
    var sendHttp = {
        Start: function () {
            $.ajax({
                type: arg_method,
                url: arg_url,
//                timeout:arg_timeOut,
                data: arg_data,
                dataType: "json",
                success: sendHttp.Successs,
                error: sendHttp.Error
            });
        },
        Successs: function (arg_data) {
            arg_callBack(arg_data);
        },
        Error: function (arg_errMsg) {
            arg_error(arg_errMsg);
        }
    };
    sendHttp.Start();
};



