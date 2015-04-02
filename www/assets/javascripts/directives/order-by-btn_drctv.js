app.directive('orderBySearchUtil', function(){
  return {
    scope: {
      model: '=',
    }, 
    controller: function($scope, $element, $attrs, $transclude, $filter, $parse) {
      $scope.status = {
        isopen: false
      };

      $scope.toggleDropdown = function($event) {
        $event.preventDefault();
        $event.stopPropagation();
        $scope.status.isopen = !$scope.status.isopen;
      };
      
      console.log($attrs.searchField);
      $scope.dupModel = $scope.model;
      $scope.searchFilter = function(text) {
        // zomg fkn hack i am so 1337
        var searchObj = {};
        searchObj[$attrs.searchField] = text;
        $scope.model = $filter('filter')($scope.dupModel, searchObj);
      };

      var orderBy = $filter('orderBy');

      $scope.order = function(predicate, reverse) {
        $scope.model = orderBy($scope.model, predicate, reverse); 
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

    },
    restrict: 'E', // E = Element, A = Attribute, C = Class, M = Comment
    templateUrl: '../../../templates/order-by-btn.html',
    link: function($scope, iElm, iAttrs, controller) {
      
    }
  };
});