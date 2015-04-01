// grab our gulp packages
var gulp          = require('gulp');
var gutil         = require('gulp-util');
var concat        = require('gulp-concat');
var autoprefixer  = require('gulp-autoprefixer');
var uglify        = require('gulp-uglify');
var ngAnnotate    = require('gulp-ng-annotate');
var rename        = require('gulp-rename');
var browserSync   = require('browser-sync');
var reload        = browserSync.reload;

gulp.task('js', function() {
  return gulp.src('./www/assets/javascripts/**/*.js')
    .pipe(concat('main.js'))
    .pipe(gulp.dest('./www/dist'));
});

gulp.task('minifyjs', function() {
  return gulp.src('./www/assets/javascripts/**/*.js')
    .pipe(ngAnnotate()) 
    .pipe(uglify())
    .pipe(rename('main.min.js'))
    .pipe(gulp.dest('./www/dist'));
});

gulp.task('css', function() {
  return gulp.src('./www/assets/stylesheets/*.css')
    .pipe(autoprefixer())
    .pipe(gulp.dest('./www/assets/stylesheets'))
    .pipe(reload({stream: true}));
});

gulp.task('serve', ['css', 'js'], function() {
  browserSync({
    proxy: "192.168.1.34:5000",
    open: false
  });

  gulp.watch('./www/assets/stylesheets/*.css', ['css']);
  gulp.watch('./www/assets/javascripts/**/*.js', ['js']).on('change', reload);
  gulp.watch('./www/templates/*.html').on('change', reload);
});


gulp.task('default', ['serve']);
