angular.module('HelloWorldApp', [])
    .controller('HelloWorldController', function($scope) {
        $scope.ingredients = [];
        $scope.newIngredient = "";

        $scope.addIngredient = function() {
            $scope.ingredients.push($scope.newIngredient);
        }
    });