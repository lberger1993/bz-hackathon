angular.module('chooseRecipeApp', [])
   .controller('chooseRecipeController',['$http','$scope', function($http,$scope) {
        $scope.image = [
         {imageName : 'spaghetti', imageSrc : '../assets/img/spaghetti-bolognese.jpeg' },
        {imageName : 'pasta', imageSrc : '../assets/img/pasta.jpeg' },
        ];

        $http({
           method: 'GET',
           url: '/api/v1/get_all_recipes'
       }).then(function successCallback(response) {
           console.log(response.data)
           $scope.Foodrecipes = response.data;
       }, function errorCallback(response) {
           //TODO add error processing
       });
       $scope.optomize = function(recipe_id){
        $scope.alternatives = [];
        $scope.alternatives_rendered = false;
        for (var element in $scope.Foodrecipes ){
            if ($scope.Foodrecipes[element]['RecipeID'] == recipe_id){
                for (var val in $scope.Foodrecipes[element]['FoodItems']){
                    console.log($scope.Foodrecipes[element]['FoodItems'][val]['FoodIemID']);
                    $scope.alternatives_rendered = true;
                    $scope.alternatives.push({'id': $scope.Foodrecipes[element]['FoodItems'][val]['FoodIemID'], 'alternates': $scope.Foodrecipes[element]['FoodItems'][val]['Alternative'], 'water_scores': $scope.Foodrecipes[element]['FoodItems'][val]['AlternativeAmountInRecipe']});
                    //$scope.alternatives.push({'water_scores': $scope.Foodrecipes[element]['FoodItems'][val]['AlternativeAmountInRecipe']})
                }

            }
        }

       }

}]);
