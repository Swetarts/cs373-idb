# Environment
To get your application up and running you need a couple of things:
* [npm](https://www.npmjs.com/)
* [Bower](http://bower.io)
* Python 3.4

After you get bower installed, run this command inside of the **root** project directory (cs373-idb)
* $ bower install

This will create the directory **www/bower_components** and install all of our front end assets such as Angular and Bootstrap there.

After that create a python virtual environment with
* $ pyvenv-3.4 venv

This will create a directory called venv. 

To activate your virtual envrionment run:
* $ source venv/bin/activate

Now you can install all of the packages for our flask app and everything *should* work.

# Running the application
* $ python server.py
* visit localhost:5000/index.html
