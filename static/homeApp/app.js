var app = angular.module('ngViewHomeApp', ['ngRoute']);


app.config(['$routeProvider', function ($routeProvider) {
    $routeProvider
        .when('/', {
            controller: 'RootCtrl',
            templateUrl: 'home.html'
        })
        .when('/cats', {
            controller: 'CatsCtrl',
            templateUrl: ''
        })
//        .otherwise({
//            redirectTo: '/'
//        });
}]);
