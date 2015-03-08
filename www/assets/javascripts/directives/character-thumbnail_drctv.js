app.directive('characterThumbnail', function() {
  return {
    replace: true,
    templateUrl: '../../../templates/character-thumbnail.html',
    link: function(scope, element, attributes) {

      $(element).hover(function() {
        $('#characters-banner').attr('src', scope.character.image.screen_url);
      });
    }
  }
});
