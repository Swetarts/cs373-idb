app.factory('StoreFactory', function($http, HOST) {
  var factory = {};


  factory.getStores = function() {
    return $http.get(HOST + '/api/stores');
  }

  return factory;
})