app.factory("peopleFactory", function($http, $q, HOST) {
  var factory = {};

  factory.getPeople= function() {
    return $http.get(HOST+"/api/people", {cache: true});
  };

  factory.getPersonDetail = function(id) {
    return $http.get(HOST+"/api/people/" + id, {cache: true});
  };

  return factory;
})