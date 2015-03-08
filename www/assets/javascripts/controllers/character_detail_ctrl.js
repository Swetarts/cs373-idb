app.controller('CharacterDetailCtrl', function($scope, charactersFactory, $stateParams) {

  charactersFactory.getCharacterDetail($stateParams['id']).then(
    function(data){
      $scope.character = data.data;
    },
    function() {
      console.log("error retrieving character:", $stateParams['id']);
    }
  );

});