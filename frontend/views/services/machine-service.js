angular.module("turingMachine").factory("MachineService", function($http, config) {


    var _testApi = function () {
        return $http.get(config.baseUrl + "/test");
    };

    var _execute = function(operation, operand1, operand2){
        return $http.get(config.baseUrl + "/execute", {
            params: {
                operation: operation,
                operand1: operand1,
                operand2: operand2
            }
        });
    }

    return {
        testApi    : _testApi,
        execute    : _execute
    }
});
