app.filter('fix_src', function(){
    return function(text) {
      return text.replace(/data-src/g, "src");
    };
});