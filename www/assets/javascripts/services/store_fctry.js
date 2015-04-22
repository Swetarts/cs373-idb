app.factory('StoreFactory', function($http, HOST) {
  var factory = {};


  factory.getStores = function() {
    var stores = [11050, 3162, 10606];
    return $http.get(HOST + '/api/stores');
  }

  return factory;
})