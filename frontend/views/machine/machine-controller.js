angular.module("turingMachine").controller("MachineController", function ($scope, MachineService) {

    $scope.execute = function(){
        MachineService.execute($scope.operation, $scope.operand1, $scope.operand2).then(function(response){
            $scope.response_data = response.data;
            var tape_p = document.getElementById("tape");
            tape_p.innerHTML = response.data.result_tape;
            $scope.tape = response.data.result_tape;
            console.log(tape_p.innerHTML);
            $scope.processTape(tape_p);
        });
    }

    $scope.processTape = function(tape_p){
        $scope.current_position = 0;
        $scope.current_state = '>';

//        $scope.response_data.operation_list.forEach(function(operation){

        for(var i = 0; i < $scope.response_data.operation_list.length; i++){
            var operation = $scope.response_data.operation_list[i];

            console.log($scope.current_position);
            $scope.tape = replaceAt($scope.tape, $scope.current_position, operation["symbol"]);
            $scope.current_state = operation["state"];
            if($scope.current_position < 0 && operation["position"] < 0){
                throw 'Position out of bounds';
            }
            $scope.current_position = $scope.current_position + operation["position"];

            console.log($scope.tape);

            $scope.tape.replace
            tape_p.innerHTML = $scope.tape;
            setTimeout(function(){}, 3000);
        };

        function replaceAt(string, index, replace) {
            return string.substring(0, index) + replace + string.substring(index + 1);
        }


    }

});