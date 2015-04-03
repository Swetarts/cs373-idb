app.directive('thumbnailSummary', function(){
  return {
    scope: {
      collection: '=',
      type: '@'
    },
    restrict: 'E', 
    templateUrl: 'templates/thumbnail-summary.html'
});