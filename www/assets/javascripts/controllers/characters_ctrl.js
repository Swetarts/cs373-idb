app.controller('CharactersCtrl', function($scope, characters, cfpLoadingBar, $filter) {

  $scope.characters = characters;

  // comment in to debug loading bar
  //cfpLoadingBar.start();

  $scope.status = {
    isopen: false
  };

  $scope.toggleDropdown = function($event) {
    $event.preventDefault();
    $event.stopPropagation();
    $scope.status.isopen = !$scope.status.isopen;
  };

  var orderBy = $filter('orderBy');

  $scope.order = function(predicate, reverse) {
    $scope.characters = orderBy($scope.characters, predicate, reverse); 
    updateOrderOpt(predicate, reverse); 
  };

  $scope.orderOpt = 'None';

  function updateOrderOpt(predicate, reverse) {
    if(predicate === 'id') {
      $scope.orderOpt = 'None';
    }
    else if(predicate === 'name' && reverse === false) {
      $scope.orderOpt = 'Name Ascending';
    }
    else if(predicate === 'name' && reverse === true) {
      $scope.orderOpt = 'Name Descending';
    }
    else {
      $scope.orderOpt = '';
    }
  }


});
