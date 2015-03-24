app.factory("charactersFactory", function($http, $q, HOST) {
  var factory = {};

  factory.getCharacters = function() {
    return $http.get(HOST+"/api/characters", {cache: true});
  };

  factory.getCharacterDetail = function(id) {
    return $http.get(HOST+"/api/characters/" + id, {cache: true});
  };

  return factory;
});