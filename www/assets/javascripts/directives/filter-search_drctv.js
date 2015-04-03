app.directive('filterSearch', function(){
  // Runs during compile
  return {
    scope: {
      model: '=',
      searchField: '@'
    },
    controller: function($scope, $element, $attrs, $transclude, $filter) {
      $scope.dupModel = $scope.model;

      $scope.searchFilter = function(text) {
        // zomg fkn hack i am so 1337
        var searchObj = {};
        searchObj[$scope.searchField] = text;
        
        $scope.model = $filter('filter')($scope.dupModel, searchObj);
      };
    },
    restrict: 'E', 
    templateUrl: 'templates/filter-search.html',
    link: function($scope, iElm, iAttrs, controller) {
      
    }
  };
});