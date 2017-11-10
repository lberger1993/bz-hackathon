angular.module('chooseRecipeApp', [])
   .controller('chooseRecipeController', function($scope) {



        $scope.image = [
         {imageName : 'spaghetti', imageSrc : '../assets/img/spaghetti-bolognese.jpeg' },
        {imageName : 'pasta', imageSrc : '../assets/img/pasta.jpeg' },


        ];


});