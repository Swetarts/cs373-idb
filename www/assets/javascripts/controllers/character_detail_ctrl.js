app.controller('CharacterDetailCtrl', function($scope, character) {

  $scope.imageIsCollapsed = true;
  $scope.friendsIsCollapsed = true;
  $scope.enemiesIsCollapsed = true;

  $scope.character = character;

});