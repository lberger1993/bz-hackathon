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
            $scope.Foodrecipes = response.data;
        }, function errorCallback(response) {
            //TODO add error processing
        });


}]);