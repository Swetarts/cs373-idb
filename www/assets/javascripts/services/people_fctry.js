app.factory("peopleFactory", function($http, $q) {
  var factory = {};

  factory.getPeople= function() {
    return $http.get("http://localhost:5000/api/people", {cache: true});
  };

  factory.getPersonDetail = function(id) {
    return $http.get("http://localhost:5000/api/people/" + id, {cache: true});
  };

  return factory;
})