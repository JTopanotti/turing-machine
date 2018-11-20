angular.module("turingMachine").config(function ($routeProvider) {

    //index
    $routeProvider.when("/", {
        templateUrl: "views/machine/machine.html",
        controller: "MachineController",
        resolve: {}
    });
    $routeProvider.otherwise({ redirectTo: "/"})

});