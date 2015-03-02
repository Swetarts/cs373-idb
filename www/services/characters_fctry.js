app.factory("charactersFactory", function($http, $q) {
  var factory = {};

  factory.getCharacters = function() {
    var deffered = $q.defer();

    $http.get("http://localhost:5000/characters", {cache: true})
      .success(function(data) {
        console.log(data);
        deffered.resolve(data);
      })
      .error(function() {
        console.log("error getting characters");
        deffered.reject([{'name':'error'}]);
      });

    return deffered.promise;
  };

  factory.getCharacterDetail = function(id) {
    var deffered = $q.defer();

    $http.get("http://localhost:5000/characters/" + id, {cache: true})
      .success(function(data) {
        console.log(data);
        deffered.resolve(data);
      })
      .error(function(data) {
        console.log("error getting character:" + id);
      });

    return deffered.promise
  };

  return factory;
});