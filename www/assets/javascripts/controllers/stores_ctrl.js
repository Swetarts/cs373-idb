app.controller('StoresCtrl', function($scope, StoreFactory, places){
  
  $scope.places = places;

  $scope.map = { 
    center: { 
      latitude: 30.3192393, 
      longitude: -97.7312059  
    }, 
    zoom: 10 
  };

})