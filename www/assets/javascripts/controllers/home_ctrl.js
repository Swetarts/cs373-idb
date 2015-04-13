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

	$scope.video = '../assets/videos/bgvideo'+Math.floor(Math.random() * 9)+'.mp4';

	
  
});
