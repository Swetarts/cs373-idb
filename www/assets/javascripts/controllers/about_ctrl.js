app.controller('AboutCtrl', function($scope) {

	$scope.members = [
		{
			"name":"Sean Villars",
			"image":"http://i.imgur.com/uYwLx6k.jpg?1",
			"description":"I am a senior about to graduate in May of this year. I like skateboarding, programming, good beer, and kickin it with my bros. After I graduate I am going to start working as a Front End Engineer for Turnitin here in Austin.",
			"responsibilites":"I was responsible for the front end portion of our application. I set up Angular and programmed the characters, people, and issues poritons of our site along with the details pages for each of those. I also worked with Jerry to help get his feet wet in Angular where he successfully coded up the home and about pages.",
			"num_commits":"71",
			"num_issues":"15",
			"num_uTests":"3"
		},
		{
			"name":"Maximilian Brown",
			"image":"http://i.imgur.com/Ap2J5QI.jpg?1",
			"description": "Helped Tyler with the database, again."
			// "description":"Max is a Computer Science major at the University of Texas at Austin. He is married and has two children. When he isn't at work or school, he enjoys spending time with his family. Max recently started collecting comic books with his son and when they have time, Max and his son like to look for 'bad guys'.",
			"responsibilites":"Developed the data model/ UML diagram for the database utilizing navicat data modeler. Created python scripts to automate parsing of comicvine API data and populating our server hosted database. Worked with flask models to ensure compatibility with acutal data.",
			"num_commits":"20",
			"num_issues":"3",
			"num_uTests":"3"
		},
		{
			"name":"Gerardo Gamboa",
			"image":"http://i.imgur.com/vxbT1QN.jpg?1",
			"description":"When I’m not fighting crime and I almost never am, I’m studying at the GDC. This is my last semester studying Computer Science before I graduate with a BS and INFOSEC certificate. After graduation I hope to have more time to fight crime and save the city as well as working at AlienVault as a full time Software Engineer/superhero. My superhero origin story began in El Paso, TX until I moved to Austin, TX in 2009 to begin my studies and fight crime. Criminals beware!!!",
			"responsibilites":"My responsibilities included started my training in Angular in the front end aspect of the project. I worked with Sean to start practicing Angular and helped out with some things that later became making the home page and about page. Definitely feel a lot better with Angular than when I first started working on this project.",
			"num_commits":"14",
			"num_issues":"2",
			"num_uTests":"3"
		},
		{
			"name":"Aaron Dishman",
			"image":"http://i.imgur.com/9RzkScR.png?1",
			"description":"Dude's been crushing code for ~3 years, mostly in Java and C, but is up and coming in the Python game. His superpowers include the ability to transform any app into Mobile via Android Studio instantly. Once complete, you know the app is stable because he's mastered the skills of automated tests via Calabash. First appeared in UTCS in 2012, and will make the 'real world' debut this summer, May 2015!! POW! BAMM!",
			"responsibilites":"apiary design and edit, wiki/technical report write up, db population dev, db design, cat coralling",
			"num_commits":"17",
			"num_issues":"5",
			"num_uTests":"3"
		},
		{
			"name":"Tyler Corley",
			"image":"http://i.imgur.com/dLRQOmC.jpg?1",
			"description":"I'm a senior at the Univerity of Texas with humble beginnings from the small town of Longview, TX. I graduate in May with a job lined up at eBay in San Jose, CA. I enjoy programming, making music in and outside school, and occasionally finding ways to use emojis in my commit messages 💁.",
			"responsibilites":"Backend Bistro (Set up API calls to deliver serialized models), Fullmodel SQLAlchemist (Set up Flask models with SQLAlchemy and database migrations), Apiary Expert (Wrote out the API on Apiary.io), Defender of the SWErver (Set up the Rackspace instance and delegated SSH Authentication), and the One Who Dropped the [data]Base (Configured the PostgreSQL database users and mirrored the schema onto tables).",
			"num_commits":"7",
			"num_issues":"20",
			"num_uTests":"3"
		},
		{
			"name":"Alex Fortin",
			"image":"http://i.imgur.com/0IMTMLW.jpg?1",
			"description":"I enjoy playing soccer and drinking, preferably at the same time. Currently a senior studying brogramming at the University of America. Starting in the summer I will embark on a journey that is software engineering at Blackbaud.",
			"responsibilites":"Major responsibilities were setting up the database with the one and only Maximilian and populating it. This consisted of figuring out what attributes were needed, the relationships between attributes, and ultimately creating the schema's.",
			"num_commits":"25",
			"num_issues":"2",
			"num_uTests":"3"
		}
	]
});





