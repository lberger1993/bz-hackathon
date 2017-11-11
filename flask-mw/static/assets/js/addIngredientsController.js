angular.module('HelloWorldApp', [])
    .controller('HelloWorldController', ['$scope', '$http', function($scope, $http) {
        $scope.ingredients = [];
        $scope.newIngredient = "";
        $scope.query = "";
        $scope.waterAmount = 0.0;

        $http({
            method: 'GET',
            url: '/api/v1/get_all_food'
        }).then(function successCallback(response) {
            $scope.savedIngredients = response.data;
        }, function errorCallback(response) {
            //TODO add error processing
        });



        //TODO remove this from HelloWorld to smth better

        //TODO move this somewhere:
        $scope.addIngredient = function(newIngredient) {
            //TODO replace with real amount
            newIngredient.waterAmount = 1000;
            $scope.ingredients.push(newIngredient);
            $scope.query = "";
            $scope.waterAmount += newIngredient.WaterCost * newIngredient.waterAmount / 1000.0;
        }
    }]);