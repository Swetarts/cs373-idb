app.controller('CharactersCtrl', function($scope, characters, cfpLoadingBar) {

  $scope.characters = characters;

  // comment in to debug loading bar
  //cfpLoadingBar.start();
});
