[![Build Status](https://travis-ci.org/Swetarts/cs373-idb.svg?branch=master)](https://travis-ci.org/Swetarts/cs373-idb)

# Environment
To get your application up and running you need a couple of things:
* [npm](https://www.npmjs.com/)
* [Bower](http://bower.io)
* Python 3.4
* [Gulp](http://gulpjs.com/)

After you get bower installed, run this command inside of the **root** project directory (cs373-idb)
```bash
$ bower install
```

This will create the directory `www/bower_components` and install all of our front end assets such as Angular and Bootstrap there.

Next install gulp and dependencies
```bash
$ npm install -g gulp
...
$ npm install
```

You can now run gulp tasks. For default just run
```bash
$ gulp
```
This will kick off the browser-sync server. You might need to adjust the `proxy` setting inside of `gulp.js` to point at wherever you are hosting your local server.

After you install the bower components you need to install the `gulp` dependencies.Run:
```bash
$ npm install
```
This will install all of the dev dependencies inside of the `package.json` file.

### **Important**
You must at least run `$ gulp js` in order to generate the `main.js` file that is used in `index.html`. Failing to do so will leave you with an empty site.

After that create a python virtual environment with
```bash
$ pyvenv-3.4 venv
```

This will create a directory called venv.

To activate your virtual envrionment run:
```bash
$ source venv/bin/activate
```

Note: You may receive an error while attempting to create the virtual environment in Ubuntu 14.04. Apparently Ubuntu 14.04 was shipped with a broken pyvenv. Do the following. This will create the venv without pip. Get pip in the environment afterwards.

```bash
$ pyvenv-3.4 --without-pip venv
```

Now you can install all of the packages for our flask app and everything *should* work. To do this run
```bash
pip3 install -r requirements.txt
```

# Playing with the database
When you're in the server, to get to the postgreSQL instance
```bash
postgres@swerver:/$ sudo -iu postgres
postgres@swerver:/$ psql
psql (9.3.6)
Type "help" for help.

You are now connected to database "swetards" as user "postgres".
```

## Popular Commands in `psql`
* `\connect <dbname>` - connect to that database
* `\q` - quit
* `\dt` - list tables in database
* `\l` - list databases

# Running the application
* `$ python server.py`
* visit localhost:5000/index.html

# Server Information
The Server lives at `104.239.165.88`

To log in run
```bash
ssh -i .ssh/id_rsa.pub swetard@104.239.165.88
```

# Running Tests
* `$ python3 tests.py`

Note: If you recieve an 'ImportError: No module named 'psycopg2'' run
* `$ pip install psycopg2`
and it should fix it


