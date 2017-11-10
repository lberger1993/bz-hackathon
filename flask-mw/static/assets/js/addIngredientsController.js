angular.module('HelloWorldApp', [])
    .controller('HelloWorldController', ['$scope', '$http', function($scope, $http) {
        $scope.ingredients = [];
        $scope.newIngredient = "";
        $scope.foodList = "";
        $scope.query = "";

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
            $scope.ingredients.push(newIngredient);
            $scope.query = "";
        }
    }]);