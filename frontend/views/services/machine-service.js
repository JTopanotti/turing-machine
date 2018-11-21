angular.module("turingMachine").factory("MachineService", function($http, config) {


    var _testApi = function () {
        return $http.get(config.baseUrl + "/test");
    };

    var _execute = function(operation, input){
        return $http.get(config.baseUrl + "/execute", {
            params: {
                operation: operation,
                input: input
            }
        });
    }

    return {
        testApi    : _testApi,
        execute    : _execute
    }
});
