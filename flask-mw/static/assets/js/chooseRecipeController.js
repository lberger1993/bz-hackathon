angular.module('chooseRecipeApp', [])
   .controller('chooseRecipeController',['$http','$scope', function($http,$scope) {
        $scope.image = [
         {imageName : 'spaghetti', imageSrc : '../assets/img/spaghetti-bolognese.jpeg' },
        {imageName : 'pasta', imageSrc : '../assets/img/pasta.jpeg' },
        ];
        console.log('and error here?');

       $scope.checkValue ="hi";

        $http({
            method: 'GET',
            url: '/api/v1/get_all_recipes'
        }).then(function successCallback(response) {
            console.log(response)
            $scope.Foodrecipes = response.data;
        }, function errorCallback(response) {
            //TODO add error processing
        });
           $scope.selected_recipe = 'pizza';
           $scope.optimizeOption = function(){

           };

           $scope.optimal= false;

           $scope.optimize = function () {

               optimal = true;
               matrix = [{ProductName: 'Beef', OptimizedProductName: 'Mushroom', WaterPerKilo: 150, AmountInRecipe : 0.5}];



           }
/* $scope.matrix;
          $http({
           method: 'GET',
           url: '/api/v1/get_recipe_partners'
       }).then(function successCallback(response) {
            $scope.matrix = response.data;

       }, function errorCallback(response) {
           //TODO add error processing
       });
          $scope.selected_recipe = 'pizza';
          $scope.optimizeOption = function(recipe_id){
          for (var row in $scope.matrix){
                  $scope.matrix[row]['id']
                  if ($scope.matrix[row]['id'] == recipe_id){
                       var optimized_recipeID = $scope.matrix[row]['good_recipe']
                       for (var option in $scope.Foodrecipes){
                           if (optimized_recipeID == $scope.Foodrecipes[option]['RecipeID'])
                               $scope.best_option =$scope.Foodrecipes[option];
                               console.log('my best choice', $scope.best_option);
                           }
                       }
               }
          }*/


}]);