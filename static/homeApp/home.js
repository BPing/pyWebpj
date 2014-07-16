function RootCtrl($scope) {
//    $scope.homepage = "welcome to the python web";


    getBoardAll({}, function (data) {

        if (checkData(data)) {
            if (!data.hasOwnProperty("msg")) {
                alert("网络异常，请稍后重试");
                log.error("返回数据没有‘msg’字段")
            }
            $scope.BoardsAll = data.msg;
//            console.log($scope.BoardsAll, data.msg);
            $scope.$apply();
        }

    }, function () {
        alert("网络异常，请稍后重试");
        log.error("getBoardAll request error")
    })


    $scope.small_forum_show = function (small) {
//        console.log(small);
        if (angular.isUndefined(small) || small.length == 0)
            return false;

        return true;
    }

//    testPost();

}


function getBoardAll(arg_data, arg_callBack, arg_error) {

    $.sendRequest("GET", "../../python/Forum/BoardsAll", arg_data, arg_callBack, arg_error);
}

//function testPost() {
//
//    $.sendRequest("POST", "../../python/", {test: "test"}, function (data) {
//
//        console.log(data)
//
//    }, function () {
//
//    });
//}