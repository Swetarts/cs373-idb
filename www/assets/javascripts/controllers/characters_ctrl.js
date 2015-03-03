app.controller('CharactersCtrl', function($scope, charactersFactory) {

  var promise = charactersFactory.getCharacters();
  promise.then(function(data) {
      $scope.characters = data;
    });
});