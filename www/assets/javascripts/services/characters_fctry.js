app.factory("charactersFactory", function($http, $q) {
  var factory = {};

  factory.getCharacters = function() {
    return $http.get("http://localhost:5000/api/characters", {cache: true});
  };

  factory.getCharacterDetail = function(id) {
    return $http.get("http://localhost:5000/api/characters/" + id, {cache: true});
  };

  return factory;
});