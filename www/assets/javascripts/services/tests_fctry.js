app.factory('TestsFactory', function(HOST, $http){
  var factory = {};

  factory.runTests = function() {
    return $http.get(HOST + "/api/tests");
  }

  return factory;
});