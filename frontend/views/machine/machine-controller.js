angular.module("turingMachine").controller("MachineController", function ($scope, MachineService) {

    $scope.stop = false;
    $scope.current_position = 0;
    $scope.current_state = '>';

    $scope.execute = function(){
        MachineService.execute($scope.operation, $scope.input).then(function(response){
            $scope.response_data = response.data;
            var tape_p = document.getElementById("tape");
            tape_p.innerHTML = response.data.result_tape;
            $scope.tape = response.data.result_tape;
            $scope.processTape(tape_p);
        });
    }

    $scope.reset = function(){
        location.reload();
    }

    $scope.processTape = function(tape_p){
        $scope.current_position = 0;
        $scope.current_state = '>';
        $scope.operation_list_index = 0;

        var processingInterval = setInterval(executeOperation, $scope.velocity);

        function executeOperation(operation){

                if($scope.stop || $scope.operation_list_index
                    == $scope.response_data.operation_list.length){
                    clearInterval(processingInterval);
                    $scope.stop = false;
                    $scope.tape = clean($scope.tape);
                    tape_p.innerHTML = $scope.tape;
                }

                var operation = $scope.response_data.operation_list[$scope.operation_list_index];

                if(operation != null){
                    $scope.tape = replaceAt($scope.tape, $scope.current_position, operation["symbol"]);
                    if($scope.current_position < 0 && operation["position"] < 0){
                        throw 'Position out of bounds';
                    }
                    $scope.current_position = $scope.current_position + operation["position"];
                    $scope.current_state = operation["state"];
                    tape_p.innerHTML = $scope.tape;

                    $scope.operation_list_index += 1;
                }
        }

        function replaceAt(string, index, replace) {
            return string.substring(0, index) + replace + string.substring(index + 1);
        }

        function clean(stringToTrim) {
            var return_string = stringToTrim;
            return_string = return_string.replace(/^B+/, "");
            return_string = return_string.replace(/B/g, " ");
            return return_string;
        }


    }

});