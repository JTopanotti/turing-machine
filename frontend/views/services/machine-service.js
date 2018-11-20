angular.module("turingMachine").factory("MachineService", function($http, config) {


    var _testApi = function () {
        return $http.get(config.baseUrl + "/test");
    };

    return {
        testApi    : _testApi
    }
});
