angular.module('HelloWorldApp', [])
    .controller('AddIngredientsController', ['$scope', '$http', function($scope, $http) {
        $scope.ingredients = [];
        $scope.newIngredient = "";
        $scope.query = "";
        $scope.currentAmount = 1000;
        $scope.waterAmount = 0;

        $http({
            method: 'GET',
            url: '/api/v1/get_all_food'
        }).then(function successCallback(response) {
            $scope.savedIngredients = response.data;
        }, function errorCallback(response) {
            //TODO add error processing
        });

        var removeItemFromArray = function(array, item){
            var tmp = [];
            for(var index in array){
                if(array[index].ProductName != item.ProductName){
                    tmp.push(array[index]);
                }
            }
            return tmp;
        };


        //TODO remove this from HelloWorld to smth better

        $scope.addIngredient = function(newIngredient) {
            $scope.savedIngredients = removeItemFromArray($scope.savedIngredients, newIngredient);
            $scope.ingredients.push(newIngredient);
            newIngredient.amount = 1000;
            $scope.query = "";
            $scope.updateTotalAmount();
        };

        $scope.onLoseFocus = function() {
            $scope.currentAmount = 1000;
            $scope.updateTotalAmount();
        };

        $scope.updateTotalAmount = function() {
            $scope.waterAmount = 0.0;
            $scope.ingredients.forEach(function(ingredient) {
                $scope.waterAmount += ingredient.WaterCost * ingredient.amount / 1000.0;
            });
            $scope.waterAmount = Math.floor( $scope.waterAmount );
        };
    }]);