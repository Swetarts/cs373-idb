app.controller('StoresCtrl', function($scope, StoreFactory, places){
  
var styles=[{"featureType":"all","elementType":"geometry.fill","stylers":[{"visibility":"on"}]},{"featureType":"all","elementType":"labels.text.fill","stylers":[{"saturation":36},{"color":"#817a9c"},{"lightness":40}]},{"featureType":"all","elementType":"labels.text.stroke","stylers":[{"visibility":"on"},{"color":"#000000"},{"lightness":16}]},{"featureType":"all","elementType":"labels.icon","stylers":[{"visibility":"off"}]},{"featureType":"administrative","elementType":"geometry.fill","stylers":[{"color":"#000000"},{"lightness":20}]},{"featureType":"administrative","elementType":"geometry.stroke","stylers":[{"color":"#000000"},{"lightness":17},{"weight":1.2}]},{"featureType":"administrative","elementType":"labels.icon","stylers":[{"visibility":"simplified"},{"hue":"#ff0000"}]},{"featureType":"administrative.country","elementType":"all","stylers":[{"visibility":"simplified"},{"hue":"#ff0000"}]},{"featureType":"administrative.land_parcel","elementType":"geometry.fill","stylers":[{"color":"#558684"}]},{"featureType":"administrative.land_parcel","elementType":"geometry.stroke","stylers":[{"gamma":"1.20"},{"lightness":"4"}]},{"featureType":"landscape","elementType":"geometry","stylers":[{"color":"#000000"},{"lightness":20}]},{"featureType":"landscape.man_made","elementType":"geometry.fill","stylers":[{"gamma":"1.49"},{"color":"#444f67"}]},{"featureType":"landscape.man_made","elementType":"geometry.stroke","stylers":[{"gamma":"0.00"},{"lightness":"-100"},{"saturation":"-26"},{"weight":"0.01"}]},{"featureType":"landscape.natural.landcover","elementType":"geometry.fill","stylers":[{"color":"#558684"}]},{"featureType":"poi","elementType":"geometry","stylers":[{"color":"#000000"},{"lightness":21}]},{"featureType":"poi.park","elementType":"geometry.fill","stylers":[{"color":"#558684"}]},{"featureType":"poi.place_of_worship","elementType":"geometry.fill","stylers":[{"hue":"#ff0000"},{"visibility":"simplified"}]},{"featureType":"road","elementType":"geometry","stylers":[{"weight":"1.39"},{"gamma":"1.49"},{"lightness":"-34"},{"color":"#374054"}]},{"featureType":"road","elementType":"geometry.fill","stylers":[{"color":"#374054"}]},{"featureType":"road","elementType":"geometry.stroke","stylers":[{"color":"#374054"}]},{"featureType":"road","elementType":"labels.text.fill","stylers":[{"color":"#666987"}]},{"featureType":"road.highway","elementType":"geometry.fill","stylers":[{"color":"#000000"},{"lightness":17}]},{"featureType":"road.highway","elementType":"geometry.stroke","stylers":[{"color":"#000000"},{"lightness":29},{"weight":0.2}]},{"featureType":"road.highway.controlled_access","elementType":"geometry.fill","stylers":[{"visibility":"simplified"},{"hue":"#ff0000"}]},{"featureType":"road.arterial","elementType":"geometry","stylers":[{"color":"#000000"},{"lightness":18}]},{"featureType":"road.local","elementType":"geometry","stylers":[{"color":"#000000"},{"lightness":16}]},{"featureType":"transit","elementType":"geometry","stylers":[{"color":"#000000"},{"lightness":19}]},{"featureType":"water","elementType":"geometry","stylers":[{"color":"#444f67"},{"lightness":17}]}]

var mapOptions = {
  	styles: styles
  };

  var stores = [];

  angular.forEach(places, function(value, place){
   var address = value.details.address;
   var addressParts = address.split(",");

   var store = {
    id : value.details.place_id,
    location: value.details.location,
    name: value.details.name,
    address: addressParts[0],
    city: addressParts[1],
    state_zip: addressParts[2],
    country: addressParts[3],
    web: value.details.website, 
    phone: value.details.phone_number,
    rating: value.details.rating
   };

   this.push(store);

  }, stores);

  var moreLocations = [
    {
      id: "99",
      location: {latitude: 30.357971,
                  longitude: -97.732446},
      name: "Dragon's Lair Comics & Fantasy Austin",
      address: "2438 W Anderson Ln B1",
      city: "Austin",
      state_zip: "TX 78757",
      country: "United States",
      web: "http://dlair.net",
      phone: "(512)454-2399",
      rating: "4.7"
    },
    {
      id: "100",
      location: {latitude: 30.175869,
                  longitude: -97.826313},
      name: "Junior Comics",
      address: "2110 W Slaughter Ln #147",
      city: "Austin",
      state_zip: "TX 78748",
      country: "United States",
      web: "http://www.juniorscomics.com",
      phone: "(512)282-1302",
      rating: "3.5"
    },

  ];
  stores.push(moreLocations[0]);
  stores.push(moreLocations[1]);

  // $scope.activeMarker = null;

  $scope.places = stores;
  // $scope.show = false;

  $scope.map = { 
    center: { 
      latitude: 30.3192393, 
      longitude: -97.7312059  
    }, 
    zoom: 10,
    options: mapOptions
  };

   // $scope.markerEvents = {
   //      events: {
   //        click: function(marker) {
   //          if($scope.activeMarker){
   //            closeActiveMarker();
            
   //          }
   //          $scope.activeMarker = marker;
   //        }
   //      }
   //    };

   //    function closeActiveMarker(){
   //      $scope.activeMarker.showWindow = false;
   //    };

// /*
//  * The google.maps.event.addListener() event waits for
//  * the creation of the infowindow HTML structure 'domready'
//  * and before the opening of the infowindow defined styles
//  * are applied.
//  */
// google.maps.event.addListener(infowindow, 'domready', function() {

//    // Reference to the DIV which receives the contents of the infowindow using jQuery
//    var iwOuter = $('.gm-style-iw');

//     // The DIV we want to change is above the .gm-style-iw DIV.
//     // * So, we use jQuery and create a iwBackground variable,
//     // * and took advantage of the existing reference to .gm-style-iw for the previous DIV with .prev().
    
//    var iwBackground = iwOuter.prev();

//    // Remove the background shadow DIV
//    iwBackground.children(':nth-child(2)').css({'display' : 'none'});

//    // Remove the white background DIV
//    iwBackground.children(':nth-child(4)').css({'display' : 'none'});

// });

})