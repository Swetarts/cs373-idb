// grab our gulp packages
var gulp   = require('gulp');
var gutil  = require('gulp-util');
var concat = require('gulp-concat');
var browserSync = require('browser-sync');
var reload = browserSync.reload;

// create a default task and just log a message
gulp.task('default', function() {
  return gutil.log('Gulp is running!')
});

gulp.task('concatjs', function() {
  return gulp.src('./www/assets/javascripts/**/*.js')
    .pipe(concat('main.js'))
    .pipe(gulp.dest('./www/dist'));
});

gulp.task('css', function() {
  return gulp.src('./www/assets/stylesheets/*.css')
    .pipe(reload({stream: true}));
});

gulp.task('serve', ['css'], function() {
  browserSync({
    proxy: "192.168.1.34:5000"
  });

  gulp.watch('./www/assets/stylesheets/*.css', ['css']);
});
