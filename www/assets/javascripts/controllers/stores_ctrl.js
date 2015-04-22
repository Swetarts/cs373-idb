app.controller('StoresCtrl', function($scope, StoreFactory){
  $scope.showInfo = false;
  $scope.map = { 
    center: { 
      latitude: 30.3192393, 
      longitude: -97.7312059  
    }, 
    zoom: 10 
  };

  $scope.open = function() {
    $scope.showInfo = true;
  }

  StoreFactory.getStores().then(
    function(data) {
      $scope.places = data.data;
      console.log(data);
    },
    function(err) {
      console.log("error getting stores", data);
    }
  );

})