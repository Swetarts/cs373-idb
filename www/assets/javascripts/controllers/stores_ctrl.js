app.controller('StoresCtrl', function($scope, StoreFactory, places){
  
var styles=[{"featureType":"all","elementType":"geometry.fill","stylers":[{"visibility":"on"}]},{"featureType":"all","elementType":"labels.text.fill","stylers":[{"saturation":36},{"color":"#817a9c"},{"lightness":40}]},{"featureType":"all","elementType":"labels.text.stroke","stylers":[{"visibility":"on"},{"color":"#000000"},{"lightness":16}]},{"featureType":"all","elementType":"labels.icon","stylers":[{"visibility":"off"}]},{"featureType":"administrative","elementType":"geometry.fill","stylers":[{"color":"#000000"},{"lightness":20}]},{"featureType":"administrative","elementType":"geometry.stroke","stylers":[{"color":"#000000"},{"lightness":17},{"weight":1.2}]},{"featureType":"administrative","elementType":"labels.icon","stylers":[{"visibility":"simplified"},{"hue":"#ff0000"}]},{"featureType":"administrative.country","elementType":"all","stylers":[{"visibility":"simplified"},{"hue":"#ff0000"}]},{"featureType":"administrative.land_parcel","elementType":"geometry.fill","stylers":[{"color":"#558684"}]},{"featureType":"administrative.land_parcel","elementType":"geometry.stroke","stylers":[{"gamma":"1.20"},{"lightness":"4"}]},{"featureType":"landscape","elementType":"geometry","stylers":[{"color":"#000000"},{"lightness":20}]},{"featureType":"landscape.man_made","elementType":"geometry.fill","stylers":[{"gamma":"1.49"},{"color":"#444f67"}]},{"featureType":"landscape.man_made","elementType":"geometry.stroke","stylers":[{"gamma":"0.00"},{"lightness":"-100"},{"saturation":"-26"},{"weight":"0.01"}]},{"featureType":"landscape.natural.landcover","elementType":"geometry.fill","stylers":[{"color":"#558684"}]},{"featureType":"poi","elementType":"geometry","stylers":[{"color":"#000000"},{"lightness":21}]},{"featureType":"poi.park","elementType":"geometry.fill","stylers":[{"color":"#558684"}]},{"featureType":"poi.place_of_worship","elementType":"geometry.fill","stylers":[{"hue":"#ff0000"},{"visibility":"simplified"}]},{"featureType":"road","elementType":"geometry","stylers":[{"weight":"1.39"},{"gamma":"1.49"},{"lightness":"-34"},{"color":"#374054"}]},{"featureType":"road","elementType":"geometry.fill","stylers":[{"color":"#374054"}]},{"featureType":"road","elementType":"geometry.stroke","stylers":[{"color":"#374054"}]},{"featureType":"road","elementType":"labels.text.fill","stylers":[{"color":"#666987"}]},{"featureType":"road.highway","elementType":"geometry.fill","stylers":[{"color":"#000000"},{"lightness":17}]},{"featureType":"road.highway","elementType":"geometry.stroke","stylers":[{"color":"#000000"},{"lightness":29},{"weight":0.2}]},{"featureType":"road.highway.controlled_access","elementType":"geometry.fill","stylers":[{"visibility":"simplified"},{"hue":"#ff0000"}]},{"featureType":"road.arterial","elementType":"geometry","stylers":[{"color":"#000000"},{"lightness":18}]},{"featureType":"road.local","elementType":"geometry","stylers":[{"color":"#000000"},{"lightness":16}]},{"featureType":"transit","elementType":"geometry","stylers":[{"color":"#000000"},{"lightness":19}]},{"featureType":"water","elementType":"geometry","stylers":[{"color":"#444f67"},{"lightness":17}]}]

var mapOptions = {
  	styles: styles
  };

  $scope.places = places;

  $scope.map = { 
    center: { 
      latitude: 30.3192393, 
      longitude: -97.7312059  
    }, 
    zoom: 10,
    options: mapOptions
  };

})