app.factory("issuesFactory", function($http, $q, HOST) {
  var factory = {};

  factory.getIssues = function() {
    return $http.get(HOST+"/api/issues", {cache: true});
  };

  factory.getIssueDetail = function(id) {
    return $http.get(HOST+"/api/issues/" + id, {cache: true});
  };

  return factory;
});