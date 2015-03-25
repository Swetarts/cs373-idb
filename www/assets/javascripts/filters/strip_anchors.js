app.filter('strip_anchors', function(){
    return function(text) {
      return text.replace(/<\/?a[^>]*>/g, "");
    };
});