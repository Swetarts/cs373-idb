app.controller('HomeCtrl', function($scope, SearchFactory, $state) {

	$scope.video = '../assets/videos/bgvideo'+Math.floor(Math.random() * 8)+'.mp4';

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
});
