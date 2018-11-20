angular.module("turingMachine").controller("MachineController", function ($scope, MachineService) {

    $scope.machine = "cyka";
    MachineService.testApi().then();

});