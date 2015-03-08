app.controller('CharactersCtrl', function($scope, charactersFactory) {

  charactersFactory.getCharacters().then(
    function(data) {
      $scope.characters = data.data;
    },
    function() {
      console.log('error getting characters');
    }
  );

});
