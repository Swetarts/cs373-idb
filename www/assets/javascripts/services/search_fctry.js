app.factory('SearchFactory', function($http, HOST){
  var factory = {};

  factory.search = function(query) {
    return $http.get(HOST + '/api/search?query=' + query);
  };

  return factory; 
})