// Declare app level module which depends on views, and components
var app = angular.module('myApp', ['ui.router', 'ui.bootstrap', 'angular-loading-bar', 'ngAnimate'])

  .run(function($rootScope, $state) {
    $rootScope.$on('$stateChangeStart', function(e, to) {
      // console.log($state);
      // console.log(e);
      // console.log(to);
    });

    $rootScope.$on('$stateChangeSuccess', function() {
      $("html, body").animate({ scrollTop: 0 }, 200);
    });
  })

  // change if not on local development
  .constant('HOST', 'http://104.239.165.88:5000')

  .config(function($stateProvider, $urlRouterProvider, $locationProvider) {

    // Now set up the states
    $stateProvider
      .state('home', {
        url: "/home",
        templateUrl: "../../templates/home.html",
        controller: "HomeCtrl"
      })
      .state('about', {
        url: "/about",
        templateUrl: "../../templates/about.html",
        controller: "AboutCtrl"
      })
      .state('characters', {
        url: "/characters",
        templateUrl: "../../templates/characters.html",
        controller: "CharactersCtrl",
        resolve: {
          characters: function(charactersFactory, $q) {
            var deferred = $q.defer();

            charactersFactory.getCharacters().then(
              function(data) {
                deferred.resolve(data.data)
              }, function(error) {
                console.log("error getting characters", error);
              }
            );

            return deferred.promise;
          }
        }
      })
      .state('character-detail', {
        url: "/characters/:id",
        templateUrl: "../../templates/character-detail.html",
        controller: "CharacterDetailCtrl",
        resolve: {
          character: function(charactersFactory, $q, $stateParams) {
            var deferred = $q.defer();

            charactersFactory.getCharacterDetail($stateParams['id']).then(
              function(data) {
                deferred.resolve(data.data);
              }, function(error) {
                console.log("error getting character", error);
              }
            );

            return deferred.promise;
          }
        }
      })
      .state('people', {
        url: "/people",
        templateUrl: "../../templates/people.html",
        controller: "PeopleCtrl",
        resolve: {
          people: function(peopleFactory, $q) {
            var deferred = $q.defer();

            peopleFactory.getPeople().then(
              function(data) {
                deferred.resolve(data.data)
              }, function(error) {
                console.log("error getting people", error);
              }
            );

            return deferred.promise;
          }
        }
      })
      .state('person-detail', {
        url: "/people/:id",
        templateUrl: "../../templates/person-detail.html",
        controller: "PersonDetailCtrl",
        resolve: {
          person: function(peopleFactory, $q, $stateParams) {
            var deferred = $q.defer();

            peopleFactory.getPersonDetail($stateParams['id']).then(
              function(data) {
                deferred.resolve(data.data)
              }, function(error) {
                console.log("error getting people", error);
              }
            );

            return deferred.promise;
          }
        }
      })
      .state('issues', {
        url: "/issues",
        templateUrl: "../../templates/issues.html",
        controller: "IssuesCtrl",
        resolve: {
          issues: function(issuesFactory, $q, $stateParams) {
            var deferred = $q.defer();

            issuesFactory.getIssues().then(
              function(data) {
                deferred.resolve(data.data)
              }, function(error) {
                console.log("error getting issues", error);
              }
            );

            return deferred.promise;
          }
        }
      })
      .state('issue-detail', {
        url: "/issues/:id",
        templateUrl: "../../templates/issue-detail.html",
        controller: "IssueDetailCtrl",
        resolve: {
          issue: function(issuesFactory, $q, $stateParams) {
            var deferred = $q.defer();
            
            issuesFactory.getIssueDetail($stateParams['id']).then(
              function(data) {
                deferred.resolve(data.data)
              }, function(error) {
                console.log("error getting issues", error);
              }
            );

            return deferred.promise;
          }
        }
      });
      
    $urlRouterProvider.otherwise('/home');
    $locationProvider.html5Mode(true);
});

// set loading bar under navbar
app.config(['cfpLoadingBarProvider', function (cfpLoadingBarProvider) {
    cfpLoadingBarProvider.parentSelector = '#navbar';
    cfpLoadingBarProvider.includeSpinner = false;
}]);

