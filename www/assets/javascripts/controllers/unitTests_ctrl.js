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