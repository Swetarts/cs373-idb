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
      console.log("thumb", scope.type);

    }
  }
});
