app.directive('navbar', function(){
  // Runs during compile
  return {
    // name: '',
    // priority: 1,
    // terminal: true,
    // scope: {}, // {} = isolate, true = child, false/undefined = no change
    controller: function($scope, $element, SearchFactory, $state) {
        $scope.logo = '../assets/images/'+Math.floor(Math.random() * 31)+'.png';

        $scope.search = function() {
            if($scope.searchQuery !== '') {
                var query = $scope.searchQuery;
                SearchFactory.search(query).then(
                    function(data) {
                        $state.go('search-results', {"results": data.data.results, "query": query});
                    },
                    function(error) {
                        console.log(error)
                    }
                );
            }
        }
    },
    // require: 'ngModel', // Array = multiple requires, ? = optional, ^ = check parent elements
    restrict: 'E', // E = Element, A = Attribute, C = Class, M = Comment
    templateUrl: 'templates/navbar.html',
    // replace: true,
    // transclude: true,
    // compile: function(tElement, tAttrs, function transclude(function(scope, cloneLinkingFn){ return function linking(scope, elm, attrs){}})),
    link: function($scope, iElm, iAttrs, controller) {
      
    }
  };
});
