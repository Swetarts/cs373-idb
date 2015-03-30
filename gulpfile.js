// grab our gulp packages
var gulp   = require('gulp');
var gutil  = require('gulp-util');
var concat = require('gulp-concat');

// create a default task and just log a message
gulp.task('default', function() {
  return gutil.log('Gulp is running!')
});

gulp.task('concatjs', function() {
  return gulp.src('./www/assets/javascripts/**/*.js')
    .pipe(concat('main.js'))
    .pipe(gulp.dest('./www/dist'));
});
