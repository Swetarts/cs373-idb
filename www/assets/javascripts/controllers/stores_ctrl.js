app.controller('StoresCtrl', function($scope, StoreFactory){
  $scope.showInfo = false;
  $scope.map = { 
    center: { 
      latitude: 30.3192393, 
      longitude: -97.7312059  
    }, 
    zoom: 8
  };

  $scope.open = function() {
    $scope.showInfo = true;
  }

  $scope.markers = [];
  StoreFactory.getStores().then(
    function(data) {
      $scope.markers.push(data.data.details);
      console.log(data);
    },
    function(err) {
      console.log("error getting stores", data);
    }
  );

  // $scope.markers = [
  //   {
  //     id: 1,
  //     coord: {
  //       latitude: 30.3192393, 
  //       longitude: -97.7312059,
  //     },
  //     address: '13321 Slow Poke Dr., Austin, Texas, aaaaaaaaaaaaaaaaaaa',
  //     name: 'Deez Nuts',
  //     phone_number: '5129999999',
  //     rating: '5',
  //     website: 'www.mynigga.com'
  //   }, 
  //   {
  //     id: 2,
  //     coord: {
  //       latitude: 30.2192393,
  //       longitude: -97.7312059,
  //     },
  //     address: '13321 Slow Poke Dr., Austin, Texas, aaaaaaaaaaaaaaaaaaa',
  //     name: 'Deez Nuts',
  //     phone_number: '5129999999',
  //     rating: '5',
  //     website: 'www.mynigga.com'

  //   }
  // ]

  // $scope.marker1 = {
  //     latitude: 30.3192393, 
  //     longitude: -97.7312059,
  //     data: 'Porn Store'
  //   } 
  $scope.marker2 = {
     latitude: 30.2192393, 
     longitude: -97.7312059
  }   
})