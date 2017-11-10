angular.module('HelloWorldApp', [])
    .controller('HelloWorldController', ['$scope', '$http', function($scope, $http) {
        $scope.ingredients = [];
        $scope.newIngredient = "";
        $scope.foodList = "";
        //TODO remove this from HelloWorld to smth better

        //TODO move this somewhere:
        $scope.addIngredient = function() {
            $scope.ingredients.push($scope.newIngredient);

            $http({
                method: 'GET',
                url: '/api/v1/get_all_food'
            }).then(function successCallback(response) {
                $scope.foodList = response.data;
            }, function errorCallback(response) {
                // called asynchronously if an error occurs
                // or server returns response with an error status.
            });
        }
    }]);