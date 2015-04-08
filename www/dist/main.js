// Declare app level module which depends on views, and components
var app = angular.module('myApp', ['ui.router', 'ui.bootstrap', 'angular-loading-bar', 'ngAnimate'])

  .run(function($rootScope, $state) {
    $rootScope.$on('$stateChangeStart', function(e, to) {
      // console.log($state);
      // console.log(e);
      // console.log(to);
    });

    // Moves screen to top after state change
    $rootScope.$on('$stateChangeSuccess', function() {
      $("html, body").animate({ scrollTop: 0 }, 200);
    });

    var slap = new Audio("assets/sounds/slap.mp3");
    $("a").on('click', function() {
      slap.play();
    });
  })

  // change if not on local development
  .constant('HOST', 'http://localhost:5000')

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
      .state('unitTests', {
        url: "/unitTests",
        templateUrl: "../../templates/unitTests.html",
        controller: "UnitTestsCtrl"
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


app.controller('AboutCtrl', function($scope) {

	$scope.members = [
		{
			"name":"Sean Villars",
			"image":"http://i.imgur.com/uYwLx6k.jpg?1",
			"description":"I am a senior about to graduate in May of this year. I like skateboarding, programming, good beer, and kickin it with my bros. After I graduate I am going to start working as a Front End Engineer for Turnitin here in Austin.",
			"responsibilites":"I was responsible for the front end portion of our application. I set up Angular and programmed the characters, people, and issues poritons of our site along with the details pages for each of those. I also worked with Jerry to help get his feet wet in Angular where he successfully coded up the home and about pages.",
			"num_commits":"71",
			"num_issues":"15",
			"num_uTests":"3"
		},
		{
			"name":"Maximilian Brown",
			"image":"http://i.imgur.com/Ap2J5QI.jpg?1",
			"description":"Max is a Computer Science major at the University of Texas at Austin. He is married and has two children. When he isn't at work or school, he enjoys spending time with his family. Max recently started collecting comic books with his son and when they have time, Max and his son like to look for 'bad guys'.",
			"responsibilites":"Developed the data model/ UML diagram for the database utilizing navicat data modeler. Created python scripts to automate parsing of comicvine API data and populating our server hosted database. Worked with flask models to ensure compatibility with acutal data.",
			"num_commits":"20",
			"num_issues":"3",
			"num_uTests":"3"
		},
		{
			"name":"Gerardo Gamboa",
			"image":"http://i.imgur.com/vxbT1QN.jpg?1",
			"description":"When I’m not fighting crime and I almost never am, I’m studying at the GDC. This is my last semester studying Computer Science before I graduate with a BS and INFOSEC certificate. After graduation I hope to have more time to fight crime and save the city as well as working at AlienVault as a full time Software Engineer/superhero. My superhero origin story began in El Paso, TX until I moved to Austin, TX in 2009 to begin my studies and fight crime. Criminals beware!!!",
			"responsibilites":"My responsibilities included started my training in Angular in the front end aspect of the project. I worked with Sean to start practicing Angular and helped out with some things that later became making the home page and about page. Definitely feel a lot better with Angular than when I first started working on this project.",
			"num_commits":"14",
			"num_issues":"2",
			"num_uTests":"3"
		},
		{
			"name":"Aaron Dishman",
			"image":"http://i.imgur.com/9RzkScR.png?1",
			"description":"Dude's been crushing code for ~3 years, mostly in Java and C, but is up and coming in the Python game. His superpowers include the ability to transform any app into Mobile via Android Studio instantly. Once complete, you know the app is stable because he's mastered the skills of automated tests via Calabash. First appeared in UTCS in 2012, and will make the 'real world' debut this summer, May 2015!! POW! BAMM!",
			"responsibilites":"apiary design and edit, wiki/technical report write up, db population dev, db design, cat coralling",
			"num_commits":"17",
			"num_issues":"5",
			"num_uTests":"3"
		},
		{
			"name":"Tyler Corley",
			"image":"http://i.imgur.com/dLRQOmC.jpg?1",
			"description":"I'm a senior at the Univerity of Texas with humble beginnings from the small town of Longview, TX. I graduate in May with a job lined up at eBay in San Jose, CA. I enjoy programming, making music in and outside school, and occasionally finding ways to use emojis in my commit messages 💁.",
			"responsibilites":"Backend Bistro (Set up API calls to deliver serialized models), Fullmodel SQLAlchemist (Set up Flask models with SQLAlchemy and database migrations), Apiary Expert (Wrote out the API on Apiary.io), Defender of the SWErver (Set up the Rackspace instance and delegated SSH Authentication), and the One Who Dropped the [data]Base (Configured the PostgreSQL database users and mirrored the schema onto tables).",
			"num_commits":"7",
			"num_issues":"20",
			"num_uTests":"3"
		},
		{
			"name":"Alex Fortin",
			"image":"http://i.imgur.com/0IMTMLW.jpg?1",
			"description":"I enjoy playing soccer and drinking, preferably at the same time. Currently a senior studying brogramming at the University of America. Starting in the summer I will embark on a journey that is software engineering at Blackbaud.",
			"responsibilites":"Major responsibilities were setting up the database with the one and only Maximilian and populating it. This consisted of figuring out what attributes were needed, the relationships between attributes, and ultimately creating the schema's.",
			"num_commits":"25",
			"num_issues":"2",
			"num_uTests":"3"
		}
	]
});






app.controller('CharacterDetailCtrl', function($scope, character) {

  $scope.imageIsCollapsed = true;
  $scope.friendsIsCollapsed = true;
  $scope.enemiesIsCollapsed = true;

  $scope.character = character;

});
app.controller('CharactersCtrl', function($scope, characters, cfpLoadingBar, $filter) {

  $scope.characters = characters;
  
  // comment in to debug loading bar
  //cfpLoadingBar.start();
});

app.controller('HomeCtrl', function($scope) {

	$scope.myInterval = 4000;

	$scope.slides = [
		{
			"image":"http://www.fantastic-four.nl/marvel-superheroes-website-marvel-now.jpg"
		},
		{
			"image":"http://www.bu.edu/today/files/2013/07/t_4740907330_d101750ba5_o.jpg"
		},
		{
			"image":"http://media.ignimgs.com/media/ign/imgs/minisites/topN/comic-book-heroes/top100_comic_heroes_cover.jpg"
		},
		{
			"image":"http://uploads.neatorama.com/images/posts/177/57/57177/1357476489-0.jpg"
		}
	]

	
  
});

app.controller('IssueDetailCtrl', function($scope, issue){

  // $scope.imageIsCollapsed = false;

  $scope.issue = issue;
  
});
app.controller('IssuesCtrl', function($scope, issues){

  $scope.issues = issues;
  
});
app.controller('PeopleCtrl', function($scope, people) {

  $scope.people = people;
});

app.controller('PersonDetailCtrl', function($scope, person) {

  $scope.imageIsCollapsed = true;

  $scope.person = person;
});
app.controller('UnitTestsCtrl', function($scope, TestsFactory) {

  $scope.testResults = [];

  $scope.isProcessing = false;

  $scope.runTests = function() {
    console.log("running tests");
    $scope.isProcessing = true;

    TestsFactory.runTests().then(
      function(response) {
        console.log("Test success:", response.data);
        $scope.testResults.push(response.data);
        console.log("Results arr:", $scope.testResults);
      },
      function(error) {
        console.log("error running tests")
      }
    ).finally(function() {
      $scope.isProcessing = false;
    });
  }

});
app.directive('filterSearch', function(){
  // Runs during compile
  return {
    scope: {
      model: '=',
      searchField: '@'
    },
    controller: function($scope, $element, $attrs, $transclude, $filter) {
      $scope.dupModel = $scope.model;

      $scope.searchFilter = function(text) {
        // zomg fkn hack i am so 1337
        var searchObj = {};
        searchObj[$scope.searchField] = text;
        
        $scope.model = $filter('filter')($scope.dupModel, searchObj);
      };
    },
    restrict: 'E', 
    templateUrl: 'templates/filter-search.html',
    link: function($scope, iElm, iAttrs, controller) {
      
    }
  };
});
app.directive('navbar', function(){
  // Runs during compile
  return {
    // name: '',
    // priority: 1,
    // terminal: true,
    // scope: {}, // {} = isolate, true = child, false/undefined = no change
    controller: function($scope, $element, $attrs, $transclude) {
        $scope.logo = '../assets/images/'+Math.floor(Math.random() * 31)+'.png';
    },
    // require: 'ngModel', // Array = multiple requires, ? = optional, ^ = check parent elements
    restrict: 'E', // E = Element, A = Attribute, C = Class, M = Comment
    templateUrl: 'templates/navbar.html',
    // replace: true,
    // transclude: true,
    // compile: function(tElement, tAttrs, function transclude(function(scope, cloneLinkingFn){ return function linking(scope, elm, attrs){}})),
    link: function($scope, iElm, iAttrs, controller) {
      
    }
  };
});

app.directive('orderByBtn', function(){
  return {
    scope: {
      model: '=',
    }, 
    controller: function($scope, $element, $attrs, $transclude, $filter) {
      $scope.status = {
        isopen: false
      };

      $scope.toggleDropdown = function($event) {
        $event.preventDefault();
        $event.stopPropagation();
        $scope.status.isopen = !$scope.status.isopen;
      };
      
      var orderBy = $filter('orderBy');

      $scope.order = function(predicate, reverse) {
        $scope.model = orderBy($scope.model, predicate, reverse); 
        updateOrderOpt(predicate, reverse); 
      };

      $scope.orderOpt = 'None';

      function updateOrderOpt(predicate, reverse) {
        if(predicate === 'id') {
          $scope.orderOpt = 'None';
        }
        else if(predicate === 'name' && reverse === false) {
          $scope.orderOpt = 'Name Ascending';
        }
        else if(predicate === 'name' && reverse === true) {
          $scope.orderOpt = 'Name Descending';
        }
        else {
          $scope.orderOpt = '';
        }
      }

    },
    restrict: 'E', // E = Element, A = Attribute, C = Class, M = Comment
    templateUrl: '../../../templates/order-by-btn.html',
    link: function($scope, iElm, iAttrs, controller) {
      
    }
  };
});
app.directive('thumbnailSummary', function(){
  return {
    scope: {
      collection: '=',
      type: '@'
    },
    restrict: 'E', 
    templateUrl: 'templates/thumbnail-summary.html'
  }
});
app.directive('thumbnail', function() {
  return {
    replace: true,
    scope: {
      model: '=',
      type: '@'
    },
    templateUrl: '../../../templates/thumbnail.html',
    link: function(scope, element, attributes) {
      $(element).hover(
        function() {
          $('#banner-image').attr('src', scope.model.image.small_url);
        }
      );
    }
  }
});

app.filter('strip_anchors', function(){
    return function(text) {
      return text.replace(/<\/?a[^>]*>/g, "");
    };
});


app.filter('to_trusted', function($sce){
    return function(text) {
      return $sce.trustAsHtml(text);
    };
});
(function titleScroller(text) {
    document.title = text;
    setTimeout(function () {
        titleScroller(text.substr(1) + text.substr(0, 1));
    }, 400);
}("Welcome to Swetart's Comic Database! "));
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
app.factory('TestsFactory', function(HOST, $http){
  var factory = {};

  factory.runTests = function() {
    return $http.get(HOST + "/api/tests");
  }

  return factory;
});