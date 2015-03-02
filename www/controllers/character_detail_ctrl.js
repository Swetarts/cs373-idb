app.controller('CharacterDetailCtrl', function($scope, charactersFactory, $stateParams) {

  var promise = charactersFactory.getCharacterDetail($stateParams['id']);
  promise.then(function(data) {
    $scope.character = data;
  });
});