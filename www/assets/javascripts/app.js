// Declare app level module which depends on views, and components
var app = angular.module('myApp', ['ui.router', 'ui.bootstrap'])

  .run(function($rootScope, $state) {
    $rootScope.$on('$stateChangeStart', function(e, to) {
      // console.log($state);
      // console.log(e);
      // console.log(to);
    });
  })

  .config(function($stateProvider, $urlRouterProvider, $locationProvider) {

    // Now set up the states
    $stateProvider
      .state('home', {
        url: "/home",
        templateUrl: "../../templates/home.html"
      })
      .state('about', {
        url: "/about",
        templateUrl: "../../templates/about.html"
      })
      .state('characters', {
        url: "/characters",
        templateUrl: "../../templates/characters.html",
        controller: "CharactersCtrl",
        resolve: {
          characters: function(charactersFactory, $q) {
            var deferred = $q.defer();

            charactersFactory.getCharacters()
              .then(function(data) {
                deferred.resolve(data.data)
              });

            return deferred.promise;
          }
        }
      })
      .state('character-detail', {
        url: "/characters/:id",
        templateUrl: "../../templates/character-detail.html",
        controller: "CharacterDetailCtrl"
      });

    $urlRouterProvider.otherwise('/home');
    $locationProvider.html5Mode(true);
});
